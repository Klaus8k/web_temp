
# -*- coding: utf-8 -*-
import requests, json
from requests.exceptions import ConnectionError
from time import sleep

#  Метод для корректной обработки строк в кодировке UTF-8 как в Python 3, так и в Python 2
import sys
if sys.version_info < (3,):
    def u(x):
        try:
            return x.encode("utf8")
        except UnicodeDecodeError:
            return x
else:
    def u(x):
        if type(x) == type(b''):
            return x.decode('utf8')
        else:
            return x

# --- Входные данные ---
import os
with open('id_token.json', 'r', encoding='utf-8') as file:
    ID_info = json.loads(file.read())
print(ID_info)



#  Адрес сервиса Campaigns для отправки JSON-запросов (регистрозависимый)
CampaignsURL = ID_info['CampaignsURL']

# OAuth-токен пользователя, от имени которого будут выполняться запросы
token = ID_info['yandex_token']

# Логин клиента рекламного агентства
# Обязательный параметр, если запросы выполняются от имени рекламного агентства
clientLogin = ID_info['clientLogin']

# --- Подготовка, выполнение и обработка запроса ---
#  Создание HTTP-заголовков запроса
headers = {"Authorization": "Bearer " + token,  # OAuth-токен. Использование слова Bearer обязательно
           "Client-Login": clientLogin,  # Логин клиента рекламного агентства
           "Accept-Language": "ru",  # Язык ответных сообщений
           }

# Создание тела запроса
body = {"method": "get",  # Используемый метод.
        "params": {"SelectionCriteria": {},  # Критерий отбора кампаний. Для получения всех кампаний должен быть пустым
                   "FieldNames": ["Id", "Name"]  # Имена параметров, которые требуется получить.
                   }}

# Кодирование тела запроса в JSON
jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')

# Выполнение запроса
try:
    result = requests.post(CampaignsURL, jsonBody, headers=headers)

    # Отладочная информация
    # print("Заголовки запроса: {}".format(result.request.headers))
    # print("Запрос: {}".format(u(result.request.body)))
    # print("Заголовки ответа: {}".format(result.headers))
    # print("Ответ: {}".format(u(result.text)))
    # print("\n")

    # Обработка запроса
    if result.status_code != 200 or result.json().get("error", False):
        print("Произошла ошибка при обращении к серверу API Директа.")
        print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
        print("Описание ошибки: {}".format(u(result.json()["error"]["error_detail"])))
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
    else:
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
        print("Информация о баллах: {}".format(result.headers.get("Units", False)))
        # Вывод списка кампаний
        to_send = []
        for campaign in result.json()["result"]["Campaigns"]:
            to_send.append("Рекламная кампания: {} №{}".format(u(campaign['Name']), campaign['Id']))
            
            print("Рекламная кампания: {} №{}".format(u(campaign['Name']), campaign['Id']))

        if result.json()['result'].get('LimitedBy', False):
            # Если ответ содержит параметр LimitedBy, значит,  были получены не все доступные объекты.
            # В этом случае следует выполнить дополнительные запросы для получения всех объектов.
            # Подробное описание постраничной выборки - https://tech.yandex.ru/direct/doc/dg/best-practice/get-docpage/#page
            print("Получены не все доступные объекты.")


# Обработка ошибки, если не удалось соединиться с сервером API Директа
except ConnectionError:
    # В данном случае мы рекомендуем повторить запрос позднее
    print("Произошла ошибка соединения с сервером API.")

# Если возникла какая-либо другая ошибка
except: 
    # В данном случае мы рекомендуем проанализировать действия приложения
    print("Произошла непредвиденная ошибка.")
    
    
# Отправка в чат телеграм
token_telegram = ID_info['token_telegram']

chat_id_list = ID_info['ChatID_list']['tipkor']

def telegram_bot_sendtext(bot_message):
   bot_token = token_telegram
   bot_chatID = '1030752327' # ID чата бот-пользователь, нужен что бы в эту переписку кидались сообщения.
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()
test = telegram_bot_sendtext(str(to_send))
print(test)