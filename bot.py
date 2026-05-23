import telebot
import os

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("8943965379:AAFe2Zm_ZCiPDV0HTTxAp31JMC04x40Rk1E")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

# Обработчик команды '/mem'
@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    for image in images:
        with open(f'images/{image}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)

# Обработчик команды '/eco'
@bot.message_handler(commands=['eco'])
def send_eco(message):
    bot.reply_to(message, "Экология — наука о взаимоотношениях живых организмов между собой и с окружающей их средой. Она изучает организацию и функционирование биологических систем различных уровней: популяций, биоценозов (сообществ), экосистем и биосферы в целом.")


@bot.message_handler(commands=['nature'])
def send_nature(message):
    bot.reply_to(message, "Природа — это материальный мир Вселенной в его естественном состоянии, не изменённый деятельностью человека. Это всё, что окружает человека и не создано его руками.")


@bot.message_handler(commands=['pollution'])
def send_pollution(message):
    bot.reply_to(message, "Загрязнение — это процесс внесения в окружающую среду веществ или энергии, которые могут причинить вред живым организмам или нарушить нормальное функционирование экосистем. Загрязнение может быть вызвано различными источниками, такими как промышленность, транспорт, сельское хозяйство и бытовые отходы.")

# Запуск бота
bot.polling()
