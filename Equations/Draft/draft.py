import os
import shutil
import tkinter
import tkinter.messagebox as tkm

# dict = {"u":"45","y":"12","o":"89"}

# for i in dict:
#     print("{}:{}".format(i,dict[i]))
    
# list_1 = [78,4,7,6]

# # print(dict.items())
# for k,v in dict.items():
#     print(k,v,end=" ")
    
# maj = {"hjk","bjkl"}
# print()
# maj.add("hjk2")
# print(maj)

# a = set(list_1)
# print(a)

# lis = [it for it in range(50)]
# print(lis)

# class Cat:
#     name = None
#     age = None
#     color = None
    
#     def set_data(self,name,age,color=None):
#         self.name = name
#         self.age = age
#         self.color = color
   
#         print("Имя : ",self.name,"Возраст :", self.age,"Цвет:",self.color)
# Cat1 = Cat()
# Cat1.set_data("Барсик",5,"Black")
# # Cat1.get_data()
# Cat2 = Cat()
# Cat2.set_data("Мурзик",3)
# # Cat2.get_data()

# class Cat:
#     name = None
#     age = None
#     color = None
    
#     def __init__(self,name=None,age=None,color=None):
#         self.name = name
#         self.age = age
#         self.color = color
#         print("Имя : ",self.name, ";","Возраст :", self.age, ";","Цвет:",self.color)
    
# Cat1 = Cat("Барсик",5)

# Cat2 = Cat("Мурзик")

# func = lambda x,y: x*y
# print(func(4,5))

with open(r"C:\Users\DNS\Desktop\Git works\Pyth\Hello.txt","r") as file:
    a= file.read()
print(a)
# # file.writelines("fesfs")
# # file.writelines("\n")
# # file.writelines("Sun")
# # file.writelines("\n")
# # file.writelines("Day")
# file.close()

# for i in range(1,10):
#     if i == 4:
#         continue
#     print(i)
    
# list1 = [1,2,3,4,5]

# list2 = [it*2 for it in list1]

# print(list2)
    
    
# try:
#     for i in range(7,-3,-1):
        
#         print(round(5/i,2))
    
# except ZeroDivisionError:
#     print(f"Обнаружено деление на ноль при i = {i}")


# import random
# set1 = [ random.randint(1,9) for item in range(7)]
# set2 = [random.randint(1,7) for item in range(9)]

# print(set1)
# print(set2)

# a = set(set1)
# b = set(set2)
# print(sorted(a.intersection(b)))    
# n = int(input())
# def divide(m):
#     m = m//2
#     if m == 1:
#         return 1
#     else:
#         return  divide(m)+m
# print(divide(16))

   
# def count_nums1(tuple_a: tuple) -> int:
#      count = 0
#      for i in range(1, len(tuple_a) - 1):
#          if tuple_a[i] > tuple_a[i - 1] and tuple_a[i] > tuple_a[i + 1]:
#             count += 1
#      return sum([1 for i in range(1, len(tuple_a) - 1) if tuple_a[i] > tuple_a[i - 1] and tuple_a[i] > tuple_a[i + 1]])
# print(count_nums1((1,5,6,7,4,9,1,5,2)))    
# def sum_divisors(num: int) -> int:
#     sum_res = 1
#     sq_num = num ** 0.5
#     if sq_num == int(sq_num):
#         sum_res += int(sq_num)
#         for div in range(2, int(sq_num)):
#             if num % div == 0:
#                 sum_res += div + num // div
#     else:
#         for div in range(2, int(sq_num) + 1):
#             if num % div == 0:
#                 sum_res += div + num // div
#     return sum_res


# def find_pairs(k: int) -> None:
#     for num_1 in range(2, k + 1):
#         num_2 = sum_divisors(num_1)
#         if num_1 == sum_divisors(num_2) and num_1 < num_2 < k:
#             print(num_1, num_2)

# find_pairs(300)

# d = int(input("Введите разность прогрессии "))
# a1 = int(input("Введите первый член "))
# n= int(input("Введите количество членов "))
# print(*[a1+d*(i-1) for i in range(1,n) ])

# min = int(input("Введите мин предел "))
# max = int(input("Введите макс предел "))

# list1 = [1,45,23432,5,4,1,864,53,31,3,1,8]


# def index(Minim, Maxim,list)->int:
#     list2=[]
#     count = 0
#     for el in list:
#         if el>=Minim and el<=Maxim:
#             list2.append(count)
#         count+=1
#     return list2
# print(index(min,max,list1))

# _______________________________________________

