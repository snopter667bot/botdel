from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, CommandHandler, ApplicationBuilder, MessageHandler, ConversationHandler, filters, CallbackContext, CallbackQueryHandler

TOKEN = "7585954539:AAFq7Q8Pt64u6mYXRfv7mOxDeyE4ZzFb3Ik"
application = ApplicationBuilder().token(TOKEN).build()

async def hello(update:Update, context:ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        [("Hola"), ("Hola")],
        ["Adios"]
    ])
    await update.message.reply_text("Tecla enviado", reply_markup=keyboard)
    
async def saludar_despedir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Hola":
        await update.message.reply_text("Cómo estas?", reply_markup=ReplyKeyboardRemove())
    if update.message.text == "Adios":
        await update.message.reply_photo("https://es.onlynude.men/wp-content/galeries/sites/5/Tim-Parise-00003-364x499.jpg", reply_markup=ReplyKeyboardRemove())
    pass

application.add_handler(CommandHandler("start", hello))
application.add_handler(MessageHandler(filters.ALL, saludar_despedir))
application.run_polling(allowed_updates=Update.ALL_TYPES)