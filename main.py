import discord
import asyncio
from discord.ext import commands
import urllib.request as req
import re
#--------------------------------------------
class Cotacao:

    def __get_cotacao(self, url, regex='^.*nacional" value="([0-9,]+)"'):   #pegar o valor das moedas
        pagina = req.urlopen(url)
        s = pagina.read().decode('utf-8')

        m = re.match(regex, s, re.DOTALL)
        if m:
            return float(m.group(1).replace(',', '.'))
        else:
            return 0

    def dolar(self):
        return (self.__get_cotacao('http://dolarhoje.com/'))

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

dolar_float = float(cotacao.dolar())
#-----------------------------------------------------------------------------------------------------------------------
client = commands.Bot(command_prefix = ".")  #prefixo do bot 
client.remove_command('help') #remove o comando help para fazer um personalizado
mensagem_bonitinha = ('Analisando minha bolsa de valores:chart_with_upwards_trend:...Por favor aguarde.') #mensagem antes dos valores

print('software online')
@client.event
async def on_ready():
    print('bot online')

#-----------------------------------------    #comandos
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author        
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Stonks. Bem vindo.')
    embed.add_field(name=".dolar", value='Informa a cotação do Dolar.', inline = False)
    embed.add_field(name=".euro", value='Informa a cotação do Euro.', inline = False)
    embed.add_field(name=".rublo", value='Informa a cotação do Rublo.', inline = False)
    embed.add_field(name=".bitcoin", value='Informa a cotação do Bitcoin.', inline = False)       #help
    embed.add_field(name=".peso", value='Informa a cotação do Peso Argentino.', inline = False)
    embed.add_field(name=".libra", value='Informa a cotação da Libra.', inline = False)
    embed.add_field(name=".converter", value='Converte um valor em Dolar para Real.', inline = False)
    embed.add_field(name=".imposto", value='Fala umas verdades.', inline = False)
    await ctx.send(author, embed=embed)
    
@client.command()                          
async def dolar(ctx):
    await ctx.send(mensagem_bonitinha)     
    await ctx.send(f'1 Dolar está custando {cotacao.dolar()} Reais. :money_with_wings: ')    #dolar

@client.command()                     
async def euro(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Euro está custando {cotacao.euro()} Reais. :money_with_wings: ')      #euro

@client.command()  
async def libra(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Libra está custando {cotacao.libra()} Reais. :money_with_wings: ')     #libra

@client.command()  
async def rublo(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Rublo Russo está custando {cotacao.rublo()} Reais. :money_with_wings: ')   #rublo

@client.command()  
async def peso(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Peso Argentino está custando {cotacao.peso()} Reais. :money_with_wings: ')    #peso

@client.command()  
async def bitcoin(ctx):
    await ctx.send(mensagem_bonitinha)
    await ctx.send(f'1 Bitcoin está custando {cotacao.bitcoin()} Reais. :money_with_wings: ')     #bitcoin

@client.command()  
async def vbuck(ctx):
    await ctx.send('KKKKKKKKK VBUCK TA CARO PRA CARALHO')                                         #vbuck

@client.command()                
async def imposto(ctx):                      
    await ctx.send('IMPOSTO É ROUBO :angry:')

#------------------------------------------------------------------------------------

@client.command()
async def converter(ctx, arg):
    multiplicacao = (float("{0:.4}".format(dolar_float))*float("{0:.4}".format(arg)))        #converter
    await ctx.send (f'{arg} Dolares valem mais ou menos {multiplicacao} Reais.')

#------------------------------------------------------------------------------------------------------

client.run('#TOKEN') 
