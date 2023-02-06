import telebot
from telebot import types
import random

bot = telebot.TeleBot("5508313179:AAHIEVLg2SfHWNF-WbtJjYxrX0FtCQVHKCQ")  # Токин


####################
# _______Старт______#
####################

@bot.message_handler(commands=['start'])
def start(message):
    # преветственая клавиатура
    sto = open(
        'loli.png', 'rb')
    bot.send_photo(message.chat.id, sto)

    # Клавиатура
    clav = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cl1 = types.KeyboardButton("Манга")
    cl2 = types.KeyboardButton("Аниме")

    clav.add(cl1, cl2)

    # Приветствие
    bot.send_message(message.chat.id,
                     "Добро пожаловать хазяин, <b>{0.first_name}</b>!\n"
                     "Я - <b>{1.first_name}</b> я помогу вам быстро находить хентай с лольками.\n"
                     " <b>Ваш акаунт:</b> \n"
                     "<i>Логин:</i> <b>bakibos</b> \n"
                     "<i>Пароль:</i> <b>21bakibos21</b>\n"
                     "<i>Сперва перейди по этим силкам и войди используя логин и пароль выше :\n"
                     "<a href = 'https://hentaichan.live/tags/lolcon'>hentaichan</a>\n"
                     "<a href = 'https://nude-moon.org/tags/%D0%BB%D0%BE%D0%BB%D0%B8%D0%BA%D0%BE%D0%BD+'>nude-moon</a> \n"
                     "<a href ='https://animefox.org/hentai/lolicon/' >animefox</a>\n"
                     "<a href ='https://anifap.org/lolicon/'>anifap</a></i> ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=clav)


@bot.message_handler(content_types=['text'])
def lop(message):
    if message.text == "Манга":
        # Фото
        nud = open(
            'nud.png', 'rb')
        hent = open(
            'hent.png', 'rb')
        # Генератор рандома
        list = [1, 2]
        d = random.choice(list)
        if d == 1:
            # Кнопки
            kls = types.InlineKeyboardMarkup(row_width=1)
            itm = types.InlineKeyboardButton("Сылка",
                                             url="https://nude-moon.org/tags/%D0%BB%D0%BE%D0%BB%D0%B8%D0%BA%D0%BE%D0%BD+")
            kls.add(itm)
            # Фото
            bot.send_photo(message.chat.id, nud, reply_markup=kls)
        elif d == 2:
            # Кнопки
            kls2 = types.InlineKeyboardMarkup(row_width=1)
            itm2 = types.InlineKeyboardButton("Сылка",
                                              url="https://hentaichan.live/tags/lolcon")
            kls2.add(itm2)
            # Фото
            bot.send_photo(message.chat.id, hent, reply_markup=kls2)

    elif message.text == "Аниме":

        fox = open("hanime.png", "rb")
        fap = open("fap.png", "rb")

        list = [1, 2]
        d = random.choice(list)
        if d == 1:
            kls = types.InlineKeyboardMarkup(row_width=1)
            itm = types.InlineKeyboardButton("Сылка",
                                             url="https://animefox.org/hentai/lolicon/")
            kls.add(itm)
            # Фото
            bot.send_photo(message.chat.id, fox, reply_markup=kls)

        elif d == 2:
            kls2 = types.InlineKeyboardMarkup(row_width=1)
            itm2 = types.InlineKeyboardButton("Сылка",
                                             url="https://anifap.org/lolicon/")
            kls2.add(itm2)
            # Фото
            bot.send_photo(message.chat.id, fap, reply_markup=kls2)

try:
    if __name__ == "__main__":
        print("Бот запущен проблем нет")
        bot.polling(non_stop=True)
except Exception:
    print("Ошыбка")
