#Nico.py Version 1.0.2

import discord
import asyncio
import requests
import json

client = discord.Client()
cbkey = 'cool cat loves to boogie woogie'
ocrkey = 'no'

prefix = "n!"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_status(game=discord.Game(name='Version 1.0.2'))   

@client.event
async def on_message(message):
    if message.content.startswith(prefix) and message.author.id != client.user.id and len(message.content) > 1:
    #if the message starts with "n!", the message is NOT sent by the bot himself and if its not blank
        command = message.content.split()[0][len(prefix):].lower()
        #keep only the actual command from the message, remove the prefix and make it lowercase
        args = message.content.replace(command, "").replace(prefix, "")[1:]
        #the rest of the message ex: "n!haha yes mama" in this case, "yes mama" is args 

        if command == "banwho":
            await client.send_message(message.channel, 'ban lucas tbh')
            
        elif command == "help":
            await client.send_file(message.channel, "help.png")

        elif command == "duck":
             await client.send_message(message.channel, 'quack')
        
        elif command == "cheese":
             await client.send_message(message.channel, 'http://i.imgur.com/LbDn23x.png')

        elif command == "succ":
            await client.send_message(message.channel, 'l...lewd')

        elif command == "nigra":
            await client.send_message(message.channel, 'https://www.youtube.com/watch?v=V4jH0WeV67I')

        elif command == "igra":
            await client.send_message(message.channel, 'https://www.youtube.com/watch?v=V4jH0WeV67I')

        elif command == "gra":
            await client.send_message(message.channel, 'https://www.youtube.com/watch?v=V4jH0WeV67I')
            
        elif command == "c":
            r = requests.get("https://www.cleverbot.com/getreply?key=%s&input=%s" % (cbkey, args))
            await client.send_message(message.channel, r.json()['output'])  
                                      
        elif command == "cleverbot":
            r = requests.get("https://www.cleverbot.com/getreply?key=%s&input=%s" % (cbkey, args))
            await client.send_message(message.channel, r.json()['output'])
            
        elif command == "clever":
            r = requests.get("https://www.cleverbot.com/getreply?key=%s&input=%s" % (cbkey, args))
            await client.send_message(message.channel, r.json()['output'])
            
        elif command == "ocr":
            r = requests.get("https://api.ocr.space/parse/imageurl?apikey=%s&url=%s" % (ocrkey, args))

            if len(r.json()['ParsedResults'][0]['ParsedText']) > 0:
                await client.send_message(message.channel, r.json()['ParsedResults'][0]['ParsedText'])
            else:
                await client.send_message(message.channel, "No text found. If this error persists, ping Mosaic or one of the GitHub contributors.")
        
        elif command == "moozy":
            userch = message.author.voice_channel
            if userch is None:
                await client.send_message(message.channel, "Please join a voice channel before using this command.")
                return
            else:
                waitpls = await client.send_message(message.channel, "Please wait...")
                voice = await client.join_voice_channel(userch)
                player = await voice.create_ytdl_player(args)
                player.start()
                await client.edit_message(waitpls, "**Now playing:** %s" % player.title)
                while player.is_done() == False:
                    pass
                await client.edit_message(waitpls, "**Finished playing:** %s" % player.title)
                await voice.disconnect()

        elif command == "music":
            userch = message.author.voice_channel
            if userch is None:
                await client.send_message(message.channel, "Please join a voice channel before using this command.")
                return
            else:
                waitpls = await client.send_message(message.channel, "Please wait...")
                voice = await client.join_voice_channel(userch)
                player = await voice.create_ytdl_player(args)
                player.start()
                await client.edit_message(waitpls, "**Now playing:** %s" % player.title)
                while player.is_done() == False:
                    pass
                await client.edit_message(waitpls, "**Finished playing:** %s" % player.title)
                await voice.disconnect()

client.run('nico nico niiiiii~~~')
