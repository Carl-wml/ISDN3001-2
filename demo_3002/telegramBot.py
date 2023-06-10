import telebot
import notificationHandler as nh
import threading
# token = r'6248471775:AAG_NOphIUK-vo1h2fw4vlhMmt52c_IrEX8'
class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot = telebot.TeleBot(token)

# Define a function to handle incoming messages from users
        
        @self.bot.message_handler(func=lambda message: True)
        def echo_message(message):
            # Send a reply message to the user with their original message
            # self.bot.reply_to(message, message.text)
            self.bot.reply_to(message, "Sorry, busy now, will get back to you...")
            # chat_id = message.chat.id

        # # Send a reply message to the user with their chat ID
            # bot.reply_to(message, f"You are chatting with chat ID {chat_id}")
            # print(message.text, chat_id)
            nh.NotificationHandler().show_notification("Telegram", message.text+" from "+str(message.chat.id))
            threading.Thread(target=self.bot.polling).start()

# Start the bot and listen for incoming messages
    def polling(self):
        self.bot.polling()

    def send_message(self, chat_id, message):
        self.bot.send_message(chat_id, message)


# #To-used !!!
# tb = TelegramBot(r'6248471775:AAG_NOphIUK-vo1h2fw4vlhMmt52c_IrEX8')
# tb.polling()
# tb.send_message(6179628881, "Hello World!")
# 6179628881, 6123913070, 6038638909
