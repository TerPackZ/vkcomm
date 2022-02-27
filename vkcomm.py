import vk_api
import pyfiglet
from colorama import init, Fore, Back, Style
import random
import vk
import time
import os
import sys
token = input("Введите токен: ")
user_id = input("Введите айди страницы: ")
posts_id = input("Введите айди поста: ")
msgs = input("Введите сообщение: ")
session = vk.Session(access_token=token)
apivk = vk.API(session, v=5.95)
while True:
    api.wall.createComment(owner_id=user_id,
                       post_id=posts_id,
                       message=msgs)
