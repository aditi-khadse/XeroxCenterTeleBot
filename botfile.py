import telegram.ext 
from telegram.ext import Updater
from telegram.ext import *
# from telegram.ext import *


# Bot name: CK_is_Legen_WaitForIt_DARY


Token = "6230085595:AAFvFhnVxy8UFtzB503RhZKXsvbTxJ1Ahpc"

updater = Updater("6230085595:AAFvFhnVxy8UFtzB503RhZKXsvbTxJ1Ahpc", use_context=True)
# print(type(updater))
disp = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to Xerox Corner. Here, you can view our inventory and place orders. Type /help to see the available commands.")
    
def help(update,context):
    update.message.reply_text("""
    Here are the available commands:
    \n/inventory - View the store's inventory
    \n/order - Place an order
    \n/contact - Contact information
     """)
    
def inventory(update, context):
    update.message.reply_text('''
    Here is our inventory:
    \nPrint type - 
    1) Black and white print (2/- per page)
    2) Color print (5/- per page)
    3) Glossy Paper print (10/- per page)
    \nSide type-
    1) One side (2/- per page)
    2) Both sides (1.5/- per page)
    \nCompile by -
    1) Stapler (free)
    2) Punching Machine (free)
    3) Spiral Binding (20/- per bind)
    ''')

def order(update, context):
        update.message.reply_text('''
        Place your order by filling this google form: https://forms.gle/jJZLdnSesxgNJQSm9''')

def contact(update, context):
    update.message.reply_text("You can contact on the official mail id:abc@gmail.com \nWhatsapp us on: 9999999999")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('inventory',inventory))
disp.add_handler(telegram.ext.CommandHandler('order',order))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()