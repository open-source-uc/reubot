import os, dotenv
import telebot
import bot_commands

dotenv.load_dotenv('./.env')
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)
DOCUMENTATION_URL = "shorturl.at/tCFNX"

@bot.message_handler(commands=['checkout'])
def checkout(message):
    list_name = message.text.replace("/checkout ", "")
    bot.reply_to(message, bot_commands.set_current_list(list_name))


@bot.message_handler(commands=['create'])
def create(message):
    try:
        list_name = message.text.replace("/create ", "")
        bot.reply_to(message, bot_commands.create_list(list_name))
    except:
        bot.reply_to(message, "Something went wrong. Please try again")

@bot.message_handler(commands=['delete'])
def delete(message):
    list_name = message.text.replace("/delete ", "")
    bot.reply_to(message, bot_commands.delete_list(list_name))
    bot_commands.set_current_list("")


@bot.message_handler(commands=['add_bullet'])
def add_bullet(message):
    CURRENT_LIST = bot_commands.get_current_list()
    if CURRENT_LIST != None:
        try:
            params = message.text.replace("/add_bullet ", "").split(", ")
            print(params)
            if len(params) == 1:
                description = params[0]
                bot.reply_to(message, bot_commands.add_bullet(CURRENT_LIST, description))
            else:
                description, checked = params
                bot.reply_to(message, bot_commands.add_bullet(CURRENT_LIST, description, checked))

            bot.send_message(message.chat.id, bot_commands.print_list(CURRENT_LIST))
        except:
            bot.reply_to(message, "Command parameters must be separated by ', '")
    else:
        bot.reply_to(message, "There is no list selected")


@bot.message_handler(commands=['delete_bullet'])
def delete_bullet(message):
    CURRENT_LIST = bot_commands.get_current_list()
    if CURRENT_LIST != None:
        try:
            bullet_id = message.text.replace("/delete_bullet ","")
            bot.reply_to(message, bot_commands.delete_bullet(CURRENT_LIST, bullet_id))
            bot.send_message(message.chat.id, bot_commands.print_list(CURRENT_LIST))
        except:
            bot.reply_to(message, "Command parameters must be separated by ', '")
    else:
        bot.reply_to(message, "There is no list selected")


@bot.message_handler(commands=['check'])
def check_bullet(message):
    CURRENT_LIST = bot_commands.get_current_list()
    if CURRENT_LIST != None:
        try:
            bullet_id = message.text.replace("/check ","")
            bot.reply_to(message, bot_commands.checked(CURRENT_LIST, bullet_id, True))
            bot.send_message(message.chat.id, bot_commands.print_list(CURRENT_LIST))
        except:
            bot.reply_to(message, "Command parameters must be separated by ', '")
    else:
        bot.reply_to(message, "There is no list selected")


@bot.message_handler(commands=['uncheck'])
def uncheck_bullet(message):
    CURRENT_LIST = bot_commands.get_current_list()
    if CURRENT_LIST != None:
        try:
            bullet_id = message.text.replace("/uncheck ","")
            bot.reply_to(message, bot_commands.checked(CURRENT_LIST, bullet_id, False))
            bot.send_message(message.chat.id, bot_commands.print_list(CURRENT_LIST))
        except:
            bot.reply_to(message, "Command parameters must be separated by ', '")
    else:
        bot.reply_to(message, "There is no list selected")


@bot.message_handler(commands=['update'])
def update_bullet(message):
    CURRENT_LIST = bot_commands.get_current_list()
    if CURRENT_LIST != None:
        try:
            params = message.text.replace("/update ","").split(", ")
            bullet_id, description = params
            bot.reply_to(message, bot_commands.update_bullet(CURRENT_LIST, bullet_id, description))
            bot.send_message(message.chat.id, bot_commands.print_list(CURRENT_LIST))
        except:
            bot.reply_to(message, "Command parameters must be separated by ', '")
    else:
        bot.reply_to(message, "There is no list selected")



@bot.message_handler(commands=['view'])
def view(message):
    list_name = message.text.replace("/view ","")
    bot.send_message(message.chat.id, bot_commands.print_list(list_name))

@bot.message_handler(commands=["view_lists"])
def view_all_lists(message):
    bot.send_message(message.chat.id, bot_commands.view_all_lists())

@bot.message_handler(commands=["help"])
def get_help(message):
    bot.send_message(message.chat.id, f"Link documentación: { DOCUMENTATION_URL }")

bot.polling()

