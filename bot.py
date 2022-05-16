from discord.ext import commands
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates
from datetime import datetime 
import random,discord,os,wikipedia,qrcode,requests,time


load_dotenv()
TOKEN = os.getenv('TOKEN')                                      #Load discord token from env file

help_command = commands.DefaultHelpCommand(                     # Change the no category to commands
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix='!', help_command=help_command) 
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


@bot.command(name='whatis', help='Send wikipedia article about topic you wrote')    #Command name and help for it 
async def whatis(ctx,*args):
    try :
        data = " " .join(args)                                                      #Try if article exist                                                                        
        article = wikipedia.summary(data, sentences = 2)                            #Words separeted by space 
        await ctx.send(article)                                                     #Send wikipedia article                                                
   
    except:                                                                         #If article doesn't exist or if exist more articles than 1
        data = " " .join(args)                                                      #Words separeted by space                                                                  
        article = wikipedia.search(data, results = 5)                               #Search for articles
        
        if len(article) > 0 :                                                       #If something found
            result = str(article)[1:-1]                                             #Convert to string
            result = result.replace("'", "")                                        #Add , between results
            await ctx.send(f"{data} can be : {result}")                             #Send results
        else :                                                                      #If didn't found
            await ctx.send("The article isn't existing or you wrote it wrong") 

@bot.command(name='qrcode', help="Make your own qrcode | !qrcode 'what you want in qrcode' ")    #Command name and help for it 
async def qr(ctx,*args):
    script_dir = os.path.abspath(os.path.dirname(__file__))        #Get script directory
    data = " " .join(args)                                         #Words separeted by space
    img = qrcode.make(data)                                        #Make qr code
    
    filepath = script_dir + "\\qr.png"
    img.save(filepath)                                             #Save qr code 
    
    
    await ctx.send(file=discord.File(filepath))                    #Send qr code
    os.remove(script_dir + "\\qr.png")                             #Delete the qr code to save space on device

@bot.command(name='news', help="Send top 3 news")                  #Command name and help for it 
async def qr(ctx):
    url = 'https://www.bbc.com/news'                               #URL for news
    response = requests.get(url)                                   

    soup = BeautifulSoup(response.text, 'html.parser')

    links = []

    for a in soup.select("[class~=gs-c-promo-heading]",href=True):
        links.append("https://www.bbc.com"+ a['href'])              #Add links to news article

    await ctx.send(f"{links[1]}\n{links[2]}\n{links[13]}\n")        #Send 3 news 

@bot.command(name='rpas', help="Rock Paper and Scissors game | !rpas 'your choice'")      #Command name and help for it 
async def game(ctx,arg):
   
    choices = ["rock", "paper", "scissors"]

    bot_choice = random.choice(choices)                             

    player_choice = arg                                               

    if player_choice in choices :                                   #If player writes correctly choice
        if bot_choice == player_choice :
            await ctx.send(f"Tie, you both selected {bot_choice}")

        elif bot_choice == "rock" and player_choice == "paper":
            await ctx.send(f"You win, bot selected {bot_choice}\nCongratulations :tada:")

        elif bot_choice == "rock" and player_choice == "scissors":
            await ctx.send(f"Bot win, bot selected {bot_choice}")

        elif bot_choice == "paper" and player_choice == "rock":
            await ctx.send(f"Bot win, bot selected {bot_choice}")

        elif bot_choice == "paper" and player_choice == "scissors":
            await ctx.send(f"You win, bot selected {bot_choice}\nCongratulations :tada:")

        elif bot_choice == "scissors" and player_choice == "rock":
            await ctx.send(f"You win, bot selected {bot_choice}\nCongratulations :tada:")

        elif bot_choice == "scissors" and player_choice == "paper":
            await ctx.send(f"Bot win, bot selected {bot_choice}")
    
    elif player_choice not in choices:                                 #If player writes something else 
        await ctx.send(f"Write please !rpas (rock,paper,scissors)")

@bot.command(name='random', help="Send random number | !random from 'number' to 'number' ")    #Command name and help for it
async def rnd(ctx,*arg):
    try :                                                                   
        if arg[0] == "from" and arg[2] == "to" :                            #IF user wrote it in correct format
            num1 = int(arg[1])                                              #User number1 to int
            num2 = int(arg[3])                                              #User number2 to int
            random_num = random.randrange(num1,num2 + 1)                    #Random number (number2 + 1 is for the maximum number entered by the user to be sent as well)
            await ctx.send(random_num)
        else:
            await ctx.send("Write please : !random from 'your number' to 'your number'")
    except:                                                                             
        await ctx.send("Write please : !random from 'your number' to 'your number'")

