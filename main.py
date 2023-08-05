from typing import Final
from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler, filters

from texttospeech import Text2speech as t2s

TOKEN: Final = '<>'
BOT_USERNAME: Final = '@TSC_0_BOT'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello, there You have started the {BOT_USERNAME}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I transcribe text')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

def send_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc_file = open('out.mp3', "rb")
    chat_id = update.message.chat_id
    return context.bot.send_document(chat_id, doc_file)


def handle_response(text: str) -> str:
    text: str = text.lower()

    # Commands
    if 'hello' in text:
        return 'hello there this is Transcribe Bot'
    if 'how are you' in text:
        return 'I am fine, still in development.....☺️ '

    if 'say' in text:
        proc = text.replace('say', '')
        speak = t2s()
        speak.text_to_speech(proc,save=True)



    return 'Write hello ... BOT still in development...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'USER: {update.message.chat.id} in {message_type}: {text}')

    response: str = handle_response(text)

    print(f'BOT: {response}')
    await update.message.reply_text(response)


# Error handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update : {update} caused : {context.error}')


# main
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    print('Starting BOT.....')
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler("send", send_document))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling started.....')
    app.run_polling(poll_interval=3)

