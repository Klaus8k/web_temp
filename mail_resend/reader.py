import re
# from bs4 import BeautifulSoup
import base64
from email.header import decode_header
import email
import imaplib
import json


const_dict = json.load(open('const.json', 'r'))
email_adress = const_dict['email']
password = const_dict['pass']


imap_server = "imap.spaceweb.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_adress, password)
imap.select()
count_mail = imap.uid('search', "ALL")[1][0]
print(count_mail.split(b' '))
for i in count_mail.split(b' '):
    res, msg = imap.uid('fetch', i, '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])
    # дата получения, приходит в виде строки, дальше надо её парсить в формат datetime
    letter_date = email.utils.parsedate_tz(msg["Date"])
    letter_id = msg["Message-ID"]  # айди письма
    letter_from = msg["Return-path"]  # e-mail отправителя
    print(letter_date, letter_id, letter_from)

# https://habr.com/ru/articles/688784/
# получение одной библиотекой - отправка другой. Желательно в байтовом виде переслать
# https://sky.pro/media/kak-ispolzovat-python-dlya-raboty-s-elektronnoj-pochtoj/