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
print("")
import string
s=string.printable[:-5]
dic={}
for k in s:
    v='X'
    dic[k]=v
###fonction
def X(g):
    txt=[]
    for k in g:
        v=dic[k]
        txt.append(v)
        txt2="".join(txt)
    return txt2 
###main
while True:
    h=input("ecrit: ")
    S=X(h)
    print(h+'=>'+S)
    input("enter*\n")