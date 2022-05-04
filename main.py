import logging
from traceback import format_tb
from telegram.ext import *
import responses

###API KEY - BotFather Telegram ####
API_KEY = '###' #Agregar API KEY

#Login

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

# Declaracion de comandos

def start_command(update, context):
    update.message.reply_text('Hola humano! Estas hablando con la maxima deidad Maya')

def help_command(update, context):
    update.message.reply_text('Intenta preguntar algo, ya vere si eres digno de una respuesta')

def custom_command(update, context):
    update.message.reply_text('Comando custom, en proceso')

#Respuesta a mensajes del usuario

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    #Bot Response
    update.message.reply_text(text)

#Respuesta ante error

def error(update, context):
    logging.error(f'Update {update} cause error {context.error}')

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    #Comandos
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    #Mensajes
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    #Log de errores
    dp.add_error_handler(error)

    #Iniciar bot
    updater.start_polling(1.0)
    updater.idle()