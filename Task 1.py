import datetime
from requests import get
import time

def get_time_data():
 url = "https://yandex.com/time/sync.json?geo=213"
 start_time = time.time()

#Задание 1 - a
#Отправляем get запрос и получаем данные в формате json 
 response = get(url)
 data = response.json()
 end_time = time.time()
 print(data)

#Задание 1 - b
#
 timestamp = data.get("time") / 1000 #Переводим миллисекунды в секунды
 time_zone = data.get("clocks", {}).get("213", {}).get("name")
 people_time = datetime.datetime.fromtimestamp(timestamp)
 print(time_zone)
 print(people_time)

#Задание 1 - c
 server_time = timestamp
 locals_time = start_time + (end_time - start_time)/2 #Cреднее между временем отправки запроса и получения ответа
 delta = (server_time - locals_time)
 print(f"Дельта времени: {delta} секунд")
 return delta
 
#Задание 1 - d
deltas = []
for i in range(5):
    print(f"\nЗапрос #{i+1}")
    delta = get_time_data()  
    deltas.append(delta)

average_delta = sum(deltas) / len(deltas) # Вычисляем среднюю разницу по всем измерениям
print(f"\nСредняя дельта по 5 запросам: {average_delta} секунд")