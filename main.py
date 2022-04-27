from Pustaka import Mesin_pencari,df
import telebot

bot = telebot.TeleBot("2008546622:AAGBwXOQZiF0ULcihUBLXbukI-O8eGxZWW0")

mesin = Mesin_pencari(df.demografik_dosen,df)
mesin.fit()
user_history = []

print("\n================================>")
print("running bot")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,f"""
Halo {message.from_user.first_name} ini adalah sebuah layanan yang kami bangun dimana kamu dapat dengan mudah
mengakses nomor dosen yang ingin kamu hubungi cara penggunaannya sangat gampang
kamu cukup tuliskan nama dosen yang ingin kamu cari atau mata kuliah apa beliau mengajar, semoga hari kamu menyenangkan :)
""")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"""Penggunaanya mudah banget kok kamu tinggal tulis nama dosen yang kamu cari \n
    contoh:\n
    saya ingin mencari nomor Bapak Wahyu Wardhana \n maka saya cukup menulis nama beliau atau dimata kuliah 
    mana beliau mengajar (´▽｀)""")
@bot.message_handler(content_types=['text'])
def main(message):
    bot.send_message(message.chat.id,"oke permintaan kamu kami proses")
    data = {'user':message.from_user.first_name,'id':message.from_user.id,'chat':message.text}
    pesan = message.text
    nomor,nama = mesin.predict([pesan])
    user_history.append(data)
    # print(user_history)
    bot.send_message(message.chat.id, f"berikut nomor telepon yang besangkutan : {nama}")
    bot.reply_to(message, f"{nomor}")
    print(user_history)

@bot.message_handler(commands=['dont'])
def cocok():
    pass


bot.polling()