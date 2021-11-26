import telebot
from telebot import types
# import threading

import config
from geniusAPI import genius


bot = telebot.TeleBot(config.TOKEN_TEST)


@bot.message_handler(commands=['start'])
def welcome(message):
    # sticker = open('static/welcome_stricker.webp', 'rb')
    # bot.send_sticker(message.chat.id, sticker)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Text of song 🎤")
    item2 = types.KeyboardButton("Log in Spotify 🎼")

    markup.add(item1, item2,)

    bot.send_message(message.chat.id,
                     "Hi, {0.first_name}!" +
                     "\nI am <b>{1.first_name}</b> - bot which can analize your music on Spotify.\n" +
                     "Also I can give you a text of needed song." +
                     "\nWhat do you want to do?".format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.chat.type == 'private':
        if message.text == "Text of song 🎤":
            bot.send_message(message.from_user.id, '👇 Enter the name of artist 👇')
            bot.register_next_step_handler(message, get_genius_artist)
        elif message.text == "Log in Spotify 🎼":
            bot.send_message(message.chat.id, "Greetings 🥂🥂🥂 \nFollow this link to authorize in Spotify: \n\nhttp://127.0.0.1:5000/")
        else:
            bot.send_message(message.chat.id, "Incorrect input ❌")


def get_genius_artist(message):
    global artist
    artist = message.text
    bot.send_message(message.from_user.id, '👇 Enter the name of song 👇')
    bot.register_next_step_handler(message, get_genius_song)


def get_genius_song(message):
    global song
    song = message.text
    bot.send_message(message.chat.id, 'Wait a few seconds...')
    result = genius(artist, song)
    bot.send_message(message.chat.id, result)


bot.polling(none_stop=True)
