import random,os

clear=lambda:os.system("cls")               #Clear_Fn
clear()

color_blue=lambda:os.system("color 0d")     #Blue_Color_Fn
color_red=lambda:os.system("color 0c")      #Red_Color_Fn
color_brwhite=lambda:os.system("color 0f")  #Bright_White_Color_Fn

color_brwhite()                             #Bright_White_Color_Fn_Call

def choose(shuff):                          #Default_Fn
    k=[]
    for i in range(0,long):
        y=list(random.choice(shuff))
        k=k+y
        random.shuffle(k)
        clear()                             #Clear_Fn_Call
        color_blue()                        #Blue_Color_Fn_Cal
    print("=======================================\nYour PassWord Is : ",end="")    
    for a in k:
        print(a,end="")
    print("\n=======================================")        

def choose1(shuff1,n):                      #Customized_Fn
    k=[]
    for j in range(0,n):
        y=list(random.choice(shuff1))
        k=k+y 
    return k

#main
print("\t\t=====================\n\t\t<|PassWord Generator|>\n\t\t=====================\n================")
choice=int(input("1.Auto Generated\n2.Customized\n================\nYour Choice(1/2) : "))
lo=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
no=['1','2','3','4','5','6','7','8','9','0']
sy=['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}',':',';','|','<','>','/','?']
if choice==1:
    long=int(input("================\nEnter Length Of The Password (Min 8) : "))
    if long>=8:
        choice1=int(input("=============================\nWhat Type Of Pass You Need?\n1.Only Aplhabets\n2.Only Numeric\n3.Only Symbols\n4.Apha-Numeric\n5.Alpha-Symbolic\n6.Symbols & Number\n7.All Mixed\n8.Auto Generate\n======================\nYour Choice In No. : "))
        if choice1==1:#Alpha
            mix=lo+up
            choose(mix)
        elif choice1==2:#NUM
            choose(no)
        elif choice1==3:#Sym
            choose(sy)
        elif choice1==4:#Alpha_Num
            mix=no+up+no+lo+no
            choose(mix)
        elif choice1==5:#Apha_Sym
            mix=up+sy+lo
            choose(mix)
        elif choice1==6:#Sym_Num
            mix=no+sy
            choose(mix)
        elif choice1==7:#MIX
            mix=up+no+sy+lo 
            choose(mix)
        elif choice1==8:#Auto
            mix=no+up+sy+lo+no
            choose(mix)    
        else:
            clear()                             #Clear_Fn_Call
            color_red()                         #Red_Color_Fn_Call
            print("============================\nInvalid Input >>> Try Again\n============================") 
    else:
        clear()                                 #Clear_Fn_Call
        color_red()                             #Red_Color_Fn_Call
        print("=============================================\n\t\t|<E><R><R><O><R>|\n\t\t  Invalid Length\n:For Customized Length Use Customized Pass Fn:\n==============================================")               
elif choice==2:
    print("========================================\nWelcome To Customized PassWord Generator\n========================================")
    upper=int(input("How Many Upper Case Letter : "))
    lower=int(input("How Many Lower Case Letter : "))
    number=int(input("How Many Numbers : "))
    symbols=int(input("How Many Symbols : "))
    print("=====================================")
    if upper<0 or number<0 or symbols<0 or lower<0:
        clear()                                 #Clear_Fn_Call
        color_red()                             #Red_Color_Fn_Call
        print("\t |<:ERROR:>|\n\tInvalid Input\n=====================================")
    else:
        x=upper+lower+number+symbols
        print("Length Of The Password is : ",x,"\n=====================================")
        result=input("Do You Want To Continue?\nY/N : ")
        print("=====================================")
        if result=='y' or result=='Y':
            clear()
            color_blue()                     #Blue_Color_Fn_Cal
            print("Your Passsword Is : ",end="")
            a=choose1(sy,symbols)
            b=choose1(lo,lower)
            c=choose1(up,upper)
            d=choose1(no,number)
            e=a+b+c+d
            random.shuffle(e)
            for a in e:
                print(a,end="")
            print("\n=====================================")            
        elif result=='n' or result=='N':            
            clear()                          #Clear_Fn_Call
            color_red()                      #Red_Color_Fn_Call
            print("============================\nInvalid Input >>> Try Again\nWell No Problem Try Again :)\n============================") 
        else:
            clear()                          #Clear_Fn_Call
            color_red()                  #Red_Color_Fn_Call
            print("============================\nInvalid Input >>> Try Again\n============================") 
                
else:
    clear()                                 #Clear_Fn_Call
    color_red()                             #Red_Color_Fn_Call
    print("============================\nInvalid Input >>> Try Again\n============================\n\t |<:ERROR:>|\n\tInvalid Input\n============================") 
input("Hit Enter To Exit")    
