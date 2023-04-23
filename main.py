import telegram.ext 
from telegram.ext import Updater
from telegram.ext import *
# from telegram.ext import *


# Bot name: CK_is_Legen_WaitForIt_DARY


Token = "6146724476:AAF99tbfYU50gMknpDsJEmJaWGSLtNfdyR8"

updater = Updater("6146724476:AAF99tbfYU50gMknpDsJEmJaWGSLtNfdyR8", use_context=True)
# print(type(updater))
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Welcome to OnTips Xerox Printing Bot. Type /help to get help")
    
def help(update, context):
    update.message.reply_text(
    """
    /start - Start the bot
    /help - Help
    /details - Details of Xerox printing
    /upload - Upload files
    /payments - Payments
    /contact - Contact Us
    """
    )
    
def details(update, context):
    update.message.reply_text(
    """Details of Xerox printing
    
    1) Normal A4 - Rs. 2.00/page
    2) Color A4 - Rs. 5.00/page
    3) Glossy A4 - Rs. 10.00/page
    4) Instant prints - Rs. 5.00 additional cost
    """
    )
    
# def upload(update, context):
#     update.message.reply_text()
    
# def payments(update, context):
#     update.message.reply_text()
    
def contact(update, context):
    update.message.reply_text(
    """Contact Us via email or phone
    
    Email: ontips@gmxil.com
    Ph. No.: 9999999999
    """
    )
    
dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("details", details))
# dispatcher.add_handler(telegram.ext.CommandHandler("upload", upload))
# dispatcher.add_handler(telegram.ext.CommandHandler("payments", payments))
dispatcher.add_handler(telegram.ext.CommandHandler("contact", contact))


updater.start_polling()
updater.idle()