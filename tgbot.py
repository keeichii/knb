import telebot
from telebot import types
import webbrowser
bot = telebot.TeleBot('tg bot token')



@bot.message_handler(commands=['start', 'main', 'hello'])
def start_bot(message):
   first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, дарова\nхочешь соснуть хуйца в камень-ножницы-бумага?"
   markup = types.InlineKeyboardMarkup()
   button_yes = types.InlineKeyboardButton(text='я тя трахну', callback_data='yes')
   button_no = types.InlineKeyboardButton(text='не', callback_data='no')
   markup.add(button_yes, button_no)
   bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

def choice(message):
   s12 = "ну выбирай епта"
   markup = types.InlineKeyboardMarkup()
   button_k = types.InlineKeyboardButton(text='камень', callback_data='k')
   button_n = types.InlineKeyboardButton(text='ножницы', callback_data='n')
   button_b = types.InlineKeyboardButton(text='бумага', callback_data='b')
   markup.add(button_k, button_n, button_b)
   bot.send_message(message.chat.id, s12, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
   s2 = '<b>ты идиот?</b>'
   bot.send_message(message.chat.id, s2, parse_mode='html')

@bot.message_handler(commands=['site', 'website'])
def site(message):
   webbrowser.open('https://vk.com/keeichi')

@bot.callback_query_handler(func=lambda callback: True)
def knb(callback):
   if callback.data == 'yes' or callback.data == 'again':
      choice(callback.message)
   elif callback.data == 'del':
      bot.delete_message(callback.message.chat.id, callback.message.message_id)
   elif callback.data == 'no':
      site(callback.message)
   elif callback.data == 'k':
      s = 'а у меня бумага, лошок)'
      markup = types.InlineKeyboardMarkup()
      button = types.InlineKeyboardButton(text='заново', callback_data='again')
      markup.add(button)
      bot.send_message(callback.message.chat.id, s, reply_markup=markup)
   elif callback.data == 'n':
      s = 'а у меня камень, лошок)'
      markup = types.InlineKeyboardMarkup()
      button = types.InlineKeyboardButton(text='заново', callback_data='again')
      markup.add(button)
      bot.send_message(callback.message.chat.id, s, reply_markup=markup)
   elif callback.data == 'b':
      s = 'а у меня ножницы, лошок)'
      markup = types.InlineKeyboardMarkup()
      button = types.InlineKeyboardButton(text='заново', callback_data='again')
      markup.add(button)
      bot.send_message(callback.message.chat.id, s, reply_markup=markup)
   else:
      help(callback.message)

@bot.message_handler(content_types=['photo'])
def photo(message):
   markup = types.InlineKeyboardMarkup()
   button_del = types.InlineKeyboardButton(text='удали себя нахуй из этой жизни', callback_data='del')
   markup.add(button_del)
   bot.reply_to(message, 'какое же ты уебище, анлак', parse_mode='html', reply_markup=markup)

@bot.message_handler()
def kkk(message):
   if message.text.lower():
      bot.reply_to(message, 'иди нахуй', parse_mode='html')




bot.polling(none_stop=True)




'''from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, дарова\nхочешь соснуть хуйца в камень-ножницы-бумага?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'я тя трахну', callback_data='yes')
  button_no = types.InlineKeyboardButton(text='не', callback_data='no')
  markup.add(button_yes)
  markup.add(button_no)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response1(function_call1):
  if function_call1.message:
     if function_call1.data == "yes":
        second_mess = "ну выбирай епта"
        markup = types.InlineKeyboardMarkup()
        button_k = types.InlineKeyboardButton(text='камень', callback_data='k')
        #button_n = types.InlineKeyboardButton(text='ножницы', callback_data='n')
        #button_b = types.InlineKeyboardButton(text='бумага', callback_data='b')
        markup.add(button_k)
        #markup.add(button_n)
        #markup.add(button_b)
        botTimeWeb.send_message(function_call1.message.chat.id, second_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call:True)
def response2(function_call2):
  if function_call2.message:
     if function_call2.data == "k":
        rd_mess = "а у меня бумага, лошок)"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ну лан(", url="https://timeweb.cloud/"))
        markup.add(types.InlineKeyboardButton("заново нахуй", url="https://timeweb.cloud/"))
        botTimeWeb.send_message(function_call2.message.chat.id, rd_mess, reply_markup=markup)


     if function_call.data == "b":
        rd_mess = "а у меня ножницы, лошок)"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ну лан(", url="https://timeweb.cloud/"))
        markup.add(types.InlineKeyboardButton("заново нахуй", url="https://timeweb.cloud/"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

     if function_call.data == "n":
        rd_mess = "а у меня камень, лошок)"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ну лан(", url="https://timeweb.cloud/"))
        markup.add(types.InlineKeyboardButton("заново нахуй", url="https://timeweb.cloud/"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

botTimeWeb.infinity_polling()'''
