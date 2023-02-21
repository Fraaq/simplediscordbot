# simplediscordbot
Simple python discord bot. This bot can send random text from txt file or random image from directory and it can delete message if the message contains word that you banned. It can also send and article from wikipedia based on user input. Users can create their own qrcode. And simple chat system (bot can response if someone write his name).

## Table of contents
* [Features](#features)
* [How to use it](#how-to-use-it)
* [Commands](#commands)

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
1. Install [python](https://www.digitalocean.com/community/tutorials/install-python-windows-10) and [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)   
2. [Install](https://www.geeksforgeeks.org/how-to-install-a-python-module/) modules  
```pip install -r requirements.txt``` 
3. Get a Discord [Bot Token](https://www.writebots.com/discord-bot-token/)
4. Enable [message content intent](https://autocode.com/discord/threads/what-are-discord-privileged-intents-and-how-do-i-enable-them-tutorial-0c3f9977/) for bot 
5. Create file named .env in main directory and add ```DISCORD_TOKEN='YOURSUPERSECRETTOKEN'``` replace the YOURSUPERSECRETTOKEN with your bot token   
6. Customize [words](./text/text.txt), [images](./images) and [banned words](./ban%20words/words.txt)  
7. Customize your [bot response name](./bot.py) for chat system (change the list "name_to_react" on bottom of the file to what you want)

## Commands
<b>!text</b> (random text from text.txt file)   
<b>!image</b> (random image from images folder)   
<b>!whatis</b> (Send wikipedia article based on user input)   
<b>!qrcode "what do you want in qrcode"</b> (Send qrcode based on user input)   
<b>!news</b> (Send 3 news)   
<b>!rpas "you can choice rock,paper,scissors"</b> (Rock Paper and Scissors game)   
<b>!random from "your number" to "your number"</b> (Random number)   
<b>!gtn</b> (Guess the number game)  
<b>!convert</b> (Convert currency to another currency)  
