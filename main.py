import discord
import asyncio
import requests
import json
from discord.ext import commands
from time import sleep
from math import trunc
from random import choice

client = commands.Bot(command_prefix = ".")   #prefix
client.remove_command('help')
mensagem_bonitinha = ('Analisando minha bolsa de valores:chart_with_upwards_trend:...Por favor aguarde.') #message before value

print('software online')
sleep(1)
print('booting up bot...')

@client.event
async def on_ready():
    print('bot online')


class Exchange():
    def __get_cotacao(self, url, coin):
        self.url = url
        self.coin = coin
        
    
    def dolar(self):
        coin = "USD"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]
        

    def euro(self):
        coin = "EUR"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]


    def iene(self):
        coin = "JPY"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]


    def coroa(self):
        coin = "DKK"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]
    
    def rublo(self):
        coin = "RUB"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]   
        strvalor = str(valor)
        return strvalor[0:4]
     

    def canadense(self):
        coin = "CAD"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]

    def hongkong(self):
        coin = "HKD"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]


    def franco(self):
        coin = "CHF"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        strvalor = str(valor)
        return strvalor[0:4]


    def mexico(self):
        coin = "MXN"
        url = "https://api.exchangeratesapi.io/latest?base=" + (coin)
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = (cotacao["rates"] ["BRL"])
        strvalor = str(valor)
        return strvalor[0:4]
  
moeda = Exchange()

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Stonks. Bem vindo.')
    embed.add_field(name=".dolar", value='Informa a cotação do Dólar.', inline = False)
    embed.add_field(name=".franco", value='Informa a cotação do Franco Suíço.', inline = False)
    embed.add_field(name=".canadense", value='Informa a cotação do Dólar Canadense.', inline = False) #help structure
    embed.add_field(name=".iene", value='Informa a cotação do Iene.', inline = False)
    embed.add_field(name=".euro", value='Informa a cotação do Euro.', inline = False)
    embed.add_field(name=".rublo", value='Informa a cotação do Rublo.', inline = False)
    embed.add_field(name=".honkong", value='Informa a cotação do Dólar de Hong Kong.', inline = False)
    embed.add_field(name=".mexico", value='Informa a cotação do Peso mexicano de Hong Kong.', inline = False)
    embed.add_field(name=".coroa", value='Informa a cotação da Coroa dinamarquesa de Hong Kong.', inline = False)
    embed.add_field(name=".converter", value='Converte um valor em Dólar para Real.', inline = False)
    embed.add_field(name=".vbuck", value='Informa o preço do Vbuck.', inline = False)
    embed.add_field(name=".roubo", value='Fala umas verdades.', inline = False)
    await ctx.send(author, embed=embed)


@client.command()
async def dolar(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Dolar está custando R${moeda.dolar()}. :money_with_wings:'))

@client.command()
async def euro(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Euro está custando R${moeda.euro()}. :money_with_wings:'))

@client.command()
async def iene(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Iene está custando R${moeda.iene()}. :money_with_wings:'))

@client.command()
async def coroa(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Coroa Dinamarquesa está custando R${moeda.coroa()}. :money_with_wings:'))

@client.command()
async def rublo(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Rublo está custando R${moeda.rublo()}. :money_with_wings:'))

@client.command()
async def canadense(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Dolar canadense está custando R${moeda.canadense()}. :money_with_wings:'))

@client.command()
async def hongkong(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Iene de Hongkong está custando R${moeda.hongkong()}. :money_with_wings:'))

@client.command()
async def franco(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Franco Suíço está custando R${moeda.franco()}. :money_with_wings:'))

@client.command()
async def mexico(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Peso mexicano está custando R${moeda.mexico()}. :money_with_wings:'))

@client.command()
async def vbuck(ctx):
    await ctx.send(mensagem_bonitinha)
    sleep(1)
    await ctx.send('KKKKKKKKK VBUCK TA CARO DEMAIS MANO. VAI DAR NAO.')#vbuck

@client.command()
async def roubo(ctx):
    msg = await ctx.send('IMPOSTO')
    sleep(1)
    await msg.edit(content=('É'))
    sleep(1)
    await msg.edit(content=("ROBÔ :robot:"))

@client.command()
async def stonks(ctx):
    await ctx.send('Estou aqui para te ajudar com conversão de moedas.')
    sleep(1)
    await ctx.send('Digite ".help" para ver o que posso fazer!')

@client.command()
async def converter(ctx, arg=1):
    try:
        url = "https://api.exchangeratesapi.io/latest?base=USD"
        requisicao = requests.get(url)
        cotacao = json.loads(requisicao.text)
        valor = cotacao["rates"] ["BRL"]
        multiplicacao = int(arg) * float(valor)        #convert
        await ctx.send (f'{arg} Dolares valem mais ou menos {trunc(multiplicacao)} Reais.')

    except:
        await ctx.send("Formato não suportado. Tente usar ponto ao invés de vírgula.")



client.run('token')