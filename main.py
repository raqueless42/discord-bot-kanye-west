import discord 
import requests 
import json 
import random
from keep_alive import keep_alive


client = discord.Client ()

ye_trigger = ["presidente", "kim", "dinheiro", "música", "musica", "escravo", "estados unidos", "YE", "kanye", "west", "kardashian", "heartless", "trump", "taylor swift"]

ye_words = ["YE"]

def get_quote():
  response = requests.get ("https://api.kanye.rest")
  json_data = json.loads(response.text)
  quote = json_data
  return (quote)
 
@client.event
async def on_ready():
  print('Logamos como {0.user}'.format(client))

@client.event
async def on_message(message):
  if message .author == client.user:
    return

  msg = message.content

  if msg.startswith('YE'):
    quote = get_quote()
    await message.channel.send(quote)


  if any(word in msg for word in ye_trigger):
    await message.channel.send(random.choice(ye_words))


server = ('OTY5MjI4Mzg2NTIwMTM3Nzc5.YmqWRg.vD6jIVZUasLQm-c3e-Vkcujjk5M')

keep_alive()
client.run(server)