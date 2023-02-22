from discord.ext import commands
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

import embed as emb

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
    all_files = os.listdir(f"{script_directory}/images")
    allowed_extensions = ('.png', '.jpg', '.jpeg', '.gif')

    # All available images with supported extensions
    all_images = [file for file in all_files if
                  file.endswith(allowed_extensions)]

    # Choose random image and add path to it
    random_image = f"{script_directory}/images/{random.choice(all_images)}"

    await ctx.send(file=discord.File(random_image))


# Command to send random text from file text.txt in text directory

@bot.command(name='text', help='Send random text')
async def send_random_text(ctx):
    text_file_path = f"{script_directory}/text/text.txt"

    with open(text_file_path) as file:
        lines = [line for line in file.read().splitlines()]

    # Split text inside line list
    lines_with_split_text = [line.split(",") for line in lines]

    # Choose from random line random text
    random_line = random.choice(lines_with_split_text)
    random_text = random.choice(random_line)

    await emb.send_embed(ctx, title=random_text)


# Command to send wikipedia article based on the user input

@bot.command(name='whatis', help='Send wikipedia article about topic you write')
async def whatis(ctx, *args: str):
    if args:
        data = " ".join(args)

        # Try if article exist
        try:
            article = wikipedia.summary(data, sentences=2)
            await emb.send_embed(ctx, title=data.title(), description=article)

        # If article doesn't exist or if exist more articles than 1
        except (wikipedia.PageError, wikipedia.DisambiguationError):
            articles = wikipedia.search(data, results=5)

            # If something found
            if articles:
                articles = ", ".join(articles)
                await emb.send_embed(ctx, title=f'{data.title()} can be : ', description=articles)

            # If article doesn't exist
            else:
                await emb.send_embed(ctx, title="The article doesn't exist", color=0xFF0000)

    else:
        await emb.send_embed(ctx, title="Please enter a topic to search for", color=0xFF0000)


# Command to make qrcode based on the user input
@bot.command(name='qrcode', help="Make your own qrcode | !qrcode 'what you want in qrcode' ")
async def make_qrcode(ctx, *, data: str = None):
    if data:
        qr_code = qr_make(data)  # Make qrcode

        qr_filepath = f"{script_directory}/qr.png"  # Where to save qrcode
        qr_code.save(qr_filepath)  # Save qrcode

        await ctx.send(file=discord.File(qr_filepath))
        os.remove(qr_filepath)  # Delete the qrcode to save space on device

    else:
        await emb.send_embed(ctx, title='Please write !qrcode "what do you want in qrcode"', color=0xFF0000)


# Command to send news from www.bbc.com

@bot.command(name='news', help="Send top 3 news")
async def send_three_news(ctx):
    url = 'http://www.bbc.com'

    url_to_news = f'{url}/news/world/'
    response = request(url_to_news)

    soup = BeautifulSoup(response.text, 'html.parser')
    get_promo_news = soup.select("[class~=gs-c-promo-heading]", href=True)
    links = []

    # Add only 3 news to list links with full url
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
async def rpas_game(ctx, player_choice: str = None):
    if player_choice:
        choices = ("rock", "paper", "scissors")
        bot_choice = random.choice(choices)

        if player_choice in choices:

            # If tie
            if bot_choice == player_choice:
                await emb.send_embed(ctx, title="Tie", description=f"You both choose {bot_choice}", color=0x808080)

            # If player win
            elif bot_choice == "rock" and player_choice == "paper" or \
                    bot_choice == "scissors" and player_choice == "rock" or \
                    bot_choice == "paper" and player_choice == "scissors":

                await emb.send_embed(ctx,
                                     title="You win :tada:",
                                     description=f"Bot choose {bot_choice}",
                                     color=0x00ff00)

            # If bot win
            elif bot_choice == "rock" and player_choice == "scissors" or \
                    bot_choice == "paper" and player_choice == "rock" or \
                    bot_choice == "scissors" and player_choice == "paper":

                await emb.send_embed(ctx, title="Bot win", description=f"Bot choose {bot_choice}", color=0xb41b1b)

        else:
            await emb.send_embed(ctx, title="Please choose only rock, scissors or paper", color=0xFF0000)

    else:
        await emb.send_embed(ctx, title="Please write !rpas 'your choice'", color=0xFF0000)


# Command to send random number in user defined range

@bot.command(name='random', help="Send random number | !random from 'number' to 'number' ")
async def choose_random_number(ctx, *arg):
    if arg:
        try:
            # User numbers to integers
            start_number, end_number = int(arg[1]), int(arg[3])

            # If user write command in correct format
            if arg[0] == "from" and arg[2] == "to" and start_number < end_number:
                random_number = random.randrange(start_number, end_number + 1)

                await emb.send_embed(ctx, title=f'Your random number is {random_number}')

            elif start_number >= end_number:
                await emb.send_embed(ctx, title="The first number should be smaller than the second", color=0xFF0000)

            else:
                await emb.send_embed(ctx, title='Write please : !random from "your number" to "your number"',
                                     color=0xFF0000)

        except ValueError:
            await emb.send_embed(ctx, title="Write numbers please", color=0xFF0000)

        except IndexError as e:
            if str(e) == "tuple index out of range":
                await emb.send_embed(ctx, title='Write please : !random from "your number" to "your number"',
                                     color=0xFF0000)

    else:
        await emb.send_embed(ctx, title='Write please : !random from "your number" to "your number"',
                             color=0xFF0000)


