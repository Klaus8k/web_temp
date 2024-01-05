import json
import urllib.request

#адрес для отправки json-запросов
url = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns'

#данные для OAuth-авторизации
token = 'y0_AgAAAAABQ46tAAsR2gAAAAD3JOn12TELnbA-SFStLmzZejUu4yBEiyI'

#логин в Директе
login = 'klaus888'

#структура входных данных (словарь)
data = {
   'method': 'GetCampaignsList',
   'token': token,
   'locale': 'ru',
   'param': [login]
}

#конвертировать словарь в JSON-формат и перекодировать в UTF-8
jdata = json.dumps(data, ensure_ascii=False).encode('utf8')

#выполнить запрос
response = urllib.request.urlopen(url, jdata)

#вывести результат
a = response.read().decode('utf8')
print(a)