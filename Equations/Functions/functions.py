import tkinter.messagebox as tkm # Модуль messagebox для вывода диалоговых сообщений
import math  # Модуль math для работы с математическими функциями и выражениями

# Функция, вычисляющая дискриминант
def calculate_discrim(a,b,c)->float:
    a = float(a)
    b = float(b)
    c = float(c)
    D = math.pow(b,2) - 4*a*c
    return D
   
# Функция, вычисляющая корни квадратного уравнения
    
def calculate_roots(a,b,c)->dict:
  # Переводим переменные из строкового типа в тип числа с плавающей точкой
    a = float(a) 
    b = float(b)
    c = float(c)
  # Блоком try/except - ловим возможные исключения 
    try:
      D = math.pow(b,2) - 4*a*c
      x1 = (-b+math.sqrt(D))/(2*a)
      x2 = (-b-math.sqrt(D))/(2*a)
      return {'x1':x1,'x2':x2}
    except:
        tkm.showinfo('Корней нет!')
        return None