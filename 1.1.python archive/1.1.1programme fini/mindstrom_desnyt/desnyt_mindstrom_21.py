'''
##################################################################
####_#####################_#######################_###############
###| |############_######| |#####################| |##############
###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _#
###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //#
###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// #
###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  #
###########__/ |#############################__/ |################
##########|___/############628#############|___/######it's a cat!#
##################################################################

d1*pi=c1                            pour trouver la circonference du robot
c2*pi=d2                            pour trouver la circonference de la roue
c1/d2=ntr(nombre de toure de roue)  pour trouver le nombre de tour de roue qui faut mettre dans le programme
d1                                  distance entre les deux roue
c1                                  la circonference du robot
c2                                  circonference de la roue
d2                                  distance parcouru en un tour de roue
''' 
###constante
pi=3.14159265359  

###modul
def rotation1():
    ''''permet de fair une rotation avec le point daxe 
    entre les deux roue dit en nombre de tour de roue'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=str(c1/d2)
    print('nombre de tour necesaire: '+NTR)
    
def rotation2():
    ''''permet de fair une rotation avec le point daxe 
    entre les deux roue dit en nombre de tour de roue'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR2=NTR/2
    print('nombre de tour necesaire: '+str(NTR2))
    
def rotation4():
    ''''permet de fair une rotation avec le point daxe 
    entre les deux roue dit en nombre de tour de roue'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR4=NTR/4
    print('nombre de tour necesaire: '+str(NTR4))
       
def tour1():
    '''permet de fair une rotation avec le point daxe sur une roue 
    dit en nombre de tour de roue'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=str(c1/d2)
    print('nombre de tour necesaire: '+NTR)
    
def tour2():
    '''permet de fair une rotation avec le point daxe sur une roue 
    dit en nombre de tour de roue'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR2=NTR/2
    print('nombre de tour necesaire: '+str(NTR2))
    
def tour4():
    '''permet de fair une rotation avec le point daxe sur une roue 
    dit en nombre de tour de roue'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR4=NTR/4
    print('nombre de tour necesaire: '+str(NTR4))
    
def avance():
    '''permet davancer une distance x dit 
    en nombre de tour de roue'''
    a=float(input('distance a fair: '))
    c2=float(input("diametre de la roue: "))
    d2=c2*pi
    NTR=str(a/d2)
    print('nombre de tour necesaire: '+NTR)
    
def rotation_deg1():
    '''permet de fair une rotation avec le point daxe 
    entre les deux roue dit en degre'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR_deg1=NTR*360
    print('nombre de degrer necesaire: '+str(NTR_deg1))
    
def rotation_deg2():
    '''permet de fair une rotation avec le point daxe 
    entre les deux roue dit en degre'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR_deg=NTR*360
    NTR_deg2=NTR_deg/2
    print('nombre de degrer necesaire: '+str(NTR_deg2))
    
def rotation_deg4():
    '''permet de fair une rotation avec le point daxe 
    entre les deux roue dit en degre'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR_deg=NTR*360
    NTR_deg4=NTR_deg/4
    print('nombre de degrer necesaire: '+str(NTR_deg4))
    
def tour_deg1():
    '''permet de fair une rotation avec le point 
    daxe sur une roue dit en degre'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR_deg1=NTR*360
    print('nombre de degrer necesaire: '+str(NTR_deg1))
    
def tour_deg2():
    '''permet de fair une rotation avec le point 
    daxe sur une roue dit en degre'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR_deg=NTR*360
    NTR_deg2=NTR_deg/2
    print('nombre de degrer necesaire: '+str(NTR_deg2))
    
def tour_deg4():
    '''permet de fair une rotation avec le point 
    daxe sur une roue dit en degre'''
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("diametre de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=c1/d2
    NTR_deg=NTR*360
    NTR_deg4=NTR_deg/4
    print('nombre de degrer necesaire: '+str(NTR_deg4))
    
def avance_deg():
    'permet davancer une distance x dit en degre'
    a=float(input('distance a fair: '))
    c2=float(input("diametre de la roue: "))
    d2=c2*pi
    NTR=a/d2
    NTR_deg=NTR*360
    print('nombre de degrer necesaire: '+str(NTR_deg))

###main
print('by:desyt')
print('\n'*1000)
print("###################################################################")
print("####_#####################_#######################_################")
print("###| |############_######| |#####################| |###############")
print("###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _##")
print("###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //##")
print("###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// ##")
print("###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  ##")
print("###########__/ |#############################__/ |#################")
print("##########|___/############628#############|___/#######it's a cat!#")
print("###################################################################")
while True:
    b=0
    a=0
    t=0
    b=int(input('option:\n1.tour de roue\n2.degre\n3.clear screen\n\noption: '))
    if b==1:
        
       a=input('option:\n1.rotation sur une roue\n2.rotation sur lui meme\n3.avancer\n\noption: ')
       if int(a)==1:
            t=int(input('option:\n1.tour complet\n2.demie tour\n3.quart de tour\n\noption: '))
            if t==1:
                tour1()
            elif t==2:
                tour2()
            elif t==3:
                tour4()
            else:
                print('choisi une option valide')
       elif int(a)==2:
            t=int(input('option:\n1.tour complet\n2.demie tour\n3.quart de tour\n\noption: '))
            if t==1:
                rotation1()
            elif t==2:
                rotation2()
            elif t==3:
                rotation4()
            else:
                print('choisi une option valide') 
       elif int(a)==3:
            avance()
       else:
        print('choisi une option valide')  
    elif b==2:
        a=input('option:\n1.rotation sur une roue\n2.rotation sur lui meme\n3.avancer\n\noption: ')
        if int(a)==1:
            t=int(input('option:\n1.tour complet\n2.demie tour\n3.quart de tour\n\noption: '))
            if t==1:
                tour_deg1()
            elif t==2:
                tour_deg2()
            elif t==3:
                tour_deg4()
            else:
                print('choisi une option valide')
        elif int(a)==2:
            t=int(input('option:\n1.tour complet\n2.demie tour\n3.quart de tour\n\noption: '))
            if t==1:
                rotation_deg1()
            elif t==2:
                rotation_deg2()
            elif t==3:
                rotation_deg4()
            else:
                print('choisi une option valide')   
        elif int(a)==3:
            avance_deg()
        else:
                print('choisi une option valide')  
    elif b==3:
        print('\n'*1000)
        print("###################################################################")
        print("####_#####################_#######################_################")
        print("###| |############_######| |#####################| |###############")
        print("###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _##")
        print("###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //##")
        print("###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// ##")
        print("###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  ##")
        print("###########__/ |#############################__/ |#################")
        print("##########|___/############628#############|___/#######it's a cat!#")
        print("###################################################################")
        
    else:
        print('choisi une option valide')
#EOF /n