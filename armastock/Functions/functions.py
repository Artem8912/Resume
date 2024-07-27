# Данный модуль содержит функции, которые будут возвращать непостредственно данные о товарах и категориях

# Импортируем необходимые библиотеки для работы с сайтом
import requests # Библиотека web-запросов, отправляемых на сервер
from bs4 import BeautifulSoup # Библиотека, соержащая в себе методы для работы с данными сайта
import logging # Библиотека для записей о промежуточных стадиях выолнения программы
import re # Библиотека для работы с текстами
import os #  Библиотека для работы с файлами и директориями на компьютере
import json # Библиотека для работы с данными в json формате
import xlsxwriter # Библиотека для работы с файлами Excel


# Создаём объект класса logging для ведения отчётов об этапах выполнения программы    
logger = logging.getLogger(__name__)

# Устанавливаем базовую конфигурацию логирования: указываем начальный уровень логгирования (DEBUG - отладка) и указываем формат вывода записей
logging.basicConfig(level=logging.DEBUG,format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

# Создаём переменную, в которую записываем адрес стартовой страницы сайта 
url = 'https://armastock.ru/catalog'

# Делаем get-запрос для получения html-кода страницы
code = requests.get(url).text



# Функция, принимающая словарь html-кодов страниц категорий товаров и возвращающая словарь категорий товаров на 1 уровень ниже
    
def get_categories(dict:dict)->dict:
# Делаем запись о запуске функции
    logger.debug('Запуск функции get_categories')
# С помощью цикла проходимся по именам и html-кодам в словаре категорий товаров
    for name,html in dict.items():
# Проверяем наличие html-кода в поле под соотвествующим ключём словаря       
            if html != None:
# Если ключ есть - переходим к следующему блоку кода (если нет - выводим соответствующее сообщение)

# С помощью блока try/except ловим возможные исключения, которые могут возникнуть при выполнении кода              
                try:
                    # Создаём объект класса BeatifulSoup для разбора информациии с сайта 
                    soup = BeautifulSoup(html,features="lxml")
                    # Находим раздел со списком категорий
                    categories_list = soup.find(class_='section section-category').find(class_='wrapper').find(
                        class_='section-category-list')
                    if categories_list is None:
                        # Если раздел не найден, выбрасываем исключение
                        raise Exception('Ошибка в parse_categories - не найден элемент')

                    # Находим элементы списка категорий
                    category_items = categories_list.find_all('div', class_='section-category-list__item')
                    
                    # Создаём словарь со списком главных категорий           
                    dict_main_categories = {}
                    # Проходимся по элементам списка категорий и находим нужную информацию     
                    for item in category_items:
                        item = item.find('a', class_='section-category__item')
                        link = item.get('href')              
                        name = item.get_text().strip()  
                        img = item.find('div', class_='section-category__image').find('img')['src']
                        dict_main_categories[name] = link
                    # Выводим в консоль соответствующую информацию о данной категории товаров    
                        print(f"Категория : {name.strip()}\n"
                            f"Ссылка: {link}\n"
                            f"Изображение: {img}\n") 
                    
                    else:
                        print('Перечень категорий данного уровня завершён')
                        
                except :
                    print('Раздел с подкатегориями не найден')
                        
                        
            else:
                # Выводим сообщение, если html-код страницы - неккоректный
                logger.debug('Неккоректный HTML-файл')
                print()
    # Возвращаем словарь с категориями
    return dict_main_categories

                 
# Функция, возвращающая словарь с категориями нижнего уровня
# На вход функция принимает словарь с категориями на 1 уровень выше                    
def get_categ_info_by_level(dict:dict)->dict:
# Создаём словарь для хранения категорий
    dict_names_cat = {}
    try:    
# Проходимся с помощью по именам категорий
        for name,html in dict.items():
        # Создаём объект класса BeatifulSoup для разбора информациии с сайта 
                soup = BeautifulSoup(html,'lxml')
        # Находим элементы списка категорий
                category_items = soup.find_all('div', class_='section-category-list__item')
        # Если список - не пустой        
                if category_items is not None: 
        # Проходимся по элементам данного списка
                    for item in category_items:
        # Находим раздел с конкретной категорией
                            it_cat = item.find('a', class_='section-category__item')
        # Извлекаем соответствющую информацию (название и ссылку на категорию)
                            if it_cat is not None: # Проверяем наличие раздела с конкретной категорией
                                link = it_cat.get('href')  
                                text = item.get_text()  
                                Name = text.strip()
                                img = item.find('div', class_='section-category__image').find('img')['src']
        # Создаём словарь с именами категорий в качестве ключей и html-кодами в качестве значений
                                dict_names_cat[Name] = requests.get(link).text
                            else:
        # Если раздел с категорией не найден - выводим соответствующее сообщение
                                print('Раздел с категорией не найден')
                else:
        # Если раздел с категориями более нижнего уровня не найден - выводим соответсвующее сообщение
                    print('Раздел с категориями нижнего уровня не найден')
    except Exception as e:
        # Выводим соответствущее сообщение, если возникло непредвиденное исключение
        logger.debug('Возникло исключение',e)      
    # Возвращаем словарь с html-кодами страниц категорий товаров              
    return dict_names_cat

# Функция для очистки текста от ненужных символов                    
def clear_text(text:str)->str:

    try:
    # В случае, если в тексте встречаются указанные символы - убираем их
        for el in ['\\','\\n','| Армасток','/','\\','  Описание  ','   ']:
        
            text = text.replace(el,'')
    except Exception as e:
        print('Возникло исключение',e)
    # Убираем проелы слева и справа от текста    
    TEXT = text.strip()
    # Возращаем очищенный текст
    return TEXT



# Функция, возвращающая словарь с  основной информацию о товарах, на вход функция принимает словарь с html-кодами категорий товаров.
def get_dict_goods_by_categ(dict_cat:dict)->dict:
# Создаём словарь осоновной информации о товарах
    goods_by_categories = {}
    
    try:
        for Name,html in dict_cat.items():
            
    # Создаём объект класса BeatifulSoup для разбора информациии с сайта 
                soup = BeautifulSoup(html,features ='lxml')
    # Пытаемся найти разделы с категориями товаров ниженго уровня            
                category_items = soup.find_all(class_='section-category-list__item')
    # Если таких разделов нет - значит у данной категории нет подкатегорий и мы можем извлечь информацию о товарах
                if len(category_items) == 0:
    # Находим вложенный тэг со списком товаров 
                        wrapper_field = soup.find(class_='wrapper-field filter-buttons section-meta__reset')
    # Если тэг существует  
                        if wrapper_field is not None:
    # Находим тэг с разделом товаров
                            items = soup.find(class_='item-panel')
                            if items is not None:
    # Если тэг сущесвует - находим все товары в списке данного раздела
                                    goods = soup.find_all(class_='item-panel__main')
                                    if goods is not None:
    # Если товары - действительно есть - создаём словарь для сохраннения основной информации о товарах
                                        dict_goods = {}
                                        # Проходимся по каждому товару
                                        try:
                                            for good in goods:  
                                            # Создаём словарь с информацией о конкретном товаре
                                                    dict_good ={}
                                            # Извлекаем необходимую нам информацию из соответвующих тэгов
                                                    link = good.get('href')
                                                    name = good.find('div',class_='item-panel__title')
                                                    name = name.text.strip()
                                                    image = good.find('div',class_='item-panel__image').find('img')['src']
                                                    dict_good['Название'] = name
                                                    dict_good['Ссылка на товар'] = link
                                                    dict_good['Изображение'] = image
                                                    print(f'Название: {name} ')
                                                    print(f'Ссылка на товар: {link} ')
                                                    print(f'Изображение: {image} ')
                                            
                                            # В словарь всех товаров добавляем словарь с информацией о конкретном товаре по соответствующем
                                            # ключу (названию товара)        
                                                    dict_goods[name] = dict_good
                                        except Exception as e:
                                            print('Возникло исключение',e)
                                        # В словарь категорий по соответствующему ключу (имени категории) добавляем словарь с товарами
                                        goods_by_categories[f'Категория товара: {Name}'] = dict_goods
                                    else:
                                    # Если товаров в списке больше нет, выводим соответсвующее сообщение
                                        print('Перечень товаров завершён')
                            else:
                                # Если тэгов со списком товаров больше нет - выводим соотвествующее сообщение
                                    print('Перечень тэгов со списком товаров завершён')
                        else:
                            # Если раздел со списком товаров не найден - выводим соответсвующее сообщение
                            print('Раздел со списком товаров не найден')
                else:
                    # Если раздел со списком подкатегорий не найден возвращаем None 
                    return None
    except Exception as e:
        print('Возникло исключение',e)
    
    # Возвращаем словарь с основной информацией о товарах с указанием категорий, в которые они входят                    
    return goods_by_categories       

# Функция, возращающая словарь html-кодов страницы каждого товара, на вход функция принимает словарь с основной информацией о товарах
def get_html_for_all_goods(dict:dict)->dict: # На вход функция принимает словарь с основной информацией о товарах
    all_goods_codes_dict = {}
    i=1 # Вводим счётчик номера товара
    # С помощью блока try/except отлавливаем возможные исключения
    try:
    # С помощью цикла for проходимся по каждому товару
        for item in dict.values():# Проходимся по соответсвующим значениям ключей (категорий)
            for element in item.values(): # Проходимся по спискам параметров каждого товара
                link = element['Ссылка на товар']
                name = element['Название']
        # С помощью блока try/except отлавливаем возможные исключения
                try:
                        html = requests.get(link).text # С помощью get-запроса получаем html-код страницы каждого товара
        # Создаём объект BeatifulSoup для извлечения информация со страницы товара                
                        soup = BeautifulSoup(html,'lxml')
        # Извлекаем информацию о названии товара                
                        name = soup.find('title')
                        name = name.get_text().strip()
                        
        # Добавляем в словарь товаров - html-код соответсвующего товара                
                        all_goods_codes_dict[f'{i} {name}'] = html
                        
        # В случае возникновения исключения - выводим соответствующее сообщение                 
                except Exception as e:
                    logger.debug('Возникло исключение',e)
                
                i+=1    # Увеличиваем на единицу счётчик товара
            
    # В случае возникновения исключения - выводим соответствующее сообщение                 

    except Exception as e :
        logger.debug('Возникло исключение',e)
        
    # print(i)
    return all_goods_codes_dict

# Функция, принимающая на вход html код товара и возвращающая словарь с payload параметрами для каждого его подтипа 
def get_payload(html) -> dict:
    # Создаём словарь с payload параметрами для каждого подтипа
    payload = {'calcPrice':1,'amoun_input':1}
    # Создаём объект BeatifulSoup для извлечения информация со страницы товара                
    soup = BeautifulSoup(html,'lxml')
    # Если html-код корректен - приступаем к извлечению информации с сайта
    if html is not None:
        # Проходимся по соответсвующим тэгам и извлекаем информацию о Id товара
        page_wr = soup.find(class_='page-wrapper')
        if page_wr is not None:
            page_wr_in = soup.find(class_='page-wrapper__inner')
            if page_wr_in is not None:
                prod_bl = soup.find(class_='item-page product-details-block')
                if prod_bl is not None:
                    page_grid = soup.find(class_='item-page__grid')
                    if page_grid is not None:
                        item_product = soup.find('div',class_='item-page__content')
                        if item_product is not None:
                            b_bl = soup.find(class_='buy-block item-page__row property-form js-product-form actionBuy')
                            if b_bl is not None:
                                data_id = b_bl.get('data-product-id')
        # Добавляем в словарь payload Id товара
                                payload['inCartProductId'] = clear_text(data_id) # Очищаем значение Id от неенужных символов
        # Если разделы с ссответствующими тэгами найдены не будут - функция будет возвращать None    
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None    
    # Проходимся по соответсвующим тэгам и извлекаем информацию о параметре Variant товара
        if page_wr is not None:
            page_wr_in = soup.find(class_='page-wrapper__inner')
            if page_wr_in is not None:
                prod_bl = soup.find(class_='item-page product-details-block')
                if prod_bl is not None:
                    page_grid = soup.find(class_='item-page__grid')
                    if page_grid is not None:
                        item_product = soup.find('div',class_='item-page__content')
                        if item_product is not None:
                            var = soup.find('div',class_="buy-block-inner")
                            if var is not None:
                            
                                table = soup.find(class_="variants-table")
                                
                                if table is not None:
                                    type = soup.find(class_='item-page-type')
                                    
                                    if type is not None:
                                    # находим все тэги в которых содержатся подтипы данного товара   
                                            Items_page = type.find_all('tr')
                                            # Создаём список значений параметра Variant для каждого подтипа товара
                                            list_variants = []
                                            # Проходимся с помощью цикла for по всем тэгам подтипов товара
                                            for variant in Items_page:
                                            # Находим интересующий нас раздел
                                                var_item = variant.find(class_='item-page-type__item')
                                                if var_item is not None:
                                                # Извлекаем информацию о парарметре Variant каждого подтипа
                                                    var = var_item.find('input')
                                                    variant_pl = var.get('value')
                                                    # Добавляем значение параметра Variant в список значений
                                                    list_variants.append(clear_text(variant_pl))
                                                else:
                                                    return None
                                            # Добавляем в словарь payload данный список значений
                                            payload['variant'] = list_variants
    # Если разделы с ссответствующими тэгами найдены не будут - функция будет возвращать None    
                                    else:
                                        return None
                                else:
                                    return None
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
    # Если html-код неккоректный - выводим соотвествующее значение
        print('Некорректный HTML-файл')    
    # Возвращаем словарь payload с payload-параметрами конкретного товара                                    
    return payload
                                                
       
# Функция, возвращающая список словарей с детельной информацией о товарах, на вход функция принимает словарь с html-кодами каждого товара
# а также имя файла для записи данных о товарах (если пользователь захочет вывести данные в файл)            
def get_goods_detailed_info(diction:dict,*args)->list:
    
        
    i=1 # Счётчик номера товара в списке
    number = 0 # Номер строки таблицы (при записи в файл) 
    logger.debug('Запуск функции get_goods_detailed_info')
    # Создаём список словарей параметров товаров
    dict_detailed_info_goods= []
    # Создаём словарь параметров каждого товара
    dict_detailed_info_good = {}

    #Создаём файл для записи данных о товарах, если в функцию передано имя файла для записи
    if len(args) != 0:
        workbook = xlsxwriter.Workbook(f'{args[0]}.xlsx')
        # Создаём объект xlsxwriter для записи данных
        worksheet = workbook.add_worksheet()
    else:
    # Если в функцию не передано имя файла - пропускаем данный блок кода
        pass
    
    try:
        # С помощью цикла for проходимся по именам и html-кодам в словаре
        for Name,html in diction.items():
            
            
            # Создаём объект класса BeatifulSoup для извлечения информации с сайта
                soup = BeautifulSoup(html,'lxml')
            # Проходимся  с помощью цикла for по соотвествующим тэгам и извлекаем информацию о наличии подтипов у данного товара         
                page_wr = soup.find(class_='page-wrapper')
                if page_wr is not None:
                    page_wr_in = soup.find(class_='page-wrapper__inner')
                    if page_wr_in is not None:
                        prod_bl = soup.find(class_='item-page product-details-block')
                        if prod_bl is not None:
                            page_grid = soup.find(class_='item-page__grid')
                            if page_grid is not None:
                                item_product = soup.find('div',class_='item-page__content')
                                if item_product is not None:
                                    var = soup.find('div',class_="buy-block-inner")
                                    if var is not None:
                                    
                                        table = soup.find(class_="variants-table")
                                        
                                        if table is not None:
                                            type = soup.find(class_='item-page-type')
                                            
                                            if type is not None:
                                            # Находим все тэги с информацией о подтипах товара    
                                                    Items_page = soup.find_all('td',class_='item-page-type__item')
                                            # Если у товара все один подтип - то всю дальнейшую информацию будем извлекать 
                                            # непосредственно из html-кода страницы товара        
                                                    if len(Items_page) ==1:
                                                        lab = soup.find('label')
                                                        if lab is not None:
                                            # Проходимся по соответствующим тэгам и извлекаем информацию о названии, статусе и ценен товара
                                                            title = soup.find(class_='item-page-type__title variantTitle')
                                                            name = title.get_text()
                                                            status = soup.find(class_='item-panel__status')
                                                            status = status.get_text()
                                                            price = soup.find('div',class_='item-page-type__price')
                                                            price = price.get_text()
                                            # Добавляем соответсвующую информацию в словарь данного товара
                                                            dict_detailed_info_good['Название'] = clear_text(name)
                                                            dict_detailed_info_good['Статус'] = clear_text(status)
                                                            dict_detailed_info_good['Цена'] = clear_text(price)
                                                        else:
                                            # Если тэг с соответствующей информацией не найден, функция будет возвращать None
                                                            return None   
                                                    
                                            # Создаём объект класса BeatifulSoup для извлечения информации с сайта
                                                        soup = BeautifulSoup(html,'lxml')
                                            # С помощью цикла for проходимся по соответствующим тэгам и извлекаем информацию об Артикуле товара
                                                        page_wr = soup.find(class_='page-wrapper')
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    prod_bl = soup.find(class_='item-page product-details-block')
                                                                    if prod_bl is not None:
                                                                        page_grid = soup.find(class_='item-page__grid')
                                                                        if page_grid is not None:
                                                                            item_product = soup.find('div',class_='item-page__content')
                                                                            if item_product is not None:
                                                                                meta = soup.find('div',class_='item-page__sku product-code')
                                                                                if meta is not None:
                                                                                    code = meta.find('span',class_='code')
                                                                                    if code is not None:     
                                                                                        article = meta.get_text()[15:]
                                                                                        # Добавляем соответсвующую информацию в словарь данного товара
                                                                                        dict_detailed_info_good['Артикул'] = clear_text(article)
                                                                                    # В случае, если соответсвующие тэги не найдены - функция будет возвращать None
                                                                                    else:
                                                                                        return None
                                                                                else:
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else:
                                                                    return None
                                                        else:
                                                            return None
                                                                        
                                            # С помощью цикла for проходимся по соответствующим тэгам и извлекаем информацию о Старой цене товара
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    prod_bl = soup.find(class_='item-page product-details-block')
                                                                    if prod_bl is not None:
                                                                        page_grid = soup.find(class_='item-page__grid')
                                                                        if page_grid is not None:
                                                                            item_product = soup.find('div',class_='item-page__content')
                                                                            if item_product is not None:
                                                                                var = soup.find('div',class_="buy-block-inner")
                                                                                if var is not None: 
                                                                                    item_bottom=soup.find(class_='item-page__bottom')
                                                                                    if item_bottom is not None:
                                                                                        item_price = soup.find(class_='item-page__price')
                                                                                        if item_price is not None:
                                                                                            def_price = soup.find(class_='default-price')
                                                                                            if def_price is not None:
                                                                                                has_old = soup.find(class_='product-price has-old-price')
                                                                                                if has_old is not None:
                                                                                                    old_price = soup.find(class_='old-price')
                                                                                                    old_price = old_price.get_text()
                                                                                                # Добавляем в словарь данного товарар информацию о его старой цене                                                        
                                                                                                    dict_detailed_info_good['Старая цена'] = clear_text(old_price)
                                                                                                # Если  тэга, содержащего значение старой цены товара не найдено - записываем по ключу значение - 'Нет данных'
                                                                                                else:
                                                                                                    dict_detailed_info_good['Старая цена'] = 'Нет данных'
                                                                                    # В случае, если соответсвующие тэги не найдены - функция будет возвращать None
                                                                                            else:
                                                                                                return None
                                                                                        else:
                                                                                            return None
                                                                                    else:
                                                                                        return None
                                                                                else:
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else:
                                                                    return None
                                                        else:
                                                            return None
                                                                                            
                                        # С помощью цикла for проходимся по соответствующим тэгам и извлекаем информацию об изображениях товара
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    det_bl = soup.find(class_='item-page product-details-block')       
                                                                    if det_bl is not None:
                                                                        it_gr = soup.find(class_='item-page__grid')
                                                                        if it_gr is not None:
                                                                            it_gal = soup.find(class_='item-page__gallery')
                                                                            if it_gal is not None:
                                                                                sw_wr = soup.find(class_='swiper-wrapper')   
                                                                                if sw_wr is not None:
                                                                            # Находим все тэги с изображениями товара
                                                                                    images = sw_wr.find_all('img')
                                                                            # Создаём список ссылок на изображения
                                                                                    img_list = []
                                                                                    if images is not None:
                                                                            # Если изображения есть - проходимя с помощью цикла for по каждому из них
                                                                                        try:
                                                                                            for image in images:
                                                                                # Извлекаем ссылку на изображение
                                                                                                Image = image['src']
                                                                                # Добавляем ссылку на изображение в список
                                                                                                img_list.append(Image)
                                                                                        except Exception as e:
                                                                                            print('Возникло исключение',e)
                                                                                # Добавляем список ссылок в словарь данного товара
                                                                                        dict_detailed_info_good['Изображения'] = img_list
                                        # В случае, если соответсвующие тэги не найдены - функция будет возвращать None
                                                                                    else:
                                                                                        return None
                                                                                else:    
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else: 
                                                                    return None
                                                        else:
                                                            return None
                                                                        
                                                                
                                                        
                                                    # С помощью цикла for проходимся по соответствующим тэгам и извлекаем информацию о весе товара
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    prod_bl = soup.find(class_='item-page product-details-block')
                                                                    if prod_bl is not None:
                                                                        wrap_pr = soup.find(class_='wrapper product-status js-product-page')
                                                                        if wrap_pr is not None:    
                                                                            page_grid = soup.find(class_='item-page__grid')
                                                                            if page_grid is not None:
                                                                                item_product = soup.find('div',class_='item-page__content')
                                                                                if item_product is not None:
                                                                                    item_meta = soup.find(class_='item-page__meta')
                                                                                    if item_meta is not None:
                                                                                        pr_list = soup.find(class_='product-status-list')
                                                                                        if pr_list is not None:
                                                                                            ds_bl = pr_list.find('li')
                                                                                            if ds_bl is not None:
                                                                                                un_weight = ds_bl.get_text().strip()
                                                                                            # Извлекаем информацию о единице измерения веса
                                                                                                unit_weight = un_weight[-4:]
                                                                                                
                                                                                                label_weight = soup.find('span',class_='label-black weight')
                                                                                                if label_weight is not None:
                                                                                            # Извлекаем информацию о значении веса товара
                                                                                                    weight = label_weight.get_text()
                                                                                            # Добавляем информацию о весе в словарь товара
                                                                                                    dict_detailed_info_good['Вес'] = clear_text(f'{weight} {unit_weight}')
                                                                                                
                                        # В случае, если соответсвующие тэги не найдены - функция будет возвращать None

                                                                                            else:
                                                                                                return None
                                                                                        else:
                                                                                            return None
                                                                                    else:
                                                                                        return None
                                                                                else:
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else:
                                                                    return None
                                                        else:
                                                            return None
                # С помощью цикла for проходимся по соответствующим тэгам и извлекаем информацию об описании товара
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    det_bl = soup.find(class_='item-page product-details-block')       
                                                                    if det_bl is not None:
                                                                        it_page = soup.find(class_='item-page__text youtube-video-content')
                                                                        if it_page is not None:
                                                                            desc_items_p = it_page.find_all('p')
                                                                            desc_items_li = it_page.find_all('li')
                                                                            if desc_items_p is not None:
                                                                                desc= ''
                                                                                try:
                                                                                    for item in desc_items_p:
                                                                                        
                                                                                        desc_item=item.get_text()
                                                                                        desc+= clear_text(desc_item)
                                                                                except Exception as e:
                                                                                    print('Возникло исключение', e)
                                                                            desc = ''
                                                                            if desc_items_li is not None:
                                                                                try:
                                                                                    for item in desc_items_li:
                                                                                        
                                                                                        desc_item=item.get_text()
                                                                                        desc+= clear_text(desc_item)    
                                                                                except Exception as e:
                                                                                    print('Возникло исключение', e)
                                                                                desc = desc.replace('Описание','')
                                                                                # Добавляем информацию в словарь товара
                                                                                dict_detailed_info_good['Описание'] = desc.replace('\\n','').strip()
                # В случае, если соответсвующие тэги не найдены - функция будет возвращать None

                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else:
                                                                    return None
                                                        else:
                                                            return None
                                                                
                                                        # добавляем словарь товара в общий список словарей                        
                                                        dict_detailed_info_goods.append(dict_detailed_info_good)
                                                        # Блок вывода информации о товаре
                                                        print(f'Товар № {i}') 
                                                        # Записываем в переменные соответсвующие значения параметров товара
                                                        NAME = dict_detailed_info_good['Название']
                                                        ARTICLE =dict_detailed_info_good['Артикул']
                                                        PRICE =  dict_detailed_info_good['Цена'] 
                                                        OLD_PRICE = dict_detailed_info_good['Старая цена']
                                                        IMAGE = dict_detailed_info_good['Изображения']
                                                        WEIGHT = dict_detailed_info_good['Вес']
                                                        STATUS = dict_detailed_info_good['Статус']
                                                        DESCRIPT = dict_detailed_info_good['Описание']
                                                        # Вывдим информацию в консоль
                                                        print(
                                                            # f'{clear_text(Name)}:\n'
                                                            f'Название: {NAME}\n'
                                                            f'Артикул: {ARTICLE}\n'
                                                            f'Цена: {PRICE}\n'
                                                            f'Старая цена: {OLD_PRICE}\n'
                                                            f'Изображения: {IMAGE}\n'
                                                            f'Вес: {WEIGHT}\n'
                                                            f'Статус: {STATUS}\n'
                                                            f'Описание: {DESCRIPT}\n'
                                                            ) 
                                                        # Обнулям словарь товара
                                                        dict_detailed_info_good.clear() 
                                                        # Перезаписываем данные в нужном порядке для вывода данных в файл 
                                                        dict_detailed_info_good = {'Название':NAME,'Артикул':ARTICLE,'Цена':PRICE,'Старая цена':OLD_PRICE,
                                                                                'Изображения': str(IMAGE),'Вес':WEIGHT,'Статус':STATUS,'Описание':DESCRIPT}
                                                        print()   
                                                        
                                                        # Если в исходную функцию было передано имя файла для записи
                                                        if len(args) !=0:
                                                        # С помощью цикла for проходимся по значениям параметров товара
                                                            for param,value in dict_detailed_info_good.items():
                                                        # Делаем запись в соответсвующие ячейки таблицы        
                                                                worksheet.write(number,0,param)
                                                                worksheet.write(number,2,value)
                                                                number+=1
                                                        else:
                                                        # Если в функцию не передано имя файла - пропускаем данный блок кода
                                                            pass    
                                                        # Увеличиваем на единицу номер товара                                                                         
                                                        i+=1 
                                                    else:
                                                        # Если товар имеет подтипы - выводим соответствующее сообщение
                                                        print(f'Товар № {clear_text(Name)} имеет подтипы')
                                                        # Извлекаем информацию об изображениях товара (полностью аналогично товару без подтипов)
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    det_bl = soup.find(class_='item-page product-details-block')       
                                                                    if det_bl is not None:
                                                                        it_gr = soup.find(class_='item-page__grid')
                                                                        if it_gr is not None:
                                                                            it_gal = soup.find(class_='item-page__gallery')
                                                                            if it_gal is not None:
                                                                                sw_wr = soup.find(class_='swiper-wrapper')   
                                                                                if sw_wr is not None:
                                                                                    images = sw_wr.find_all('img')
                                                                                    img_list = []
                                                                                    if images is not None:
                                                                                        try:
                                                                                            for image in images:
                                                                                                Image = image['src']
                                                                                                img_list.append(Image)
                                                                                        except Exception as e:
                                                                                            print('Возникло исключение',e)
                                                                                        dict_detailed_info_good['Изображения'] = img_list
                                                                                        
                                                                                    else:
                                                                                        return None
                                                                                else:
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else:
                                                                    return None
                                                        else:
                                                            return None
                                                                                    
                                                        # Извлекаем информацию об описании товара (полностью аналогично товару без подтипов)
                                                        if page_wr is not None:
                                                                page_wr_in = soup.find(class_='page-wrapper__inner')
                                                                if page_wr_in is not None:
                                                                    det_bl = soup.find(class_='item-page product-details-block')       
                                                                    if det_bl is not None:
                                                                        it_page = soup.find(class_='item-page__text youtube-video-content')
                                                                        if it_page is not None:
                                                                            
                                                                            desc_items_p = it_page.find_all('p')
                                                                            desc_items_li = it_page.find_all('li')
                                                                            if desc_items_p is not None:
                                                                                desc= ''
                                                                                try:
                                                                                    for item in desc_items_p:
                                                                                        
                                                                                        desc_item=item.get_text()
                                                                                        desc+= clear_text(desc_item)
                                                                                except Exception as e:
                                                                                    print('Возникло исключение', e)
                                                                            
                                                                            if desc_items_li is not None:
                                                                                try:
                                                                                    for item in desc_items_li:
                                                                                        
                                                                                        desc_item=item.get_text()
                                                                                        desc+= clear_text(desc_item)    
                                                                                except Exception as e:
                                                                                    print('Возникло исключение', e)
                                                                                desc = desc.replace('Описание','')
                                                                                dict_detailed_info_good['Описание'] = desc.replace('\\n','').strip()
                                                                                
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                                else:
                                                                    return None
                                                        else:
                                                            return None
                                                                                
                                                        # Извлекаем информацию о ссылке на страницу товара( необходимой для post-запроса)
                                                        if page_wr is not None:
                                                            page_wr_in = soup.find(class_='page-wrapper__inner')
                                                            if page_wr_in is not None:
                                                                    det_bl = soup.find(class_='item-page product-details-block')       
                                                                    if det_bl is not None:
                                                                        wr_pr = soup.find(class_='wrapper product-status js-product-page')
                                                                        if wr_pr is not None:
                                                                            path = soup.find(class_='item-page__pathway')
                                                                            if path is not None:
                                                                                path_list = soup.find('ul',class_='pathway__list') 
                                                                                if path_list is not None:
                                                                                    p_l=soup.find('a',class_='last-crumb')
                                                                                    if p_l is not None:
                                                                                        
                                                                                        link = p_l.get('href').strip()
                    # В случае, если соответсвующие тэги не найдены - функция будет возвращать None

                                                                                    else:
                                                                                        return None
                                                                                else:
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                        else:
                                                                            return None
                                                                    else:
                                                                        return None
                                                            else:
                                                                return None
                                                        else:
                                                            return None
                                                                                        
                                                        # Извлекаем информацию о единице измерения веса товара     
                                                        if page_wr is not None:
                                                            page_wr_in = soup.find(class_='page-wrapper__inner')
                                                            if page_wr_in is not None:
                                                                    prod_bl = soup.find(class_='item-page product-details-block')
                                                                    if prod_bl is not None:
                                                                        wrap_pr = soup.find(class_='wrapper product-status js-product-page')
                                                                        if wrap_pr is not None:    
                                                                            page_grid = soup.find(class_='item-page__grid')
                                                                            if page_grid is not None:
                                                                                item_product = soup.find('div',class_='item-page__content')
                                                                                if item_product is not None:
                                                                                    item_meta = soup.find(class_='item-page__meta')
                                                                                    if item_meta is not None:
                                                                                        pr_list = soup.find(class_='product-status-list')
                                                                                        if pr_list is not None:
                                                                                            ds_bl = pr_list.find('li')
                                                                                            if ds_bl is not None:
                                                                                                unit_weight = ds_bl.get_text()
                                                                                                unit_weight = clear_text(unit_weight)[-4:]
                    # В случае, если соответсвующие тэги не найдены - функция будет возвращать None

                                                                                            else:
                                                                                                return None
                                                                                        else:
                                                                                            return None
                                                                                    else:
                                                                                        return None
                                                                                else:
                                                                                    return None
                                                                            else:
                                                                                return None
                                                                    else:
                                                                        return None
                                                            else:
                                                                return None
                                                        else:
                                                            return None
                                                                            
                                                    # С помощью функции get_payload получаем словарь с payload параметрами товара                                     
                                                                        
                                                        payload = get_payload(html)
                                                        # Извлекаем из данного словаря список со зачениями параметра Variant
                                                        list_var = payload['variant']
                                                        # Задаём начальный номер подтипа
                                                        type_num=1
                                                        try:
                                                            # С помощью цикла for проходися по списку значений variant
                                                            for var in list_var:
                                                            # Выводим сообщение о номере подтипа
                                                                print(f'Подтип № {type_num}')
                                                            # Записываем в словарь текущее значение параметра Variant    
                                                                payload['variant'] = var
                                                            # От правляем post-запрос с указанием словаря payload в качестве данных и получаем html-код отклика на данный запрос    
                                                                response = requests.post(link,data=payload).text
                                                                # Перевоодим текстовое значение отклика на post-запрос в формат json
                                                                resp = json.loads(response)
                                                                # Извлекаем информацию о статусе по соответсвующему ключу
                                                                status = resp['data']['count_layout']
                                                                # С помощью метода compile класса re извлекаем необходимые символы
                                                                r = re.compile("[а-яА-Я' ']+")
                                                                result = list(filter(r.match,status))
                                                                # Объединяем их в единую строку
                                                                status = ''.join(result)
                                                                # В переменные записываем значения соответствующих параметров данного подтипа товара,
                                                                # извлекая их из json словаря по соответствующим ключам
                                                                NAME = clear_text(resp['data']['title'])
                                                                ARTICLE = clear_text(resp['data']['code'])
                                                                PRICE =  clear_text(resp['data']['real_price']) + ' руб.'
                                                                OLD_PRICE = clear_text(resp['data']['old_price']) if resp['data']['old_price'] != '0 руб.' else 'Нет данных'
                                                                WEIGHT =  clear_text(resp['data']['weight']) + ' кг'  if resp['data']['weight'] != '0' else 'Нет данных'
                                                                STATUS = clear_text(str(status))
                                                                IMAGE = dict_detailed_info_good['Изображения']
                                                                DESCRIPT = dict_detailed_info_good['Описание']
                                                                # Обнуляем словарь, чтобы записать значения в нужном порядке (в слуае, если требуется запись в файл)
                                                                dict_detailed_info_good.clear()
                                                                dict_detailed_info_good['Название'] =  NAME 
                                                                dict_detailed_info_good['Артикул'] = ARTICLE
                                                                dict_detailed_info_good['Цена'] = PRICE 
                                                                dict_detailed_info_good['Старая цена'] = OLD_PRICE
                                                                dict_detailed_info_good['Изображения'] = str(IMAGE)
                                                                dict_detailed_info_good['Вес'] = WEIGHT
                                                                dict_detailed_info_good['Статус'] = STATUS
                                                                dict_detailed_info_good['Описание'] = DESCRIPT
                                                                # Выводим информацию о подтипе товара в консоль
                                                                print(
                                                                f'Название: {NAME}\n'
                                                                f'Артикул: {ARTICLE}\n'
                                                                f'Цена: {PRICE}\n'
                                                                f'Старая цена: {OLD_PRICE}\n'
                                                                f'Изображения: {IMAGE}\n'
                                                                f'Вес: {WEIGHT}\n'
                                                                f'Статус: {STATUS}\n'
                                                                f'Описание: {DESCRIPT}\n'
                                                                )   
                                                                print()
                                                                # Если в функцию передано имя файла для записи
                                                                if len(args) !=0:
                                                                # Осуществляем запись данных
                                                                    worksheet.write((number),1,f'Подтип № {type_num}')
                                                                    try:
                                                                    # C помощью цикла for проходимся по значениям в словаре товара
                                                                        for param,value in dict_detailed_info_good.items():
                                                                    # Записываем данные в соответствующую ячейку таблицы        
                                                                            worksheet.write(number,0,param)
                                                                            
                                                                            worksheet.write(number,2,value)
                                                                    # Увеличиваем номер строки на единицу
                                                                            number+=1
                                                                    except Exception as e:
                                                                        print('Возникло исключение',e)
                                                                # Увеличиваем номер подтипа на единицу    
                                                                    type_num+=1
                                                                else:
                                                                # Если в функцию не было передано имя файла для записи, просто увеличиваем номер подтипа
                                                                # на единицу без записи 
                                                                    type_num+=1
                                                        except Exception as e:
                                                            print('Возникло исключение',e)
                                                        # Увеличиваем номер товара на единицу        
                                                        i+=1
                                                        # Добавляем словарь с информацией о товаре в общий список товаров 
                                                        dict_detailed_info_goods.append(dict_detailed_info_good) 
                                            else:
                                                return None
                                        else:
                                            return None
                                    else:
                                        return None
                                else:
                                    return None
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
                
    except Exception as e:
        print('Возникло исключение',e)            
            
     # Если в функцию передано имя файла для записи
    if len(args) !=0:
    # Заканчиваем считывание файла
        workbook.close() 
    else:
    # Если в функцию не передано имя файла - пропускаем данный блок кода
        pass     
    # Возвращаем список словарей данных о товарах                                
    return dict_detailed_info_goods






   



