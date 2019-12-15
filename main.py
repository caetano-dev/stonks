import discord
import asyncio
from discord.ext import commands
import urllib.request as req
import re
#--------------------------------------------
class Cotacao:

    def __get_cotacao(self, url, regex='^.*nacional" value="([0-9,]+)"'):
        pagina = req.urlopen(url)
        s = pagina.read().decode('utf-8')

        m = re.match(regex, s, re.DOTALL)
        if m:
            return float(m.group(1).replace(',', '.'))
        else:
            return 0

    def dolar(self):
        return self.__get_cotacao('http://dolarhoje.com/')

    def euro(self):
        return self.__get_cotacao('http://eurohoje.com/')

    def libra(self):
        return self.__get_cotacao('http://librahoje.com/')

    def rublo(self):
        return self.__get_cotacao('https://dolarhoje.com/rublo-russo-hoje/')

    def peso(self):
        return self.__get_cotacao('https://dolarhoje.com/peso-argentino/')

    def bitcoin(self):
        return self.__get_cotacao('https://dolarhoje.com/bitcoin-hoje/')

cotacao = Cotacao()
#-----------------------------------------------------------------------------------------------------------------------
mensagem_bonitinha = ('Analisando minha bolsa de valores:chart_with_upwards_trend:...Por favor aguarde.')

client = commands.Bot(command_prefix = '!')

print('software online')
@client.event
async def on_ready():
    print('bot online')

#----------------    #comandos

@client.command()
async def dolar(ctx):
    await ctx.send(mensagem_bonitinha)     
    await ctx.send(f'1 Dolar está custando {cotacao.dolar()} reais :money_with_wings: ')    #dolar


@client.command()                     
async def euro(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Euro está custando {cotacao.euro()} reais :money_with_wings: ')      #euro

@client.command()  
async def libra(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Libra está custando {cotacao.libra()} reais :money_with_wings: ')     #libra

@client.command()  
async def rublo(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Rublo Russo está custando {cotacao.rublo()} reais :money_with_wings: ')   #rublo

@client.command()  
async def peso(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Peso Argentino está custando {cotacao.peso()} reais :money_with_wings: ')    #peso

@client.command()  
async def bitcoin(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Bitcoin está custando {cotacao.bitcoin()} reais :money_with_wings: ')     #bitcoin

@client.command()  
async def vbuck(ctx):
    await ctx.send('KKKKKKKKK VBUCK TA CARO PRA CARALHO')     #vbuck

# @client.command()  
# async def (ctx):
#     await ctx.send('')



client.run(#token) 


