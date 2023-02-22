# Simple Discord Bot in Python
[![License: Unlicense](https://img.shields.io/github/license/Anonym-Guy/simplediscordbot)](https://opensource.org/license/unlicense/) ![Python](https://img.shields.io/badge/python-3.11-yellow.svg) ![Watchers](https://img.shields.io/github/watchers/Anonym-Guy/simplediscordbot.svg) ![RepoSize](https://img.shields.io/github/repo-size/Anonym-Guy/simplediscordbot?color=purple)  
This bot can send random text from txt file or random image from directory and it can delete message if the message contains word that you banned. It can also send and article from wikipedia based on user input. Users can create their own qrcode. And simple chat system (bot can response if someone write his name).

## Table of contents
* [Features](#features)
* [How to use it](#how-to-use-it)
* [Commands](#commands)
* [Screenshots](#screenshots)

## Features
1. Random text from file
2. Random images from folder
3. Banned words from txt file
4. Send wikipedia article based on user input
5. Create qr code based on user input
6. Send 3 news
7. Rock Paper and Scissors game
8. Random number in range, based on user input
9. Guess the number game
10. Convert currency to another currency
11. Simple chat system
 
## How to use it 
1. Install [python](https://www.digitalocean.com/community/tutorials/install-python-windows-10) and [pip](https://www.liquidweb.com/kb/install-pip-windows/)   
2. Download and unzip [repository](https://github.com/Anonym-Guy/simplediscordbot/archive/refs/heads/main.zip)
3. Open unziped folder
4. Install modules (open cmd or powershell in unziped folder)  
```pip install -r requirements.txt``` 
5. Get a Discord [Bot Token](https://www.writebots.com/discord-bot-token/)  
-When adding a discord bot to your server give him permissions : Read Messages/View Channels, Send Messages, Manage Messages, Embed Links, Attach Files, Read Message History          
6. [Enable intent](https://autocode.com/discord/threads/what-are-discord-privileged-intents-and-how-do-i-enable-them-tutorial-0c3f9977/) for bot  
-Enable only message content intent
7. Create file named .env in main unziped folder and add ```DISCORD_TOKEN='YOURSUPERSECRETTOKEN'``` replace the YOURSUPERSECRETTOKEN with your bot token (keep the quotation marks)  
8. Customize [words](./text/text.txt), [images](./images) and [banned words](./ban%20words/words.txt)  
9. Customize your [bot response name](./bot.py) for chat system in bot.py   
```name_to_react = ("yourname","yoursecondname")```

## Commands
**!text** (random text from text.txt file)   
**!image** (random image from images folder)   
**!whatis** (Send wikipedia article based on user input)   
**!qrcode "what do you want in qrcode"** (Send qrcode based on user input)   
**!news** (Send 3 news)   
**!rpas "you can choice rock,paper,scissors"** (Rock Paper and Scissors game)   
**!random from "your number" to "your number"** (Random number)   
**!gtn** (Guess the number game)  
**!convert** (Convert currency to another currency)  

## Screenshots
<p float="left">
  <img src="/screenshots/screen1.png?raw=true" alt="Screenshot of rock, paper and scissor" width="500" height="350" />
  <img src="/screenshots/screen2.png?raw=true" alt="Wikipedia search command" width="500" height="350" /> 
  <img src="/screenshots/screen3.png?raw=true" alt="Qrcode creator" width="500" height="350" />                                                                   <img src="/screenshots/screen4.png?raw=true" alt="Random number generator" width="500" height="350" />                      
</p>
