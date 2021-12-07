
import discord
import os
import requests
import json
import yaml

SC = open('Starcraft.json')

SCData = json.load(SC)
SCDataFinal = json.dumps(SCData['Starcraft'][0]["Marine"][0]["Strong Against"]["Zerg"],indent=4)

my_secret = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!'):
    input = message.content[1:]
    splitInput = input.split(' ')
    firstInput = splitInput[0].title()
    shortcut_word = ["bc", "st", "ht", "dt", "wm", "pf", "mt", "at", "sh", "bl", "nd", "wp", "vr", "pc", "sb"]
    properly_word = ["Battlecruiser", "Siege Tank", "High Templar", "Dark Templar", "Widow Mine", "Planetary Fortress", "Missile Turret", "Auto Turret", "Swarm Host", "Brood Lord", "Nydus Worm", "Warp Prism", "Void Ray", "Photon Cannon", "Shield Battery"]


    try:
      if len(splitInput) == 1:
        for word in shortcut_word:
            if firstInput.lower() == word:
              counter = shortcut_word.index(word)
              firstInput = properly_word[counter]
        await message.channel.send(yaml.safe_dump(SCData['Starcraft'][0][firstInput], indent=4))

      if len(splitInput) > 1:
        if "." in input:
          
          dotInput = input.split('.')
          twoWordInput = dotInput[0].rstrip()
          twoWordInputSecond = dotInput

          for word in shortcut_word:
            if twoWordInput == word:
              counter = shortcut_word.index(word)
              twoWordInput = properly_word[counter]

          if ("Zerg" in twoWordInputSecond) or ("zerg" in twoWordInputSecond):
            await message.channel.send("Strong Against: " + yaml.dump(SCData['Starcraft'][0][twoWordInput.title()][0]["Strong Against"]["Zerg"], default_style="", explicit_end=None) + "Weak Against: " + yaml.dump(SCData['Starcraft'][0][twoWordInput.title()][1]["Weak Against"]["Zerg"], default_style="", explicit_end=None))
          elif ("Protoss" in twoWordInputSecond) or ("protoss" in twoWordInputSecond):
            await message.channel.send("Strong Against: " + yaml.dump(SCData['Starcraft'][0][twoWordInput.title()][0]["Strong Against"]["Protoss"], default_style="", explicit_end=None) + "Weak Against: " + yaml.dump(SCData['Starcraft'][0][twoWordInput.title()][1]["Weak Against"]["Protoss"], default_style="", explicit_end=None))
          elif (".Terran" in twoWordInputSecond) or ("terran" in twoWordInputSecond):
            await message.channel.send("Strong Against: " + yaml.dump(SCData['Starcraft'][0][twoWordInput.title()][0]["Strong Against"]["Terran"], default_style="", explicit_end=None) + "Weak Against: " + yaml.dump(SCData['Starcraft'][0][twoWordInput.title()][1]["Weak Against"]["Terran"], default_style="", explicit_end=None))
          else: return
        
        if not "." in input:
          secondInput = splitInput[1].title()
          await message.channel.send(yaml.safe_dump(SCData['Starcraft'][0][firstInput + ' ' + secondInput], indent=4))
    except:
      await message.channel.send('Wrong unit name or something')

client.run(my_secret)