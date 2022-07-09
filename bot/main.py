import os
import telebot

import check
from subinfo import subinfo
from config import config
from ddl import addurl
from ddl import read_str


VERSION = config["VERSION"]
TOKEN = config["TOKEN"]
USER = config["USER"]
API_KEY = TOKEN
bot = telebot.TeleBot(API_KEY)
    
@bot.message_handler(commands=['start'])
def start(message): 
  if message.chat.id != USER:
    bot.send_message(message.chat.id, "警告！警告!这不是你的机器人,请不要乱动"+'\n'+
                    '用户：@'+message.chat.username+'\n'+
                    '用户ID：'+str(message.chat.id)+'\n'+
                    '已记录')
    bot.send_message(USER, "警告！警告"+'\n'+
                     '用户：@'+message.chat.username+'\n'+
                     '用户ID：'+str(message.chat.id)+'\n'+
                     '正在使用机器人')
  else:
    bot.send_message(message.chat.id, "你好，主人")

@bot.message_handler(commands=["help"])
def help(message): 
    bot.send_message(message.chat.id, "/start")

@bot.message_handler(commands=['add'])
def add(message):
  text = message.text
  text = text.strip('/add ')
  addurl(text)
  bot.reply_to(message, "订阅链接："+text+'\n\n'+
              '添加成功')
  atext = subinfo(read_str())
  bot.send_message(message.chat.id,atext)

@bot.message_handler(commands=['update'])
def update(message):
  check.init()
  bot.reply_to(message, "订阅链接："+'\n\n'+
              '更新成功')
  atext = subinfo(read_str())
  bot.send_message(message.chat.id,atext)

@bot.message_handler(commands=['wget'])
def wget(message):
  url_downlosd = check.get_url()
  bot.reply_to(message, "订阅链接："+url_downlosd+'\n\n'+
              '更新成功')

@bot.message_handler(commands=['del'])
def delurl(message):
  text = message.text
  text = text.strip('/del ')
  mt = int(text)-1
  check.del_url(mt)
  bot.reply_to(message, "订阅编号："+str(text)+'\n\n'+
              '删除成功')



# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): 
#     atext=subinfo(message.text)
#     bot.send_message(message.chat.id, atext)

if __name__ == '__main__':
     bot.polling(none_stop=True)
