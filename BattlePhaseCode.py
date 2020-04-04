import time

def ini2(x,y,xn,xo,yn,yo):
    ini_1=baci(x)
    ini_2=baci(y)
    lista_1=[xn,xo,x]
    lista_2=[yn,yo,y]
    zb1=x+xn+xo
    zb2=y+yn+yo
    sum1=0
    for i in ini_1:
        sum1=sum1+int(i)
    sum2=0
    for i in ini_2:
        sum2=sum2+int(i)
    if sum1>sum2:
        time.sleep(3)
        print("\nFirst player wins the initiative!\n")
        time.sleep(3)
        hlt_2=attrs(xn,yo)
        helt2=zb2-hlt_2
        if helt2==2:
            print("The second gladiator surrenders!")
        elif helt2<1:
            print("The second gladiator is decapitated!")
        elif helt2==1:
            print("The second gladiator is wounded!")
        else:
            time.sleep(2)
            print("SECOND GLADIATOR:")
            lista_2=stats(yn,yo,y,hlt_2)
            print(lista_2)
            yn=lista_2[0]   
            hlt_1=attrs(yn,xo)
            helt1=zb1-hlt_1
            if helt1==2:
                print("The first gladiator surrenders!")
            elif helt1<1:
                print("The first gladiator is decapitated!")
            elif helt1==1:
                print("The first gladiator is wounded!")
            else:
                time.sleep(2)
                print("FIRST GLADIATOR:")
                lista_1=stats(xn,xo,x,hlt_1)
                print(lista_1)
                print("\nFirst gladiator remaining dice:",helt1)
                print("Second gladiator remaining dice: ",helt2)
            
                x=lista_1[2]
                xn=lista_1[0]
                xo=lista_1[1]
                y=lista_2[2]
                yn=lista_2[0]
                yo=lista_2[1]
                ini2(x,y,xn,xo,yn,yo)
        
    
    elif sum1<sum2:
        time.sleep(3)
        print("\nSecond player wins the initiative!\n")
        time.sleep(3)
        hlt_1=attrs(yn,xo)
        helt1=zb1-hlt_1
        if helt1==2:
            print("The first gladiator surrenders!")
        elif helt1<1:
            print("The first gladiator is decapitated!")
        elif helt1==1:
            print("The first gladiator is wounded!")
        else:
            time.sleep(2)
            print("FIRST GLADIATOR:")
            lista_1=stats(xn,xo,x,hlt_1)
            print(lista_1)
            xn=lista_1[0]
            hlt_2=attrs(xn,yo)
            helt2=zb2-hlt_2
            if helt2==2:
                print("The second gladiator surrenders!")
            elif helt2<1:
                print("The second gladiator is decapitated!")
            elif helt2==1:
                print("The second gladiator is wounded!")
            else:
                print("SECOND GLADIATOR:")
                lista_2=stats(yn,yo,y,hlt_2)
                print(lista_2)
                print("\nFirst gladiator remaining dice:",helt1)
                print("Second gladiator remaining dice: ",helt2)
            
                x=lista_1[2]
                xn=lista_1[0]
                xo=lista_1[1]
                y=lista_2[2]
                yn=lista_2[0]
                yo=lista_2[1]
                ini2(x,y,xn,xo,yn,yo)

    elif sum1==sum2:
        ini2(x,y,xn,xo,yn,yo)
        

def stats(x,y,z,hlt):
    if hlt!=0:
        list_stat=[x,y,z]
        list_stat2=[x,y,z]
        print(list_stat)
        zbroj=0
        for i in list_stat:
            zbroj=zbroj+i
        a=input("Which stat takes damage? Attack(a),Defense(b),or Speed(c)? ")
        if a=="a" or a=="A":
            b=int(input("How much damage? "))
            list_stat.pop(0)
            list_stat.insert(0,x-b)
        elif a=="b" or a=="B":
            b=int(input("How much damage? "))
            list_stat.pop(1)
            list_stat.insert(1,y-b)
        elif a=="c" or a=="C":
            b=int(input("How much damage? "))
            list_stat.pop(2)
            list_stat.insert(2,z-b)
        zbroj2=0
        for i in list_stat:
            zbroj2=zbroj2+i
        a=zbroj-zbroj2
        x=list_stat[0]
        y=list_stat[1]
        z=list_stat[2]
        x1=list_stat2[0]
        y1=list_stat2[1]
        z1=list_stat2[2]
        if list_stat[0]<1 or list_stat[1]<1 or list_stat[2]<1:
            print("You must have at least ONE dice for each stat! ")
            return stats(x1,y1,z1,hlt)
        else:
            if a<hlt:
                hlt1=hlt-a
                return stats(x,y,z,hlt1)
            elif a==hlt:
                return list_stat
            elif a>hlt:
                print("You miscalculated! Try again!")
                return stats(x1,y1,z1,hlt)
    else:
        list_stat=[x,y,z]
        print(list_stat)
        return list_stat
    print(list_stat)        

def baci(n):
        from random import randint
        l=[]
        for i in range(n):
            l.append(randint(1,6))
        l.sort(reverse=True)
        return l


def attrs(x,y):
    hlt=0
    n=baci(x)
    o=baci(y)
    print("ATTACK roll: ",n)
    print("DEFENCE roll:",o)
    time.sleep(1)
    for i in range(x):
        if i>len(o)-1:
            if n[i]>2:
                hlt+=1
                print("No DEFENCE!\t\t\tDAMAGE +1")
                time.sleep(1)
        elif n[i]>o[i]:
            hlt+=1
            print("ATTACK",n[i],"beats DEFENCE",o[i],"\tDAMAGE +1")
            time.sleep(1)
            
    print("\n\n\nYou lost",hlt,"dice.\n")
    return hlt
    

xn=int(input("First player ATTACK: "))
xo=int(input("First player DEFENCE: "))
x=int(input("First player SPEED: "))
yn=int(input("\nSecond player ATTACK: "))
yo=int(input("Second player DEFENCE: "))
y=int(input("Second player SPEED: "))
ini2(x,y,xn,xo,yn,yo)