@bot.command(name='gtn', help = 'Guess the number game')        #Command name and help for it
async def guess_the_number(ctx):
    await ctx.send("Guess the number between 1 - 100")
    random_number = random.randrange(1,101)                     #Random number between 1 - 100
    win = False                                                 
    attempts = 1                                        

    while win == False :                                        
        try :                                                                                           
            msg = await bot.wait_for('message',timeout = 15,check=lambda m: m.author == ctx.author)      #Get input of user time to write is 15s
            user_guess = int(msg.content)                                                                #User input to int
            if user_guess == random_number :                                                             #If user guessed the number
                await ctx.send(f"Congratulations you guessed the number on {attempts} try :tada:")
                win = True
                break
            elif user_guess > random_number :                                                            #If user number is lower than the number
                await ctx.send("The number is lower")
                attempts = attempts + 1
                continue

            elif user_guess < random_number :                                                            #If user number is higher than the number
                await ctx.send("The number is higher")
                attempts = attempts + 1
                continue
            
        except ValueError :                                     #If user input something else than number
            await ctx.send("Write please number")
            continue

        except :                                                #If time is up
            await ctx.send("Time is up !")
            break


@bot.command(name='convert', help='Convert currency to another currency')
async def conventor(ctx):
    await ctx.send("Enter the amount to convert :")
    
    c = CurrencyRates()
   
    try :
        amount = await bot.wait_for('message',timeout = 30,check=lambda m: m.author == ctx.author)      #Get input of user time to write is 30s
        await ctx.send("Enter the currency from which you want to convert :")
        from_currency = await bot.wait_for('message',timeout = 30,check=lambda m: m.author == ctx.author)      #Get input of user time to write is 30s
    
        await ctx.send("Enter the currency that you want converted :")
        to_currency = await bot.wait_for('message',timeout = 30,check=lambda m: m.author == ctx.author)      #Get input of user time to write is 30s


        convert = c.convert(from_currency.content.upper(), to_currency.content.upper(), float(amount.content))     #Convert user input
    
        result = round(convert,2)                                                                                 #Specified number of decimals

        await ctx.send(f"{result} {to_currency.content.upper()}")                                                  
        
    except ValueError :
        await ctx.send("You entered something wrong")
        
    except :
        pass

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

@bot.listen('on_message')
async def chat(msg):
    greetings = ["hi","hello","wassup","sup"]

    name_to_react = ["bot","robot"]                  #If user write for example "hi bot" or "hi robot" than bot will reply 
                                                     #But if user didn't write name_to_react bot will not reply
    random_greeting = random.choice(greetings)

    if any(x in msg.content for x in greetings) and any(x in msg.content for x in name_to_react):       #IF user write for example "hello bot"
        random_greeting_upper = random_greeting[0].upper() + random_greeting[1:]
        await msg.channel.send(f"{random_greeting_upper} {msg.author.name} :wave:")

    if any(x in msg.content for x in name_to_react) and any(x in msg.content for x in ["how are you","how's it going","what's up","how are you doing","how was your day"]): #If user write for example "what's up bot"
        await msg.channel.send(f"I am good, and you ?")
        response = await bot.wait_for('message',timeout = 30,check=lambda m: m.author == msg.author)    #Wait for user message how he is going
        
        if response.content in ["bad","not good"] :                                                     #If he's not doing well
            await msg.channel.send(f"Oh, I'm sorry about that :confused:")
        elif response.content in ["good","well","very good","okay","really good"] :                     #If he's doing well
            await msg.channel.send(f"I'm glad to hear that :relaxed:")
    
    if any(x in msg.content for x in name_to_react) and any(x in msg.content for x in ["how old are you","what is your age"]):      #If user ask how old are you bot
        bot_created = [2022,5,7]                                                                                                    #When was bot created
        date = datetime.utcnow()                                                                                                    #Current date
        date_to_subtract = [date.year,date.month,date.day]
        age = [date_to_subtract[0] - bot_created[0],date_to_subtract[1] - bot_created[1] ,date_to_subtract[2] - bot_created[2]]                 #Age of bot
        
        await msg.channel.send(f"I was created in 2022-05-08\nSo i'm technically {age[0]} years {age[1]} months {age[2]} days old :smile:")



bot.run(TOKEN)