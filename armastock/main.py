# Программа для парсинга данных с сайта armastock.ru

# Точка входа в проект (файл запуска  программы)

# Импортируем необходимые функции и словари из модулей программы

from Dictionaries.dictionaries import dict_site_code
from Functions.functions import (get_categ_info_by_level,get_categories,get_dict_goods_by_categ
                                 ,get_html_for_all_goods,get_goods_detailed_info,get_payload)
from Menu.menu import main_menu,categories_menu,goods_menu,record_menu,write_menu,return_menu
from Info.Info import info

# Функция запуска программы
def main():
    
    print('Добро пожаловать на сайт armastock.ru\n')
    # Инициализируем переменную choice, которая будет отвечать за выбор опции пользователем в главном меню
    choice = ''
    
    try:
    # Запускаем цикл While, который будет работать пока пользователь не выйдет из программы    
        while choice !='4':
        # Запускаем главное меню     
            main_menu()
        # Считываем значение, вводимое пользователем для переменной choice
            choice = input()
        # Если выбрана опция "Выбрать товар"    
            if choice == '1':
        # Инициализируем переменную choice_2 для выбора категории товара
                choice_2 = ''
        # Получаем список главных категорий
                dict_categ = get_categories(dict_site_code)
        # Выводим меню со списком главных категорий
                dict_main_categ = categories_menu(dict_categ)
        # Считываем значение, вводимое пользователем для выбора категории товара
                choice_2 = input()
                try:
        # Запускаем цикл while, который будет выполняться пока пользователь не выйдет в главное меню
                    while choice_2 != '0':
        # Получаем словарь с html-кодом выбранной категории                 
                        categ_lower_level = {'categ_code': dict_main_categ[int(choice_2)]}
                        try:
        # Получае список категорий на 1 уровень ниже
                            dict_lower_categ = get_categories(categ_lower_level)
        # Передаём в переменную dict_main_categ словарь с html-кодами низшей категории
                            dict_main_categ = categories_menu(dict_lower_categ)
        # Считываем значение, введённое пользователем при выборе категории и повторяем цикл
                            choice_2 = input()
                        except:
        # Если раздел с подкатегориями не найден - переходим к блоку вывода товаров
                            choice_3 = '' # Инициализируем переменную choice_3, в которой будет хранить значение номера товара, 
                                          # выбранного пользователем
                            print('Список товаров: ')
        # Получаем словарь с основной информацией о товарах
                            dict_goods = get_dict_goods_by_categ(categ_lower_level)
        # Выводим меню товаров, получая словарь с html-кодом страницы каждого товара
                            dict_htmls = goods_menu(dict_goods)
        # Считываем номер товара, выбранного пользователем
                            choice_3 = input()
                            try:
        # Запускаем цикл while, который будет работать пока пользователь не выйдет в главное меню или не выйдет из программы
                                while choice_3 != '0':
        # Получаем html-код выбранного товара
                                    html_good =  dict_htmls[int(choice_3)]
        # Формируем словарь с html-кодом данного товара
                                    dict_good = {str(choice_3):html_good}
        # Выводим меню записи, спрашивая пользователя о необходимости записать данные в файл
                                    record_menu()
        # Считываем номер выбранной опции
                                    choice_to_write = input()
        # Если пользователь выбрал запись
                                    if choice_to_write == '1':
        # Запрашиваем имя файла
                                        write_menu()
                                        filename = input()
        # Выводим детальную информацию о товаре в консоль, записывая данные в Excel файл
                                        get_goods_detailed_info(dict_good,filename)
        # Если пользователь отказался от записи    
                                    elif choice_to_write == '2':
        # Выводим информацию в консоль без записи
                                        get_goods_detailed_info(dict_good)
                                    else:
        # Если пользватель нажал другую клавишу - выходим из программы
                                        print('До свидания!')
                                        return
        # Снова отображаем меню товаров и считываем номер опции, вводимый пользователем                                
                                    goods_menu(dict_goods)
                                    choice_3 = input()
                            except Exception as e:
                                print('Возникло исключение', e)
                            break
                except Exception as e:
                    print('Возникло исключение', e)   
        # Если в главном меню выбрана опция №2 - выводим информацию о сайте    
            elif choice == '2':
                print(info)
        # Если в главном меню выбрана опция №3
            elif choice == '3':
            # Получаем словарь с категориями 1-го уровня
                dict_categories_1_names = get_categ_info_by_level(dict_site_code)
            # Получаем словарь с категориями 2-го уровня
                dict_categories_2_names = get_categ_info_by_level(dict_categories_1_names)
            #  Получаем словарь с категориями 3-го уровня
                dict_categories_3_names = get_categ_info_by_level(dict_categories_2_names)
            #  Получаем общий словарь категорий всех уровней

                dict_all_categories = {**dict_categories_1_names,**dict_categories_2_names,**dict_categories_3_names}

            #    Получаем словарь c основной информаций обо всех товарАХ с указанием категорий, в которые они входят

                all_goods_base_info =get_dict_goods_by_categ(dict_all_categories)

            #    Получаем словарь с html-кодами для каждого товара
                all_html_for_goods = get_html_for_all_goods(all_goods_base_info)


                # Выводим меню записи, спрашивая пользователя о необходимости записать данные в файл
                record_menu()
                # Считываем номер выбранной опции
                choice_all_goods = input()
                try:
                # Запускаем цикл while, который будет работать пока пользователь не выйдет в главное меню или не выйдет из программы
                    while choice_all_goods != '0':
                # Если пользователь выбрал запись            
                        if choice_all_goods == '1':
                # Запрашиваем имя файла
                            write_menu()
                            filename = input()
                #  Получаем словарь с детальной информацией обо всех товарах и записываем данные в Excel файл
                            get_goods_detailed_info(all_html_for_goods,filename)
                            
                        elif choice_all_goods == '2':
                #  Получаем словарь с детальной информацией обо всех товарах без записи данных в Excel файл
                            get_goods_detailed_info(all_html_for_goods)
                # Если пользователь вводит другую клавишу - выходим из программы
                        else:
                            print('До свидания!')
                            return
                # Запускаем меню возврата в главное меню, запрашивая у пользователя решение
                        return_menu()
                        choice_all_goods = input()
                except Exception as e:
                    print('Возникло исключение', e)
        # Если в главном меню пользватель выбирает опцию № 4 - выходим из программы
            elif choice == '4':
                print('До свидания!')
                return 
            else:
                print('\nВведите корректное значение!\n')
            
    except Exception as e:
        print('Возникло исключение', e)

# Запускаем главную функцию
if __name__ == '__main__':
    main()

    
    
    
