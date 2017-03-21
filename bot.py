import discord
import asyncio

client = discord.Client()

prefix = "n!"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
   

@client.event
async def on_message(message):
    if message.content.startswith(prefix) and message.author.id != client.user.id and len(message.content) > 1:
    #if the message starts with "n!", the message is NOT sent by the bot himself and if its not blank
        command = message.content.split()[0][len(prefix):].lower()
        #keep only the actual command from the message, remove the prefix and make it lowercase
        args = message.content.replace(command, "").replace(prefix, "")[1:]
        #the rest of the message ex: "n!haha yes mama" in this case, "yes mama" is args 
        
        #remember to always use "elif" for new commands, not "if"
        
        
        if command == "banwho":
            await client.send_message(message.channel, 'ban lucas tbh')
        elif command == "help":
            await client.send_message(message.channel, 'ask mosaic, if i explained them all i would break') 
        elif command == "sipp":
            await client.send_message(message.channel, 'why sipp when you can s u c c')
            
        elif command == "duck":
            await client.send_message(message.channel, 'quack')
            
        elif command == "cheese":
            await client.send_message(message.channel, 'http://i.imgur.com/LbDn23x.png')
            
        elif command == "test":
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1
            await client.edit_message(tmp, 'You have {} messages.'.format(counter))
            
        elif command == "ping":
            await client.send_message(message.channel, 'check your own ping lazy ass')
            
        elif command == "sleep":
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')

        elif command == "wew":
            await client.send_message(message.channel, 'wew lad')
            
        elif command == "succ":
            await client.send_message(message.channel, 'l...lewd')
            
    elif message.content.lower == 'sup, nico' and message.author.id != client.user.id:
        await client.send_message(message.channel, 'YO YO YO YO! WHAT IT IS, MOTHERFUCKERS!?')
        
    elif message.content.lower == 'nico nico ni' and message.author.id != client.user.id:
        await client.send_message(message.channel, 'Stop')

client.run('no')
