from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from datetime import datetime
from dateutil import relativedelta
from requests import get as request
from qrcode import make as qr_make
import random
import discord
import os
import wikipedia

# Load discord token (API) from env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Change the !help from no category to commands
help_command = commands.DefaultHelpCommand(
    no_category='Commands'
)

# Load intents
intents = discord.Intents.default()
intents.message_content = True

# Define discord bot and discord client
bot = commands.Bot(command_prefix='!', intents=intents, help_command=help_command)

# Variables
script_directory = os.path.abspath(os.path.dirname(__file__))  # Get script directory


# Command to send random image from images directory

@bot.command(name='image', help='Send random image to chat')
async def images(ctx):
    all_files = os.listdir(script_directory + "/images")  # Get all files from images directory
    allowed_extensions = ('.png', '.jpg', '.jpeg', '.gif')

    images = [file for file in all_files if
              file.endswith(allowed_extensions)]  # All available images with supported extensions

    random_image = f"{script_directory}/images/{random.choice(images)}"  # Choose random image and add path to it

    await ctx.send(file=discord.File(random_image))


# Command to send random text from file text.txt in text directory

@bot.command(name='text', help='Send random text')
async def text(ctx):
    text_file_path = f"{script_directory}/text/text.txt"  # Get file path

    with open(text_file_path) as file:
        for line in file.readlines():
            text = line.rstrip().split(',')  # Split words by comma

    random_text = random.choice(text)  # Choose random text
    await ctx.send(random_text)


# Command to send wikipedia article based on the user input

@bot.command(name='whatis', help='Send wikipedia article about topic you write')
async def whatis(ctx, *args: str):
    if len(args) == 0:
        await ctx.send("Please enter a topic to search for")

    else:
        data = " ".join(args)
        
        # Try if article exist
        try:  
            article = wikipedia.summary(data, sentences=2)
            await ctx.send(article)

        # If article doesn't exist or if exist more articles than 1
        except (wikipedia.PageError,
                wikipedia.DisambiguationError):  
            articles = wikipedia.search(data, results=5)

            # If something found
            if len(articles) > 0:  
                articles = ", ".join(articles)
                await ctx.send(f"{data} can be : {articles}")

            # If article doesn't exist
            else:
                await ctx.send("The article isn't exist or you wrote it wrong")


# Command to make qrcode based on the user input

@bot.command(name='qrcode', help="Make your own qrcode | !qrcode 'what you want in qrcode' ")
async def qr(ctx, *, data: str = None):
    if data:
        qr_code = qr_make(data)  # Make qrcode

        qr_filepath = f"{script_directory}/qr.png"  # Where to save qrcode
        qr_code.save(qr_filepath)  # Save qrcode

        await ctx.send(file=discord.File(qr_filepath))
        os.remove(qr_filepath)  # Delete the qrcode to save space on device

    elif not data:
        await ctx.send('Please write !qrcode "what do you want in qrcode"')


# Command to send news from www.bbc.com

@bot.command(name='news', help="Send top 3 news")
async def qr(ctx):
    url = 'http://www.bbc.com'

    url_to_news = f'{url}/news/world/'
    response = request(url_to_news)

    soup = BeautifulSoup(response.text, 'html.parser')
    get_promo_news = soup.select("[class~=gs-c-promo-heading]", href=True)
    links = []

    # Add only 3 news to links list with full url
    for counter, news in enumerate(get_promo_news):
        news_url = f'{url}{news["href"]}'

        if news_url not in links and counter <= 3:
            links.append(news_url)

        elif counter > 3:
            break

    links = "\n".join(links)
    await ctx.send(f"{links}")


# Command to rock, paper and scissors game

@bot.command(name='rpas', help="Rock Paper and Scissors game | !rpas 'your choice'")
async def game(ctx, player_choice: str = None):
    if not player_choice:
        await ctx.send(f"Please write !rpas 'your choice'")

    elif player_choice:
        choices = ("rock", "paper", "scissors")
        bot_choice = random.choice(choices)

        if player_choice in choices:

            # If tie
            if bot_choice == player_choice:
                await ctx.send(f"Tie, you both choose {bot_choice}")

            # If player win
            elif bot_choice == "rock" and player_choice == "paper" or \
                    bot_choice == "scissors" and player_choice == "rock" or \
                    bot_choice == "paper" and player_choice == "scissors":

                await ctx.send(f"You win, bot choose {bot_choice}\nCongratulations :tada:")

            # If bot win
            elif bot_choice == "rock" and player_choice == "scissors" or \
                    bot_choice == "paper" and player_choice == "rock" or \
                    bot_choice == "scissors" and player_choice == "paper":

                await ctx.send(f"Bot win, bot choose {bot_choice}")

        elif player_choice not in choices:
            await ctx.send(f"Write please !rpas (rock, paper, scissors)")


# Command to send random number in user defined range

