import pprint
from redbox.query import UNSEEN, ALL
from redbox import EmailBox
from redmail import EmailSender
import json
import imaplib
import ssl
import base64
import dill

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


for msg in inbox.search(UNSEEN):
    # if count == 1:
        # break
    sender_mail = msg.from_
    mails_list.append(msg)
    # count += 1

# for msg in mails_list:
#     x = dill.dumps(msg, protocol=4)
#     pprint.pprint(x)
#     # with dill.detect.trace():
#     #     dill.dumps(msg)

# msg = mails_list[0]
# pprint.pprint(msg.__dir__())
# open('from.txt', 'w').write(pprint.pformat(msg.headers))

# import traceback
# for _ in msg.headers.keys():
#     msg.headers[_] = ''.join(msg.headers[_].split('\r\n'))



for i in mails_list:
    sender.send(
        # headers=i_headers,
        html=i.html_body,
        # sender=msg.from_,
        subject="resend",
        receivers=[
            "tipkor@mail.ru",
        ],
        # text=f'Объект пересылки: {i.text_body}',
    )
