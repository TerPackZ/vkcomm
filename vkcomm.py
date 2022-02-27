import vk_api
import pyfiglet
from colorama import init, Fore, Back, Style
import random
import vk
import time
import os
import sys

banner = ("""
 __   __   __  __                               
/\ \ / /  /\ \/ /                               
\ \ \'/   \ \  _"-.                             
 \ \__|    \ \_\ \_\                            
  \/_/      \/_/\/_/                            

 ______     ______     __    __     __    __    
/\  ___\   /\  __ \   /\ "-./  \   /\ "-./  \   
\ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \ \-./\ \  
 \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_\ \ \_\ 
  \/_____/   \/_____/   \/_/  \/_/   \/_/  \/_/ """)
print(banner)

subscribe = input("Подписаться на автора в Telegram? (Y/n) ")
if subscribe == "y":
    os.system("termux-open-url 'https://t.me/joinchat/RUQ98c7lE_wUXexn'")
elif subscribe == "n":
    token = input("Введите токен: ")
    user_id = input("Введите айди страницы: ")
    posts_id = input("Введите айди поста: ")
    msgs = input("Введите сообщение: ")
    session = vk.Session(access_token=token)
    apivk = vk.API(session, v=5.95)
while True:
        print(apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs, guid=random.randint(0, 9999999999)))
        time.sleep(3)
