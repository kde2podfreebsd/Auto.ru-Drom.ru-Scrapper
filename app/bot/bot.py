import os
import json
import telebot
from typing import Optional
from dotenv import load_dotenv
from telebot import types


config = load_dotenv()
bot = telebot.TeleBot(os.getenv("telegram_bot_token"))

chat_ids = [406149871, 528661452]

off_markup = types.ReplyKeyboardRemove(selective=False)

start_msg = "*Парсер для графа*"

menu_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtn1 = types.KeyboardButton('/change_top_price')
menu_btn.add(itembtn1)

@bot.message_handler(commands=['start'])
def start(message) -> None:
    try:
        print(message.chat.id)
        bot.send_message(message.chat.id, start_msg, reply_markup=menu_btn, parse_mode='MARKDOWN')
    except Exception as e:
        bot.reply_to(message, f'{e}')

@bot.message_handler(commands=['change_top_price'])
def change_top_price(message) -> None:
    try:
        msg = bot.send_message(message.chat.id, 'Укажите предельную цену', reply_markup=off_markup, parse_mode='MARKDOWN')
        bot.register_next_step_handler(msg, setup_top_price)

    except Exception as e:
        bot.reply_to(message, f'{e}')

def setup_top_price(message):
    try:
        top_price = message.text
        data = {"price": top_price}
        with open('../data.json', 'w') as outfile:
            json.dump(data, outfile)

        bot.send_message(message.chat.id, f'Предельная цена обновлена: {top_price}', reply_markup=menu_btn, parse_mode='MARKDOWN')

    except Exception as e:
        bot.reply_to(message, f'{e}')

def send_ad(
        href: str,
        name: str,
        price: str,
        details: str,
        service: str,
        milage: Optional[str] = None,
        year: Optional[str] = None
):
    ad_msg = f'''
*Название:* {name}
*Цена:* {price}
*Детали:* {details}
*Сервис:* {service}
*Пробег:* {milage if milage is not None else "N/A"}
*Год:* {year if year is not None else "N/A"}
*Ссылка*: {href}
'''

    for id in chat_ids:
        bot.send_message(id, ad_msg, reply_markup=off_markup, parse_mode='MARKDOWN')


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
