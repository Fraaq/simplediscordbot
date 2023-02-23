# Simple Discord Bot in Python
[![License: Unlicense](https://img.shields.io/github/license/Anonym-Guy/simplediscordbot)](https://opensource.org/license/unlicense/) ![Python](https://img.shields.io/badge/python-3.11-yellow.svg) ![Watchers](https://img.shields.io/github/watchers/Anonym-Guy/simplediscordbot.svg) ![RepoSize](https://img.shields.io/github/repo-size/Anonym-Guy/simplediscordbot?color=purple)  
This bot can send random text from txt file or random image from directory and it can delete message if the message contains word that you banned. It can also send and article from wikipedia based on user input. Users can create their own qrcode. And simple chat system (bot can response if someone write his name).

## Table of contents
* [Features](#features)
* [How to use it](#how-to-use-it)
* [How to customize bot](#how-to-customize-bot)
* [Commands](#commands)
* [Screenshots](#screenshots)

## Features
* Random text from file
* Random images from folder
* Banned words from txt file
* Send wikipedia article based on user input
* Create qr code based on user input
* Send 3 news
* Rock Paper and Scissors game
* Random number in range, based on user input
* Guess the number game
* Convert currency to another currency
* Simple chat system
 
## How to use it 
1. Install [python](https://www.digitalocean.com/community/tutorials/install-python-windows-10) and [pip](https://www.liquidweb.com/kb/install-pip-windows/)   
2. Download and unzip [this repository](https://github.com/Anonym-Guy/simplediscordbot/archive/refs/heads/main.zip)
3. Open unziped folder
4. Install modules (open cmd or powershell in unziped folder)  
```pip install -r requirements.txt``` 
5. Get a Discord [Bot Token](https://www.writebots.com/discord-bot-token/)  
-When adding a discord bot to your server give him permissions : Read Messages/View Channels, Send Messages, Manage Messages, Embed Links, Attach Files, Read Message History          
6. [Enable intent](https://autocode.com/discord/threads/what-are-discord-privileged-intents-and-how-do-i-enable-them-tutorial-0c3f9977/) for bot  
-Enable only message content intent
7. Create file named .env in main unziped folder and open it with notepad. Add ```DISCORD_TOKEN='YOURSUPERSECRETTOKEN'``` replace the YOURSUPERSECRETTOKEN with your bot token (keep the quotation marks)  
8. Run bot.py with python

## How to customize bot
* ### Change random text (!text)  
  * Edit the **text.txt** file in **text** directory  

* ### Change random images (!image) 
  * Add or remove images inside **images** directory  
  * Supported file extensions are : **png, jpg, jpeg, gif** 

* ### Customize banned words in chat  
  * Edit **words.txt** file in **ban words** directory

* ### Customize chat system 
1. Find function ```async def chat_with_bot(msg)``` in bot.py
2. Inside function you can find variables like ```greetings``` or ```name_to_react``` and more...    
   ```python
   greetings = ("hi", "hello", "was-sup", "sup")
   name_to_react = ("bot", "robot")
   ```
   
3. Change it to whatever you want  
   ```python
   greetings = ("aloha", "Bonjour", "Hola")
   name_to_react = ("superbot", "bestrobot")
   ```
   
* ### Change bot command prefix (default is !)  
1. Find this line in bot.py

   ```python
   bot = commands.Bot(command_prefix='!', intents=intents, help_command=help_command)
   ```
2. Edit the command_prefix  
   ```python
   bot = commands.Bot(command_prefix='your_command_prefix', intents=intents, help_command=help_command)
   ```

* ### Change name or help of command  
1. Find command in bot.py that you want to change (For example I choose !image)  
   ```python
   @bot.command(name='image', help='Send random image to chat')
   ```

2. Edit the name of command and help of command  
    ```python
    @bot.command(name='your_command_name', help='your_help_message')
    ```
* ### Change messages (embeds) output of commands  
1. Find command that you want to change (For example I choose !text)  
2. After that find function that handle the embed in    
   ```python
   await emb.send_embed(ctx, title=random_text)
   ```
   
3. Finally you can edit the message (Supported arguments for the function are **title, description, color**)
   ```python
   await emb.send_embed(ctx, title=f"Your random text is {random_text}", description="This is a description", color=discord.Color.orange())
   ```
   * Remember that you need to always include argument **ctx**  
   * If you don't write argument description, the description would be empty  
   * Or if you don't write argument color default color will be blue 
   * Argument color can be hex color code like **0xe0ab76** (0xhex_color_code) or discord Class Color like **discord.Color.orange()** (discord.Color.yourcolor()) or color can be None
   
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
