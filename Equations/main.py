# Импортируем необходимые библиотеки
import tkinter as tk # Библиотека tkinter для создания графического инртерфейса GUI
import tkinter.messagebox as tkm # Модуль messagebox для вывода диалоговых сообщений
import math # Модуль math для работы с математическими функциями и выражениями
from Functions.functions import calculate_discrim,calculate_roots # Функции, которые будут выполнять необходимые вычисления

# Создаём класс GUI, внутри котого описываем элементы графического интерфейса нашей программы
class GUI:
    def __init__(self):
# Создаём родительский виджет приложения, внутри которого будут располагаться все элементы интерфейса
        self.main_window = tk.Tk()
# Даём название главному окну программы
        self.main_window.title('Программа для решения уравнений')
        
# Создаём первый виджет надписи 'квадратное уравнение'
        self.square_label = tk.Frame(self.main_window) # Помещем его в рамку главного виджета
        self.square_label = tk.Label(self.main_window,relief='raised',borderwidth=3,text='Квадратное уравнение')# Создаём соответствующую
        #виджет-надпись

# Создаём виджеты (рамки) для отображения результатов вычислений дискриминанта и корней квадратного уравнения        
        self.discrim = tk.Frame(self.main_window)
        
        self.roots = tk.Frame(self.main_window)
# Создаём рамку для виджетов очистки результатов и выхода из программы        
        self.clean_and_exit = tk.Frame(self.main_window)
# Создаём объекты StringVar(меняющаяся строка) для хранения результатов вычислений соответствующих величин       
        self.value_discrim = tk.StringVar()
        self.value_x1 = tk.StringVar()
        self.value_x2 = tk.StringVar()

# Создаём виджет-рамку expresion, внутри которого будут находиться элементы выражения квадратного уравнения
        self.expression = tk.Frame(self.main_window,relief='raised') 
        self.expression_1 = tk.Entry(self.expression,relief='raised',borderwidth=2,width=0,show=True)
# Создаём виджеты-элементы выражения                
        self.expression_2 = tk.Label(self.expression,relief='raised',text='X2 + ')
        self.expression_3 = tk.Entry(self.expression,relief='raised',borderwidth=2,width=0)
        self.expression_4 = tk.Label(self.expression,relief='raised',text='X +')
        self.expression_5 = tk.Entry(self.expression,relief='raised',borderwidth=2,width=0)
        self.expression_6 = tk.Label(self.expression,relief='raised',text='= 0')
# Создаём виджет кнопку для запуска решения нашего квадратного уравнения
        self.expression_calc = tk.Button(self.expression,width=6,text='Решить',command=self.calc_result)

# Создаём виджет для хранения результатов вычислений дискриминанта квадратного уравнения        
        self.discrim_label = tk.Label(self.discrim,borderwidth=3,relief='raised',width=3,text=' D =')
        
        self.discrim_result = tk.Button(self.discrim,borderwidth=3,relief='raised',width=3,textvariable=self.value_discrim)
       
# Создаём виджет для хранения результатов вычисления корней квадратного уравнения        
        self.roots_1_lab = tk.Label(self.roots,width=0,relief='raised',text = 'x1 =')
        
        self.roots_1_result = tk.Button(self.roots,width=0,relief='raised',textvariable=self.value_x1)
        self.roots_2_lab = tk.Label(self.roots,width=0,relief='raised',text = 'x2 =')
        
        self.roots_2_result = tk.Button(self.roots,width=0,relief='raised',textvariable=self.value_x2)
# Создаём виджет-копки для очистки данных и выхода из программы
        self.cleaner = tk.Button(self.clean_and_exit,relief='raised',width = 8,command=self.clean,text='Очистить')
        
        self.exit = tk.Button(self.clean_and_exit,relief='raised',width=8,command=self.quit,text = 'Выход')
# Последовательно размещаем все вышеописанные виджеты на панели нашей программы        
        self.square_label.pack(side='top')
        self.expression.pack(side='top',padx=5,pady=25) 
        self.expression_1.pack(side='left') 
        self.expression_2.pack(side='left')
        self.expression_3.pack(side='left')
        self.expression_4.pack(side='left')
        self.expression_5.pack(side='left')
        self.expression_6.pack(side='left')
        self.expression_calc.pack(side='left',padx=15)
        
        self.discrim.pack(side='top')
        self.discrim_label.pack(side='left')
        self.discrim_result.pack(side='left')
        
        self.roots.pack(side='top',padx=5,pady=30)
        self.roots_1_lab.pack(side='left')
        self.roots_1_result.pack(side='left')
        self.roots_2_lab.pack(side='left')
        self.roots_2_result.pack(side='left')
 
        self.clean_and_exit.pack(side = 'top',padx = 5,pady=40)
        self.cleaner.pack(side='left',padx = 1,pady=40)
        self.exit.pack(side='right',padx = 10,pady=40)
       
# Запускаем нашу программу
        tk.mainloop()

# Функция, отображающая результаты вычислений       
    def calc_result(self):
        self.a = self.expression_1.get() # В переменную a данного класса записываем значение коэффициента a, вводимое пользователем в окно виджета
        self.b =self.expression_3.get()  # В переменную b данного класса записываем значение коэффициента b, вводимое пользователем в окно виджета
        self.c =self.expression_5.get()  # В переменную c данного класса записываем значение коэффициента c, вводимое пользователем в окно виджета
# Если значение для коэффициента a не введено, то по умолчанию будем считать его равным 1
        if self.a == '':
            self.a = '1'
# Вычисляем значение дискриминанта
        D = calculate_discrim(self.a,self.b,self.c)
        self.value_discrim.set(D)
# Если дискриминант больше либо равен нулю, то вычисляем корни уравнения
        if D >=0 :
            x1 = calculate_roots(self.a,self.b,self.c)['x1']
            self.value_x1.set(x1)
            
            x2 = calculate_roots(self.a,self.b,self.c)['x2']
            self.value_x2.set(x2)
# Если дискриминант - меньшу нуля, то выводим сообщение " Корней нет"
        else:
            tkm.showinfo('Результат: ','Корней нет!')
# Функция, очищаяющая результаты вычислений    
    def clean(self):
        self.value_discrim.set('')
        self.value_x1.set('')
        self.value_x2.set('')
# Функция, закрывающая программу    
    def quit(self):    
        self.main_window.destroy()
        
# Создаём объект класса GUI         
if __name__=='__main__':
    my_gui = GUI()
        