# import matplotlib.pyplot as plt

# def main():
#     left_edge = [0,10,20,30,40]
    
#     heights = [100,200,300,400,500 ]
#     plt.bar(left_edge,heights)
#     plt.show()
# def main1():
#     x_coord = [1,4,6,8]
#     y_coord = [2,3,9,7]
    
#     plt.title("График")
#     plt.xlabel("Предложение")
#     plt.ylabel("Спрос")
#     plt.xticks(x_coord,["2015","2017","2018","2019"])
#     plt.yticks(y_coord,["5$","7$","8$","6$"])
#     plt.plot(x_coord,y_coord)
#     plt.show()


# main()
# main1()
# ___________________________________________________________
# c = lambda x,y : x+y
# print(c(5,6))

# a = [1,2,3,4,5,6,7,8,10,12]

# for i in range(len(a)):
#     if a[i]%2==0:
#         c.append(a[i])
# for i in range(0,len(c)-1,2):
#         print(f"{c[i],c[i+1]}")
#         print()

# c = lambda x: print((x,x**2),end=" ")
# def even():
#     for i in range(0,len(a)):
#             if a[i]%2==0:
#                 c(a[i])
# even()

# list ="2,3,5,9"

# a= list.split(",")
# for el in a:
#     el = int(el)
# print([int(el)*2 for el in a])

# list1 = [3,5,8,9]
# print(list1)

# list2 = list(map(lambda x:x*3,list1))
# print(list2)
# ___________________
# list0 ="2,3,5,9,19,369,45"
# list2 = list0.split(",")
# print(list2)
# list1 = list(map(int,list2))
# print(list1)

# list3 = list(filter(lambda x: x%10==9,list1))
# print(list3)

# users = ["user1","user2","user3"]
# nums = ["_01","_02","_03"]

# _______________________
# lis = []
# for i in range(len(users)):
#     lis.append((users[i],nums[i]))
# print(lis)

# ls = list(zip(users,nums))
# print(ls)

# print(dict(enumerate(users)))

# color = ["120994"]
# with open("text.txt","a") as data:
#     data.writelines(color)

# os.chdir("C:/Users/DNS/Desktop/Git works")
# print(os.getcwd())
# print(os.path.basename("C:/Users/DNS/Desktop/Git works/text.txt"))
# print(os.path.abspath("text.txt"))

# shutil.copyfile("C:/Users/DNS/Desktop/Git works/text.txt","C:/Users/DNS/Desktop/Git works/data.txt")
# a = [1,3,4,"7",6,"9",6,4,7,46,2,56]
# print(a[60])
# f= lambda x:x%2==0
# for el in a:
#     if f(el):
#         print(el)
# print(a)
# # res_list = list(map(lambda x:x%2==0,a))
# # print(res_list)
# res_list = list(map(int,a))
# print(res_list)

# users = ["ghj","gat","vhj,"]
# nums=[1,2,3]
# list_new = list(zip(nums,users))
# print(list_new)
# import math
# list_of_orbits = [(2,3),(5,7),(6,9)]
# ls=[]
# for i in range(len(list_of_orbits)):
#     ls.append(math.pi*list_of_orbits[i][0]*list_of_orbits[i][1])
# maxim = max(ls)
# print(ls)
# print(maxim)

# import pandas as pd
# df = pd.read_csv("C:/Users/DNS/Desktop/Git works/Pyth/My_works/List1.csv")
# df.head()
# df.tail(n=1)
# df.shape
# import seaborn as sn
# sn.barplot

# my_string = input("Введите строку\n")

# if my_string.endswith("d"):
#     print("Да, является")
# else:
#     print("Нет, не является")

# a = [1,5,6,7,6]
# count=0
# for el in a:
#     count+=1
# b=tuple(a)
# print(a)
# dict = {1:[1,5,3],"2":(1,5),2:{2,3}}
# c=tuple(dict)
# print(c)
# print({c})
# print(dict.popitem())
# print(dict)

# Работа с классами
# class Cars:
    
#     def __init__(self,Model=None,Color=None):
#         self.Color = Color
#         self.Model = Model
#         print(f"Модель: {self.Model} ; Цвет: {self.Color}")
#     def get(wheel):
#             print()
#     def set_data(self):
#         number = 12
#         print(number*3)
# Car1 = Cars("BMW","Blue")
# Car2 = Cars("Audi","Red")

# class Taxi(Cars):
#     def __init__(self, Model=None, Color=None):
#         super().__init__("Lexus","Pinky")
# Car3 = Taxi()  
# Car4 = Cars("Seadan","Black")