@bot.command(name='random', help="Send random number | !random from 'number' to 'number' ")
async def rnd(ctx, *arg):
    try:
        # If user write command in correct format
        if arg and arg[0] == "from" and arg[2] == "to":
            # User numbers to integers
            start_number, end_number = int(arg[1]), int(arg[3])

            random_number = random.randrange(start_number, end_number + 1)

            await ctx.send(f"Random number is : {random_number}")

        else:
            await ctx.send("Write please : !random from 'your number' to 'your number'")

    except ValueError:
        await ctx.send("Write numbers please")


# Command to guess the number game

@bot.command(name='gtn', help='Guess the number game')
async def guess_the_number(ctx):
    await ctx.send("Guess the number between 1 - 100")

    random_number = random.randrange(1, 101)
    win = False
    attempts = 1

    while not win:
        try:
            # Wait for user number guess message
            message = await bot.wait_for('message', timeout=15,
                                         check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            # User input to int
            user_guess = int(message.content)

            if user_guess == random_number:
                win = True
                await ctx.send(f"Congratulations, you guessed the number on {attempts} try :tada:")
                break

            elif user_guess > random_number:
                attempts += 1
                await ctx.send("The number is lower")
                continue

            elif user_guess < random_number:
                attempts += 1
                await ctx.send("The number is higher")
                continue

        # If user input something else than number
        except ValueError:
            await ctx.send("Write number please")
            continue

        # If time is up
        except TimeoutError:
            await ctx.send("Time is up !")
            break


# Command to convert currency to another currency based on the user input

@bot.command(name='convert', help='Convert currency to another currency | !convert from currency to currency amount')
async def convertor(ctx, from_currency: str = None, to_currency: str = None, amount: str = None):
    try:

        if not from_currency or not to_currency or not amount:
            await ctx.send('Please write !convert "from currency" "to currency" "amount"')

        elif from_currency and to_currency and amount:

            # Change user input to upper case
            from_currency, to_currency = from_currency.upper(), to_currency.upper()

            amount = float(amount)

            currency_rates = CurrencyRates()

            # Convert user input
            convert_result = currency_rates.convert(from_currency, to_currency, amount)

            # Specified number of decimals
            result = round(convert_result, 2)

            await ctx.send(f"{amount} {from_currency} = {result} {to_currency}")

    except ValueError:
        await ctx.send("You entered wrong amount to convert")

    except RatesNotAvailableError:
        await ctx.send("You entered bad currency, or currency is not supported")


# Listen for banned messages from the file words.txt in ban words directory

@bot.listen('on_message')
async def chat(msg):
    message_content = msg.content.lower()

    text_file_path = f"{script_directory}/ban words/words.txt"  # Get file path
    warn_message = msg.author.mention + " was warned"

    with open(text_file_path) as file:
        banned_words = [line for line in file.readline().split(',')]  # Get banned words from words.txt

    user_bad_words = [word for word in banned_words if word in message_content]

    if any(user_bad_words):  # If user sent bad word
        await msg.channel.send(
            warn_message) and await msg.delete()  # Send warn message and delete the message that contains banned words


# Listen for interactions with bot and response

@bot.listen('on_message')
async def chat(msg):
    message_content = msg.content.lower()

    # All possible chat interactions variables
    greetings = ("hi", "hello", "was-sup", "sup")
    name_to_react = ("bot", "robot")
    how_are_you_react = ("how are you", "how's it going", "what's up", "how are you doing", "how was your day")
    how_old_are_you_react = ("how old are you", "what is your age")

    user_greeting_msg = [greeting in message_content for greeting in greetings]
    user_name_to_react_msg = [name in message_content for name in name_to_react]
    user_how_are_you_react_msg = [x in message_content for x in how_are_you_react]
    user_how_old_msg = [x in message_content for x in how_old_are_you_react]
    user_bad_mood_msg = ("bad", "not good")
    user_good_mood_msg = ("good", "well", "very good", "okay", "really good")

    random_greeting = random.choice(greetings)
    random_greeting = random_greeting.title()

    # If the user greets the bot
    if any(user_greeting_msg) and any(user_name_to_react_msg):
        await msg.channel.send(f"{random_greeting} {msg.author.name} :wave:")

    # If the user asks how the bot is doing
    if any(name_to_react) and any(user_how_are_you_react_msg):
        await msg.channel.send(f"I am good, and you ?")

        # Wait for user message how he is doing
        response = await bot.wait_for('message', timeout=30, check=lambda m: m.author == msg.author)

        if response.content in user_bad_mood_msg:
            await msg.channel.send(
                f"Oh, I'm sorry about that :confused:\n"
                f"If you want, you can play games with me type !help for more information :blush:"
            )

        elif response.content in user_good_mood_msg:
            await msg.channel.send(f"I'm glad to hear that :relaxed:")

    # If user asks how old is bot
    if any(user_name_to_react_msg) and any(user_how_old_msg):
        bot_created = datetime(2022, 8, 5)
        current_date = datetime.utcnow()
        bot_created, current_date = bot_created.date(), current_date.date()
        age = relativedelta.relativedelta(current_date, bot_created)

        await msg.channel.send(
            f"I was created in 2022-05-08\n"
            f"So i'm technically {age.years} years {age.months} months {age.days} days old :smile:"
            )


# If command not found

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found !\nIf you want to check all available commands write !help.")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
