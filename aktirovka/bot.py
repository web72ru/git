import cursor as cursor
import telebot
import sqlite3
from kluch import kluch

bot = telebot.TeleBot(kluch)


# Рабочий кусок кода, который записывает и удаляет ид телеграма
@bot.message_handler(commands=['start'])
def start(message):
    # подключение к базе данных
    соединение = sqlite3.connect('polzovateli.db')
    курсор = соединение.cursor()

    курсор.execute("""CREATE TABLE IF NOT EXISTS login_id(id INTEGER)""")
    соединение.commit()

    # Существует ли пользователь в базе данных
    телеграм_ид = message.chat.id
    курсор.execute(f"SELECT id FROM login_id WHERE id = {телеграм_ид}")
    база = курсор.fetchone()
    if база is None:
        # Добавление пользователя Телеграма
        польз_ид = [message.chat.id]
        курсор.execute("INSERT INTO login_id VALUES(?);", польз_ид)
        соединение.commit()
        bot.send_message(message.chat.id, 'Вы подписались на рассылку актировки')
    else:
        bot.send_message(message.chat.id, 'Вы уже подписаны на рассылку актировки')


@bot.message_handler(commands=['delete'])
def delete(message):
    # подключение к базе данных
    соединение = sqlite3.connect('polzovateli.db')
    курсор = соединение.cursor()

    # Удаление пользователя из базы данных
    телеграм_ид = message.chat.id
    курсор.execute(f"DELETE FROM login_id WHERE id = {телеграм_ид}")
    соединение.commit()
    bot.send_message(message.chat.id, 'Вы отписались на рассылку актировки')


bot.polling()

телеграм_рассылка = 'Просизвольное сообщение, которое должны получить все подписчики тг бота.'

'''
@bot.message_handler(commands=['dist'])
def dist(message):
    соединение = sqlite3.connect('polzovateli.db')
    курсор = соединение.cursor()
    кортеж_телеграм_ид = курсор.execute("SELECT id FROM login_id")
    for один_ид in кортеж_телеграм_ид:
        bot.send_message(один_ид[0], телеграм_рассылка)
        print(один_ид[0])
    соединение.close()
'''




'''
# Рабочий кусок кода доказывающий, что подключение к базе работает и циклом достаёт из базы ид
соединение = sqlite3.connect('polzovateli.db')
курсор = соединение.cursor()
кортеж_телеграм_ид = курсор.execute("SELECT id FROM login_id")
for один_ид in кортеж_телеграм_ид:
    print(один_ид[0])
соединение.close()
'''