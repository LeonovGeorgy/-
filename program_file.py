# Убедитесь что все библиотеки установлены.
import requests
import json

# Функция, которая отправляет SMS
def sendsms(number, message, sender):
    url = "https://api.iqsms.ru/messages/v2/send.json"
    body = {"phone": number, "text": message, "sender": sender, "statusQueueName": "qwerty"}
    headers = {"Content-Type": "application/json", "charset": "utf-8", "X-Api-Key": "api_key"}
    response = requests.post(url, json.dumps(body), headers=headers)
# Вместо "api_key" вставьте свой ключ

# Путь к файлу с заготовленным текстом и данными адресата
filename = 'message.txt'
with open(filename, 'r') as f:
    lines = f.readlines()
    name = lines[0].strip()
    phone = lines[1].strip()
    message = lines[2].strip()

# Номер или аналог, с которого отправляем сообщения
sender = "SenderName"

# Сообщение, которое отправляем адресату
msg = f"Привет, {name}! {message}"

# Отправляем SMS
sendsms(phone, msg, sender)

# Для массовой отправки потребуется немного доработать работу с файлом.
# Думаю с этим уже ни у кого проблем не будет. Всем успехов! ))
