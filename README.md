# simplediscordbot
Simple python discord bot. This bot can send random text from txt file or random image from directory and it can delete message if the message contains word that you banned. It can also send and article from wikipedia based on user input. Users can create their own qrcode. And simple chat system (bot can response if someone write his name).

<h1>Features</h1>
1. Random text from file <br>
2. Random images from folder <br>
3. Banned words from txt file <br>
4. Send wikipedia article based on user input <br>
5. Create qr code based on user input<br>
6. Send 3 news<br>
7. Rock Paper and Scissors game<br>
8. Random number in range, based on user input<br>
9. Guess the number game<br>
10. Convert currency to another currency<br>
11. Simple chat system 
 
<h1>How to use it </h1>
1.<a href="https://www.geeksforgeeks.org/how-to-install-pip-on-windows/"> Install pip</a><br>
2.<a href="https://www.geeksforgeeks.org/how-to-install-a-python-module/"> Install modules</a> (pip install -r requirements.txt)<br>
3. Create .env file in main directory and add " DISCORD_TOKEN='YOURSUPERSECRETTOKEN' " replace the YOURSUPERSECRETTOKEN with your <a href="https://www.writebots.com/discord-bot-token/" >bot token</a> <br>
4. Enable <a href="https://autocode.com/discord/threads/what-are-discord-privileged-intents-and-how-do-i-enable-them-tutorial-0c3f9977/">message content intent</a> for bot<br>
5. Customize your <a href="https://github.com/Anonym-Guy/simplediscordbot/blob/main/text/text.txt">own words</a>, <a href="https://github.com/Anonym-Guy/simplediscordbot/tree/main/images">images</a> and <a href="https://github.com/Anonym-Guy/simplediscordbot/tree/main/ban%20words">banned words</a><br>
6. Customize your <a href="https://github.com/Anonym-Guy/simplediscordbot/blob/main/bot.py">bot response name</a> for chat system (change the array "name_to_react" on bottom of the file to what you want)

<h1>Commands</h1>
<b>!text</b> (random text from text.txt file) <br>
<b>!image</b> (random image from images folder) <br>
<b>!whatis</b> (Send wikipedia article based on user input) <br>
<b>!qrcode "what do you want in qrcode"</b> (Send qrcode based on user input) <br>
<b>!news</b> (Send 3 news) <br>
<b>!rpas "you can choice rock,paper,scissors"</b> (Rock Paper and Scissors game) <br>
<b>!random from "your number" to "your number"</b> (Random number) <br>
<b>!gtn</b> (Guess the number game) <br>
<b>!convert</b> (Convert currency to another currency)<br>