# a = int(input())


# def Fact(n):
#     for i in range(n,0,-1):
#         if (i==1):
#             return 1
#         else:
#             return i*Fact(i-1)
# print(Fact(a))


# def message(m):
    
#     for i in range(m,0,-1):
#         if (i==1):
#             return "Это рекурсия "
        
#         else:
#             return "Это рекурсия" + "\n"+message(m-1)

# print(message(5))  


# def message(times= int(input())):
#     if times>0:
        
#         print( "Это рекурсия")
#         message(times-1)
# message()

# Нахождение НОД двух чисел 

# def nod(a,b):
   
#     for i in range(2,a+1):
#         if  a%i==0 and b%i==0:
#              maxim = i
#     return maxim
# print(nod(24,24))
# Создание первой программы с GUI

# class MyGUI:            
#     def __init__(self):
        
#        self.main_window = tkinter.Tk()
       
#        self.main_window.title("Мой первый GUI") 
       
#        self.top_frame= tkinter.Frame(self.main_window)
#        self.bottom_frame = tkinter.Frame(self.main_window)
       
#        self.label1 = tkinter.Label(self.main_window,borderwidth=7,relief="raised",text="Какой-то текст")   
#        self.label2 = tkinter.Label(self.main_window,borderwidth=10,relief="raised",text="Другой текст") 
#        self.label3 = tkinter.Label(self.main_window,borderwidth=10,relief="raised",text="Прочий текст") 
       
#        self.label4 = tkinter.Label(self.main_window,borderwidth=7,relief="raised",text="Какой-то текст")   
#        self.label5 = tkinter.Label(self.main_window,borderwidth=10,relief="raised",text="Другой текст") 
#        self.label6 = tkinter.Label(self.main_window,borderwidth=10,relief="raised",text="Прочий текст") 
       
#        self.label1.pack(side="top")
#        self.label2.pack(side="top")
#        self.label3.pack(side="top")
       
#        self.label4.pack(side="left")
#        self.label5.pack(side="left")
#        self.label6.pack(side="left")
       
#        self.top_frame.pack()
#        self.bottom_frame.pack()
       
#     #    self.label1.pack(side="left")
#     #    self.label2.pack(side="left")    
#     #    self.label1.pack(ipadx=50,ipady=50,padx=(10,50),pady=(20,20))
#     #    self.label2.pack(ipadx=50,ipady=50,padx=50,pady=50)    
#        tkinter.mainloop()
# if __name__=="__main__":
#     my_gui = MyGUI()   

class ConvertGUI:
   def __init__(self):
      self.main_window = tkinter.Tk()
      
      self.bottom_frame = tkinter.Frame(self.main_window)
      self.top_frame = tkinter.Frame(self.main_window)
      
      
      # self.open_button1 = tkinter.Button(self.top_frame,text="Нажми здесь",command=self.do_something,relief="raised",borderwidth=4)
      # self.label_button1 = tkinter.Label(self.top_frame,text="Введите значение")
      # self.calc_label1 = tkinter.Entry(self.top_frame,borderwidth=2,relief="raised")
      
      # self.open_button1.pack(side = "left")
      # self.label_button1.pack(side="left")
      # self.calc_label1.pack(side="left")
      self.value = tkinter.StringVar()
      self.calc_result = tkinter.Button(self.top_frame,textvariable=self.value)
      self.open_button2 = tkinter.Button(self.bottom_frame,text="Нажми здесь",command=self.do_something,relief="raised",borderwidth=4)
      self.label_button2 = tkinter.Label(self.bottom_frame,text="Введите значение")
      self.calc_entry = tkinter.Entry(self.bottom_frame,borderwidth=2,relief="raised")
      self.calc_button2 = tkinter.Button(self.bottom_frame,command=self.calculate,text="Перевести в километры")
      
      self.quit_button2 = tkinter.Button(self.bottom_frame,text="Закрыть",command=self.quit,relief="raised",borderwidth=4)
      
      
      
      
      self.open_button2.pack(side = "left")
      self.label_button2.pack(side="left")
      
      self.calc_entry.pack(side="left")
      
      self.calc_button2.pack(side="left")
      self.quit_button2.pack(side="left")
      self.calc_result.pack(side="left")
      
      self.quit_button = tkinter.Button(self.main_window,text="Закрыть",command=self.quit,relief="raised",borderwidth=4)      
      # self.open_button = tkinter.Button(self.main_window,text="Нажми здесь",command=self.do_something,relief="raised",borderwidth=4)
      # self.quit_button = tkinter.Button(self.main_window,text="Закрыть",command=self.quit,relief="raised",borderwidth=4)
      self.bottom_frame.pack()
      self.top_frame.pack()
      
      tkinter.mainloop()
   def do_something(self):
      tkm.showinfo("Реакция","Спасибо,что нажали кнопку")
   def quit(self):
      self.main_window.destroy()
   def calculate(self):
      miles = float(self.calc_entry.get())
      kilo = miles/0.642
      self.value.set(kilo)
      tkm.showinfo("Значение: ",str(kilo)+" kilometers - это "+str(miles)+" миль")
