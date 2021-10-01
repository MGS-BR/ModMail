import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
client.help_command = commands.MinimalHelpCommand()

@client.event
async def on_ready():

    print(f'{client.user.name} ONLINE!')

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ModMail'))

@client.command(aliases=['modmail', 'suporte'])
@commands.dm_only()
async def support(ctx):

    guild = client.get_guild(id=your server id)
    guild_channel = client.get_channel(modmail chat id)
    user_channel = await ctx.author.create_dm()

    solicitacao_user = discord.Embed(
        title='Suporte',
        description=f'Solicitação de suporte enviada para: {guild.name}',
        color = discord.Color.blue()
    )
    solicitacao_user.set_footer(text=f'Guild id: {guild.id}')

    solicitacao_guild = discord.Embed(
        title='Solicitação de Suporte',
        description=f'{ctx.author} enviou uma solicitação de suporte.\nPara aceitar o suporte digite **"accept {ctx.author.id}"**.\nPara negar a solicitação digite **"decline {ctx.author.id}"**.\nApós aceitar o suporte digite **"close {ctx.author.id}"** para encerrar o suporte.',
        color=discord.Color.blue()
    )
    solicitacao_guild.set_footer(text=f'User id: {ctx.author.id}')

    await user_channel.send(embed=solicitacao_user)
    await guild_channel.send(embed=solicitacao_guild)

    def check1(m):
        return m.channel == guild_channel

    while True:

        confirmaçao = await client.wait_for('message', check=check1)

        if confirmaçao.content == f'accept {ctx.author.id}':

            solicitacao_aceita = discord.Embed(
                title='Solicitação de suporte aceita',
                description='Envie a sua mensagem para conversar com o suporte.',
                color = discord.Color.blue()
            )
            await user_channel.send(embed=solicitacao_aceita)
            await confirmaçao.add_reaction('✅')
            break
        
        elif confirmaçao.content == f'decline {ctx.author.id}':
            
            solicitacao_negada = discord.Embed(
                title='Solicitação de suporte recusada',
                description='Infelizmente a sua solicitação de suporte foi recusada.',
                color= discord.Color.blue()
            )
            await user_channel.send(embed=solicitacao_negada)
            await confirmaçao.add_reaction('✅')
            return
            
    def check2(m):
        return m.author == ctx.author and m.channel == ctx.author.dm_channel
    
    def check3(m):
        return m.channel == guild_channel

    while True:
        
        msg_user = await client.wait_for('message', check=check2, timeout=60)

        mensagem_enviada_user = discord.Embed(
            description=f'Mesagem envida para **{guild.name}**\nPor favor aguarde a respota do suporte.',
            color=discord.Color.blue()
        )

        await guild_channel.send(f'**{ctx.author}**: {msg_user.content}')
        await user_channel.send(embed=mensagem_enviada_user)

        msg_guild = await client.wait_for('message', check=check3)

        mensagem_enviada_guild = discord.Embed(
            description=f'Mesagem envida para **{ctx.author}**\nPor favor aguarde a resporta do usuario.',
            color=discord.Color.blue()
        )

        if msg_guild.content == f'close {ctx.author.id}':

            suppot_close_user = discord.Embed(
                description=f'Suporte com **{guild.name} encerrado**.',
                color=discord.Color.blue()
            )

            suppot_close_guild = discord.Embed(
                description=f'Suporte com **{ctx.author} encerrado**.',
                color=discord.Color.blue()
            )

            await user_channel.send(embed=suppot_close_user)
            await guild_channel.send(embed=suppot_close_guild)
            
            break
        
        await user_channel.send(f'**{guild.name}**: {msg_guild.content}')
        await guild_channel.send(embed=mensagem_enviada_guild)

client.run('Token here')
