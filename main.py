from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["خيار 1", "خيار 2"],  # صف يحتوي على زرين
        ["خيار 3"]  # صف يحتوي على زر واحد
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('اختر من القائمة:', reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token('7865424971:AAF_Oe6lu8ZYAl5XIF1M6qU_8MK6GHWEll8').build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()

if __name__ == "__main__":
    main()
