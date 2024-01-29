import base64


with open('from.txt', 'r') as f:
    data = f.read().split()

x = [i for i in data if i.startswith('=')]
# print(x)


for _ in x:
    if _[0] != '<' or not _[0]:
        data_t = _.lstrip('=?UTF-8?B?')
# проблема в малом регистре и другой кодивровке
        print(data_t)
        # try:
        print(base64.b64decode(data_t).decode())
        # except:
        #     print('wrong --- ', data_t)