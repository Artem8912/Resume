# Программа для определения длины самой длинной подстроки с неповторяющимися символами
word = input("Введите строку ")
length = 0 # Длина текущей подстроки
lengthstr =[] # Список всех построк с неповторяющимися символами
count = True 
box = 0
k=0 # Счётчик итераций анализа всех возможных подстрок, начиная с K-ого элемента
for j in range(k,len(word),1):
    for i in range(k,j,1):
        if word[k:j+1].count(word[i])==1 :
            count*=True
        else:
            count*=False
                        
    if count == True:
        length+=1
        lengthstr.append(length)
    else:
        count = True
        k+=1    

maxstr = max(lengthstr)

print(f"Размер самой длинной подстроки: {maxstr}")