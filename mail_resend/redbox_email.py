import pprint
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


def clean_base(data):
    return data.from_.strip('\n\r\t ').split(' ')[0]


for msg in inbox.search('ALL'):
    # msg.read()

    sender_mail = msg.from_
    mails_list.append(msg)
    html_list = []

    try:
        if msg.text_body:
            # message = msg.html_body
            with open('from.txt', 'a+', encoding="utf-8") as file:
                if not sender_mail[0].isalpha():
                    # file.write(sender_mail + '\n')
                    # file.write(message)
                    # html_list.append(message)
                    file.write('==============' * 10)
                    # count += 1

    except TypeError:
        print('wrong type')
import traceback
print(count, 'записано писим в файл')
for i in mails_list[:2]:
    # pprint.pprint(i.headers)
    try:
        pprint.pprint(i.headers)
        sender.send(
            html=i.html_body,
            headers=i.headers,
            sender=i.from_,
            subject='resend',
            receivers=['tipkor@mail.ru',],
            # text=f'Объект пересылки: {i.text_body}',
        )
    except ValueError as inst:
        pprint(traceback.print_exc())
