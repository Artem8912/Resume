# Данный модуль содержит словарь с html-кодом главной страницы сайта


import requests #Импортируем библиотеку requsts для работы с запросами на сервер сайта
url = 'https://armastock.ru/catalog'#Записываем в переменную url-адрес сайта

# Отправляем get-запрос на сервер и получаем html-код cfqnf
code = requests.get(url).text

# Создаём словарь с html-кодом главной страницы

dict_site_code = {'armastock.ru':code}