if __name__=="__main__":
   my_gui = ConvertGUI()

# class Listbox:
#    def __init__(self):
#       self.main_menu = tkinter.Tk()
      
#       self.list = tkinter.Listbox(self.main_menu,height=0,width=0)
#       self.list.pack()
      
#       self.list.insert(0,"Понедельник ")
#       self.list.insert(1,"Вторник")

#       tkinter.mainloop()
# if __name__=="__main__":
#    listbox = Listbox()

# class ScrollHorizVer:
#     def __init__(self):
#         self.main_menu = tkinter.Tk()
#         self.main_menu.title("Меню с выбором города")
#         self.outer_frame = tkinter.Frame(self.main_menu)
#         self.outer_frame.pack()
#         self.inner_frame = tkinter.Frame( self.outer_frame)
#         self.inner_frame.pack()
#         # self.bottom_frame = tkinter.Frame( self.outer_frame,height=2,width=15,borderwidth=1,relief="raised")
#         # self.bottom_frame.pack()
#         self.listbox=tkinter.Listbox(self.inner_frame, height=5,width=10)
#         self.listbox.pack(side="left")
#         self.v_scroll = tkinter.Scrollbar(self.inner_frame,orient=tkinter.VERTICAL)
#         self.v_scroll.pack(side="right",fill=tkinter.Y)
        
#         self.h_scroll = tkinter.Scrollbar(self.outer_frame, orient=tkinter.HORIZONTAL)
#         self.h_scroll.pack(side="bottom",fill=tkinter.X)
        
#         self.h_scroll.config(command=self.listbox.xview)
#         self.v_scroll.config(command=self.listbox.yview)
#         self.listbox.config(yscrollcommand=self.v_scroll.set,xscrollcommand=self.h_scroll.set)
        
#         cities = ["Брюссельxcvbjkhklh,mcvhj","Минск","Лондон","Токио"," Брюссельxcvbjkhklh,mcvhj"," Брюссель"," Брюссель"," Брюссель"," Брюссель"," Брюссель"," Брюссель"," Брюссель",]
        
#         for city in cities:
#             self.listbox.insert(tkinter.END,city)
        
        
#         tkinter.mainloop()
# if __name__=="__main__":  
#       scrollHorizVer = ScrollHorizVer()

# class Horiz:
#     def __init__(self):
#         self.main_menu = tkinter.Tk()
#         self.listbox_frame = tkinter.Frame(self.main_menu)
#         self.listbox_frame.pack(padx=20,pady=20)
#         self.listbox = tkinter.Listbox(self.listbox_frame,height=0,width=30)
#         self.listbox.pack(side="top")
        
#         self.h_scroll = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.HORIZONTAL)
#         self.h_scroll.pack(side="bottom",fill=tkinter.X)
        
#         self.h_scroll.config(command=self.listbox.xview)
        
#         self.listbox.config(xscrollcommand= self.h_scroll.set)
        
#         cities = ["Брюссельxcvbjkhklh,mcvhj","Минск","Лондон","Токио"," Брюссельxcvbjkhklh,mcvhj"," Брюссель"," Брюссель"," Брюссель"," Брюссель"," Брюссель"," Брюссель"," Брюссель",]
        
#         for city in cities:
#             self.listbox.insert(tkinter.END,city)
        
        
#         tkinter.mainloop()
# if __name__=="__main__":  
#       scrollHorizVer = Horiz()
        
        
# class CheckButtons:
#     def __init__(self):
        
#         self.main_menu = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_menu)
#         self.bottom_frame=tkinter.Frame(self.main_menu)
        
#         self.cb_var1=tkinter.IntVar()
#         self.cb_var2=tkinter.IntVar()
#         self.cb_var3=tkinter.IntVar()
        
