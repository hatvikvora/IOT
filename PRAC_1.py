import telepot
token = '1300125276:AAH3WY-1F2vYyloTtGdXj4rbr_zMO99e8t0'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id.format(msg["text"]))

TelegramBot.message_loop(handle)
