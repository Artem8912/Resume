Int = input("Введите число:\n")
Roman = ""
def Decade(n1,n5,n10,k):
        if Int[len(Int) - k -1] == "1":
            Roman =n1
        elif Int[len(Int) - k -1] == "2":
            Roman = 2*n1
        elif Int[len(Int) - k -1] == "3":
            Roman = 3*n1
        elif Int[len(Int) - k -1] =="4" :
            Roman = n1+n5
        elif Int[len(Int) - k -1] == "5":
            Roman = n5
        elif Int[len(Int) - k -1] == "6":
            Roman = n5 + n1  
        elif Int[len(Int) - k -1] == "7":
            Roman = n5 + n1*2    
        elif Int[len(Int) - k -1] == "8":
            Roman = n5 + n1*3
        elif Int[len(Int) - k -1] =="9":
            Roman = n1+n10
        elif Int[len(Int) - k -1] == "0":
            Roman = ""
        return Roman 

if len(Int)==1:
    print(Decade("I","V","X",0))
elif len(Int) == 2:
    print(Decade("X","L","C",1)+Decade("I","V","X",0))
elif len(Int) == 3:
    print(Decade("C","D","M",2)+Decade("X","L","C",1)+Decade("I","V","X",0))
elif len(Int) == 4:
    print(Decade("M"," превышен диапазон","превышен диапазон",3)+Decade("C","D","M",2)+ Decade("X","L","C",1)+Decade("I","V","X",0))
                   