#         self.cb_var1.set(0)
#         self.cb_var2.set(0)
#         self.cb_var3.set(0)
        
      
        
        
#         self.cb1 = tkinter.Checkbutton(self.top_frame,text="Вариант 1",variable=self.cb_var1)
#         self.cb2 = tkinter.Checkbutton(self.top_frame,text="Вариант 2",variable=self.cb_var2)
#         self.cb3 = tkinter.Checkbutton(self.top_frame,text="Вариант 3",variable=self.cb_var3)
        
      
#         self.cb1.pack()
#         self.cb2.pack()
#         self.cb3.pack()
        
#         self.ok_button = tkinter.Button(self.bottom_frame,text="OK",command=self.show_choice)
#         self.quit_button = tkinter.Button(self.bottom_frame,text="Выйти",command=self.main_menu.destroy)
        
#         self.ok_button.pack(side="left")
#         self.quit_button.pack(side="left")
        
#         self.top_frame.pack()
#         self.bottom_frame.pack()
        
#         tkinter.mainloop()     
        
#     def show_choice(self):
#         self.message = ""     
#         if self.cb_var1.get() == 1:
#             self.message += "Вы выбрали  1\n"
#         if self.cb_var2.get() == 1:
#             self.message += "Вы выбрали  2\n"
#         if self.cb_var3.get() == 1:
#             self.message += "Вы выбрали  3\n"
               
#         tkm.showinfo("Выбор: ",self.message)
               
# if __name__=="__main__":  
#       check = CheckButtons()
            
# class timeZone:
#     def __init__(self):
#         self.main_menu = tkinter.Tk()
#         self.main_menu.title("Часовые пояса")
        
#         self.top_frame = tkinter.Frame(self.main_menu)
#         self.mid_frame = tkinter.Frame(self.main_menu)
#         self.bottom_frame = tkinter.Frame(self.main_menu)
        
#         self.top_frame.pack()
#         # self.mid_frame.pack()
#         self.bottom_frame.pack()
        
#         self.listbox = tkinter.Listbox(self.top_frame,height=5,width=0,relief="raised",borderwidth=2)
#         self.listbox.bind("<<ListboxSelect>>",self.timezone)
        
#         self.cities = ["Париж","Лондон","Берлин","Нью-Йорк","Сидней"]
        
#         self.value = tkinter.StringVar()
        
#         for city in self.cities:
#             self.listbox.insert(tkinter.END,city)
            
#         self.scroll = tkinter.Scrollbar(self.top_frame,orient="vertical")
        
#         self.scroll.config(command=self.listbox.yview)
#         self.listbox.config(yscrollcommand=self.scroll.set)
        
#         self.listbox.pack(side="left")
#         self.scroll.pack(side="right",fill=tkinter.Y)
        
        
        
        
#         self.label1 = tkinter.Label(self.bottom_frame,text="Часовой пояс",width=0)
#         self.time_zone = tkinter.Label(self.bottom_frame,textvariable=self.value,width=5,borderwidth=2,relief="solid")
        
#         self.label1.pack(side="left")
#         self.time_zone.pack(side="right")
        
#         tkinter.mainloop()
        
#     def timezone(self,event):
#         zone= event
#         index = self.listbox.curselection()
#         zone = self.listbox.get(index[0])
#         if zone == "Париж":
#             self.value.set("+1:00")
#         elif zone == "Лондон":
#            self.value.set( "+2:00")
#         elif zone == "Берлин":
#             self.value.set("+3:00")
#         elif zone == "Нью-Йорк":
#             self.value.set("+4:00")
#         elif zone == "Сидней":
#             self.value.set("+5:00")
#         # tkm.showinfo(self.time_zone)
# if __name__=="__main__":
#     time = timeZone()

# class Dig:
#     x = int(input())
#     y=int(input())
#     @classmethod
#     def com(cls):
#         print(cls.x+cls.y)
        
# Dig.com()
        
# def greet_me(**kwargs):
#     for key in kwargs.items():
#         print("{0}".format(key))
       
# greet_me(name = "yasoob",n="cghmj",r="ghjg,")
# # def test_args_kwargs(arg1, arg2, arg3):
# #     print("arg1:", arg1)
# #     print("arg2:", arg2)
# #     print("arg3:", arg3)

# # args = ("two", 3, 5)
# # test_args_kwargs(*args)

# func_output = 0
# msg = func_output or "Не было возвращено данных"
# print(msg)


# c=lambda x,y:x+y
# print(c(2,6))

# n = int(input("Введите число "))
# def Fact(m):
#     for i in range(m,0,-1):
#         if (i ==1):
#             return 1
#         else:
#             return Fact(i-1)* i
# print(Fact(n))
        