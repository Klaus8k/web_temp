from redbox.query import UNSEEN
from redbox import EmailBox
from redmail import EmailSender
import json
import imaplib
import ssl


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
    cls_imap=SSL_low,
)

sender = EmailSender(
    host='smtp.spaceweb.ru',
    port=587,
    username=SOURCE_ADDR,
    password=PSWD
)

print(box.kws_imap)
inbox = box['INBOX']

for msg in inbox.search(UNSEEN):
    msg.read()
    print(msg)

    sender = msg.from_
    subject = msg.subject

sender.send(
    subject='resend',
    receivers=[sender],
    text=f'Объект пересылки: {subject}',
)