# Command to guess the number game

@bot.command(name='gtn', help='Guess the number game')
async def guess_the_number(ctx):
    await emb.send_embed(ctx, title="Guess the number between 1 - 100",
                         description='Write the number in the chat. If you want to exit type "exit"')

    random_number = random.randrange(1, 101)
    win = False
    attempts = 1

    while not win:
        try:
            # Wait for user number guess message
            message = await bot.wait_for('message', timeout=15,
                                         check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            # If user wants to exit the game
            if message.content == "exit":
                await emb.send_embed(ctx, title="Thank you for playing")
                break

            # User input to int
            user_guess = int(message.content)

            if user_guess == random_number:
                win = True

                await emb.send_embed(ctx,
                                     title="Congratulations",
                                     description=f"You guessed the number on {attempts} try :tada:",
                                     color=0x00ff00)
                break

            elif user_guess > random_number:
                attempts += 1
                await emb.send_embed(ctx, title="The number is lower")
                continue

            elif user_guess < random_number:
                attempts += 1
                await emb.send_embed(ctx, title='The number is higher')
                continue

        # If user input something else than number
        except ValueError:
            await emb.send_embed(ctx, title='Write number please', color=0xFF0000)
            continue

        # If time is up
        except TimeoutError:
            await emb.send_embed(ctx, title='Time is up !', color=0xFF0000)
            break


# Command to convert currency to another currency based on the user input

@bot.command(name='convert', help='Convert currency to another currency | !convert from currency to currency amount')
async def convert_currency(ctx, from_currency: str = None, to_currency: str = None, amount: str = None):
    try:
        if from_currency and to_currency and amount:

            # Change user input to upper case
            from_currency, to_currency = from_currency.upper(), to_currency.upper()

            amount = float(amount)

            currency_rates = CurrencyRates()

            # Convert user input
            convert_result = currency_rates.convert(from_currency, to_currency, amount)

            # Specified number of decimals
            result = round(convert_result, 2)

            await emb.send_embed(ctx, title=f"{amount} {from_currency} = {result} {to_currency}")

        else:
            await emb.send_embed(ctx, title='Please write !convert "from currency" "to currency" "amount"',
                                 color=0xFF0000)

    except ValueError:
        await emb.send_embed(ctx, title='You entered wrong amount to convert', color=0xFF0000)

    except RatesNotAvailableError:
        await emb.send_embed(ctx, title='You entered bad currency, or currency is not supported', color=0xFF0000)


# Listen for banned words from the file words.txt in ban words directory

@bot.listen('on_message')
async def check_for_banned_words(msg):
    message_content = msg.content.casefold()

    words_file_path = f"{script_directory}/ban words/words.txt"
    warn_message = f"{msg.author.mention} was warned"

    # Get banned words from words.txt
    with open(words_file_path) as file:
        banned_words_lines = [line for line in file.read().splitlines()]

    # Split words with , and add them in one list
    banned_words = [line.split(",") for line in banned_words_lines]
    banned_words = [word for lines in banned_words for word in lines]

    user_banned_message = [word for word in banned_words if word in message_content]

    # If user sent bad word
    if any(user_banned_message):
        await msg.channel.send(warn_message) and await msg.delete()


# Listen for interactions with bot and response

@bot.listen('on_message')
async def chat_with_bot(msg):
    message_content = msg.content.casefold()

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
        response = await bot.wait_for('message', timeout=30,
                                      check=lambda m: m.author == msg.author and m.channel.id == msg.channel.id)

        if response.content in user_bad_mood_msg:
            await msg.channel.send(
                f"Oh, I'm sorry about that :confused:\n"
                f"If you want, you can play games with me type !help for more information :blush:")

        elif response.content in user_good_mood_msg:
            await msg.channel.send(f"I'm glad to hear that :relaxed:")

    # If user asks how old is bot
    if any(user_name_to_react_msg) and any(user_how_old_msg):
        bot_created = datetime(year=2022, month=8, day=5)
        current_date = datetime.utcnow()
        bot_created, current_date = bot_created.date(), current_date.date()
        age = relativedelta.relativedelta(current_date, bot_created)

        await msg.channel.send(
            f"I was created in {bot_created}\nSo i'm technically {age.years} years {age.months} months "
            f"{age.days} days old :smile:")


# If command not found

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await emb.send_embed(ctx,
                             title="Command not found !",
                             description="If you want to check all available commands write !help.",
                             color=0xFF0000)


# Run bot

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
