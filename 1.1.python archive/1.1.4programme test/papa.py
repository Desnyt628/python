#calculatrice
while True:
    a=float(input("\n\npremier nombre\n>"))
    b=float(input("deuxieme nombre\n>"))
    print("1.addition\n2.multiplication\n3.division\n4.soustraction")
    c=int(input('>'))
    if c==1:
        print(a+b)
    elif c==2:
        print(a*b)
    elif c==3:
        print(a/b)
    elif c==4:
        print(a-b)