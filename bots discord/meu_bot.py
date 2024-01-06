import discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'message.author.name as regras do servidor são: \n 1- Não pode cantar o hino do atlético \n 2- Não pode dar o cuzinho dia de sabado \n 3- Tem que usar a camisa do cruzeiro pelo menos uma vez na semava \n 4- Tem que usar o meme do coisa ruim voltou a cada vitória do cruzeiro')

        elif message.content == '?chama no pv':
            await message.author.send('Deixa de viadagem')

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'O viado do {member.mention} chegou no {guild.name}'
            await guild.system_channel.send(mensagem)

client = MyClient(intents=intents)
client.run('MTE4NTYxMzc2NjY3MTQ2NjQ5Nw.GP2d-4.s1FyJT69s-Vvcrm1kndCnD29wYGY1z7bRSklq4')
