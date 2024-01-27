from redbox.query import UNSEEN
from redbox import EmailBox
from redmail import EmailSender
import json
import imaplib
import ssl
import base64 

# https://red-mail.readthedocs.io/en/stable/
# https://red-box.readthedocs.io/en/latest/

const_dict = json.load(open('const.json', 'r'))
SOURCE_ADDR = const_dict['email']
PSWD = const_dict['pass']
HOST = "imap.spaceweb.ru"

# ctx = ssl.create_default_context()
# ctx.set_ciphers('DEFAULT')


class SSL_low(imaplib.IMAP4_SSL):
    def __init__(self, ssl_context, *args, **kwargs):
        super().__init__()

        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT')
        self.ssl_context = ctx

        print(self)


# imap_class = imaplib.IMAP4_SSL(host=HOST, ssl_context=ctx)
box = EmailBox(
    host=HOST,
    port=993,
    username=SOURCE_ADDR,
    password=PSWD,
    # cls_imap=SSL_low,
)

sender = EmailSender(
    host='smtp.spaceweb.ru',
    port=587,
    username=SOURCE_ADDR,
    password=PSWD
)

# print(box.kws_imap)
inbox = box['INBOX']

mails_list = []
count = 0
for msg in inbox.search('ALL'):
    msg.read()

    sender_mail = msg.from_
    mails_list.append(msg)
    
    if msg.from_.lstrip().startswith('='):
        data = msg.from_.strip('\n\r\t ').split(' ')[0]
        print(f'---> {data} <---')
    try:
        if msg.text_body:
            count += 1
            with open('1.txt', 'a+') as file:
                a = '=====' * 100
                file.write(msg.text_body)
                file.write(a + '\n')
                
    except TypeError:
        print('wrong type')

print(count, 'записано писим в файл')
# for i in mails_list:
#     sender.send(
#         sender=i.from_,
#         subject='resend',
#         receivers=['tipkor@mail.ru',],
#         text=f'Объект пересылки: {i.text_body}',
#     )
