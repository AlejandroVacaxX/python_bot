import discord
from dotenv import load_dotenv # i use this library for safety, so i dont have to share mi token in github
import os
import requests
import json 
# it seems tha the meme api is down, so in the test it didnt work
def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = response.json()
  
  # i make this because the API is down, it broke mi code.
  print("this is the message from the API ", json_data)
  # -------------------

  if 'url' in json_data:
      return json_data['url']
  else:
      # i send this message to the discord server
      return "i can´t find a meme :( look up the console."

# this is the funcion that make the API request to get a dog picture
def get_dog():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        json_data = response.json()
        return json_data['message']
    # this a exception handler, thanks to this the code dont crash if something wrong happend
    except Exception as e:
        print(e)
        return "No pude encontrar un perrito :("

# with this i load the variables from my .env

load_dotenv()

#this messages are used in the bot responses
mensaje = 'Por lo que he oido es el amor de tu vida, pareces muy enamorado de ella, que envidia. 😍'
amorDeVida = 'Quitze Carranza 🌸'


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        # i use a  if statemantes to check the bot, is not efficient 
        # the last message is for my girlfriend
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        
        if message.content.startswith('$bye'):
            await message.channel.send('Good Bye!')
            
        if message.content.startswith('$Quitze'):
            await message.channel.send(mensaje)
        # this message is for impress my girlfriend 🫡
        if message.content.startswith('$¿quien es el amor de mi vida bot?'):
            await message.channel.send(amorDeVida)

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

        #you have to put "$dog" in the discord message to get a dog picture
        if message.content.startswith('$dog'):
            # this tell to the user that we are doing something, i think it look cool
            #make the experience more nice
            await message.channel.send("Looking for the cutties dog... 🐶")
            
            meme_url = get_dog()
            await message.channel.send(meme_url)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
discord_token = os.getenv('DISCORD_TOKEN')

#i make this if to look for error, if your discord token dont work or
# you dont have install the dotenv library the code will not brake.

if discord_token == None:
  print('Error: please check your token or your .evn file')
else:
    print("Turn on the bot...")
    client.run(discord_token)