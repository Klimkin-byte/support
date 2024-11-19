import random
import telebot
from telebot import types

bot=telebot.TeleBot("6645530171:AAGxbzvX7acpwjy9lHzSBaRN0gvLO0xm_TY")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Сыграем в игру")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne=types.KeyboardButton("/select")
    butTwo=types.KeyboardButton("/close")
    markup.add(butOne,butTwo)
    bot.send_message(message.chat.id,"Select",reply_markup=markup)
@bot.message_handler(commands=["close"])
def close(message):
    bot.send_message(message.chat.id,"<em><b>ohrana otmena</b></em>",parse_mode="html")

@bot.message_handler(commands=['select'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne=types.KeyboardButton("Start")
    butTwo=types.KeyboardButton("Finish")
    markup.add(butOne,butTwo)
    bot.send_message(message.chat.id,"Выбери ",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def buttonText(message):
    if message.text == "Start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Камень")
        butTwo = types.KeyboardButton("Ножницы")
        butThree = types.KeyboardButton("Бумага")
        butFour = types.KeyboardButton("Close")
        markup.add(butOne, butTwo, butThree, butFour)
        bot.send_message(message.chat.id, "Choose", reply_markup=markup)
    elif message.text == "Finish":
        bot.send_message(message.chat.id, "Goodbye")
    elif message.text == "Камень":
        b=random.randrange(1,4)
        a=1
        if a == 1 and b == 1 or a == 2 and b == 2 or a == 3 and b == 3:
            bot.send_message(message.chat.id,"Ничья Kамень-Kамень")
        elif a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1:
            bot.send_message(message.chat.id,"Ты выиграл Kамень-Hожницы")
        elif a == 1 and b == 3 or a == 3 and b == 2 or a == 2 and b == 1:
            bot.send_message(message.chat.id,"Бот тебя выиграл Kамень-Бумага")
    elif message.text == "Ножницы":
        b=random.randrange(1,4)
        a=2
        if a == 1 and b == 1 or a == 2 and b == 2 or a == 3 and b == 3:
            bot.send_message(message.chat.id,"Ничья Ножницы-Ножницы")
        elif a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1:
            bot.send_message(message.chat.id,"Ты выиграл Ножницы-Бумага")
        elif a == 1 and b == 3 or a == 3 and b == 2 or a == 2 and b == 1:
            bot.send_message(message.chat.id,"Бот тебя выиграл Ножницы-Камень")
    elif message.text == "Бумага":
        b=random.randrange(1,4)
        a=3
        if a == 1 and b == 1 or a == 2 and b == 2 or a == 3 and b == 3:
            bot.send_message(message.chat.id,"Ничья Бумага-Бумага")
        elif a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1:
            bot.send_message(message.chat.id,"Ты выиграл Бумага-Камень")
        elif a == 1 and b == 3 or a == 3 and b == 2 or a == 2 and b == 1:
            bot.send_message(message.chat.id,"Бот тебя выиграл Бумага-Ножницы")
    elif message.text == "Close":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Start")
        butTwo = types.KeyboardButton("Finish")
        markup.add(butOne, butTwo)
        bot.send_message(message.chat.id, "Select", reply_markup=markup)
        bot.send_message(message.chat.id, "GG")
    else:
        bot.send_message(message.chat.id, "Error")



bot.infinity_polling()