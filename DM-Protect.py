import discord, asyncio

token = 'token'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(m):
    await asyncio.sleep(20)
    i = discord.Embed(title='서버 멤버가 보내는 다이렉트 메시지 허용하기를 꺼주시기 바랍니다.',color=0x2f3136)
    i.set_image(url='')
    channel = client.get_guild(m.guild.id).text_channels[0]
    i = await channel.create_invite(max_uses=1)

    try:
        await m.send(embed=i)
        await m.send(i)
        await m.kick()
    except:
        pass


client.run(token)
