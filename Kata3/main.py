from telegram.ext import Updater , CommandHandler

def main():
    # Instanciamos el updater
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    #añade manejador al comando /start

    updater.dispatcher.add_handler(CommandHandler("start",start))
    
    #añade manejador al comando /repite

    updater.dispatcher.add_handler(CommandHandler("repite",repite))

    #añade manejador para el comando /suma

    updater.dispatcher.add_handler(CommandHandler("suma",suma))



    #Empieza el bot
    updater.start_polling()
    # capturamos señal de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola mundo")

def repite(update,context):
    update.message.reply_text(update.message.text)

def suma (update,context):
    #args son las palabras que mandás con telegram
    # hace 
    resultado = int (context.args[0]) + int(context.args[1]) 
    #vuelve a string
    resultado = str(resultado) 
    update.message.reply_text("El reusltado es "+resultado)

main()