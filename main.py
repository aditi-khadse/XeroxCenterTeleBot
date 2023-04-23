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
    update.message.reply_text("Hello! Welcome to Xerox Corner. Here, you can view our inventory and place orders. Type /help to see the available commands.")
    
def help(update,context):
    update.message.reply_text("""
    Here are the available commands:
    \n/inventory - View the store's inventory
    \n/order - Place an order
    \n/upload -
    \n/contact - Contact information
     """)
    
def inventory(update, context):
    update.message.reply_text('''/
    Here is our inventory:
    Print type - 
    1) Black and white print
    2) Color print
    \nPage type-
    1) One side
    2) Both sides
    \nCompile by-
    1) Stapler
    2) Punching Machine
    3) Spiral Binding
    ''')

def upload(update, context):
        update.message.reply_text('''
        Upload your files by filling this form: https://forms.gle/jJZLdnSesxgNJQSm9''')
                                  
def order(update, context):
        update.message.reply_text('''
        Enter your order details as follows:
        \nPrint Type
        \nPage Type
        \nCompile by
        \n
        \nExample: Black and white, one side, punching machine
        ''')

def contact(update, context):
    update.message.reply_text("You can contact on the official mail id: \nWhatsapp us on:")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('inventory',inventory))
disp.add_handler(telegram.ext.CommandHandler('order',order))
disp.add_handler(telegram.ext.CommandHandler('upload',upload))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()


updater.start_polling()
updater.idle()
