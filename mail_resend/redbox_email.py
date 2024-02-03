import pprint
from redbox.query import UNSEEN, ALL
from redbox import EmailBox
from redmail import EmailSender
from redbox.models.message import EmailMessage
from typing import List, Type, Union

import json
import imaplib
import ssl
import base64
# import dill

# https://red-mail.readthedocs.io/en/stable/
# https://red-box.readthedocs.io/en/latest/


const_dict = json.load(open("const.json", "r"))
SOURCE_ADDR = const_dict["email"]
PSWD = const_dict["pass"]
HOST = "imap.spaceweb.ru"


# ctx = ssl.create_default_context()
# ctx.set_ciphers('DEFAULT')


box = EmailBox(
    host=HOST,
    port=993,
    username=SOURCE_ADDR,
    password=PSWD,
)

sender = EmailSender(
    host="smtp.spaceweb.ru", port=587, username=SOURCE_ADDR, password=PSWD
)

inbox = box["INBOX"]
mails_list = []
count = 0


def write_message(messages: List[EmailMessage]) -> None:

    for i in messages:
        print(i.headers['Content-Type'])
        if 'multipart/mixed' in i.headers['Content-Type']: # тип контакта в хедере
            if i.html_body.startswith('<'): # если, начинается html c '<'
                print('header - --------------------', i.html_body)
                mails_list.append(i.html_body) 
                continue
            print(i.html_body)
            body_mail_b64 = base64.b64decode(i.html_body).decode()
            print(body_mail_b64)
            mails_list.append(body_mail_b64)
        elif 'text/plain' in i.headers['Content-Type']:
            print('header - --------------------', i.html_body)
            mails_list.append(i.html_body)



msg_list = []

for msg in inbox.search(ALL):
    msg_list.append(msg)


write_message(msg_list)
pprint.pprint(mails_list)


for i in mails_list:
    html_mail = i
    # subject = base64.b64decode(i.headers['Subject']).decode()
    sender.send(
        # headers=i_headers,
        html=html_mail,
        # sender=msg.from_,
        subject="resend",
        receivers=[
            "tipkor@mail.ru",
        ],
        # text=f'Объект пересылки: {i.text_body}',
    )
