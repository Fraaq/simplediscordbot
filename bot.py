from discord.ext import commands
from dotenv import load_dotenv
import random,discord,os


load_dotenv()
TOKEN = os.getenv('TOKEN')  #Load discord token from env file

bot = commands.Bot(command_prefix='!') 
client = discord.Client()

@bot.command(name='image', help='Send random image to chat')    #Command name and help for it 
async def images(ctx):
    script_dir = os.path.abspath(os.path.dirname(__file__))     #Get script directory
    filenames = os.listdir(script_dir + "\images")              #Get all files from images directory
    extensions = ['.png','.jpg','.gif']                         #Allowed file extensions
    images = []

    for i in filenames:                                         #Check if files have supported extensions
        if i.endswith(tuple(extensions)) and i not in images:   
            images.append(i)
  
    random_img = script_dir + "\\images\\" + random.choice(images)     #Choose random image and add path to it     
    await ctx.send(file=discord.File(random_img))                      #Send random image

@bot.command(name='text', help='Send random text')              #Command name and help for it 
async def text(ctx):
    script_dir = os.path.abspath(os.path.dirname(__file__))     #Get script directory
    text_file_path = script_dir + "\\text\\" + "text.txt"       #Get file path
    file = open(text_file_path, 'r')                            

    for line in file.readlines():                               #Split words by comma
        text = line.rstrip().split(',')
   
    file.close()             
    random_text = random.choice(text)                           #Choose random text
    await ctx.send(random_text)                                 #Send random text

@bot.listen('on_message')
async def chat(msg):

    script_dir = os.path.abspath(os.path.dirname(__file__))     #Get script directory
    text_file_path = script_dir + "\\ban words\\" + "words.txt" #Get file path
    file = open(text_file_path, 'r') 
    message = msg.author.mention + " was warned"                #Warn message

    for line in file.readlines():                               #Split words by comma
        words = line.rstrip().split(',')
   
    file.close()             

    for i in words : 
       if i in msg.content:                                     #If ban words is send
            await msg.delete()                                  #Delete the message if contains baned words 
            await msg.channel.send(message)                     #Send warn message
            
bot.run(TOKEN)