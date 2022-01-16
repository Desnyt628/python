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

###chiffrement dun message en leet speak (1337)###
###constante
SUBSTITUTIONS=[['a','4'],['e','3'],['l','1'],['o','0'],['t','7']]
###section fonctions
def coder_message(message,subtitutions):
    """traite une phrase et la traduit en leet (ancein,nouveau)"""
    for s in subtitutions:
        vcar=s[0]
        ncar=s[1]
        message=message.replace(vcar,ncar)
    return message
###section main test
message=input("message a chiffrer: ")
txt_convert=coder_message(message,SUBSTITUTIONS)
print("Tu avais saisi ceci: "+message)
print("Le codage donne ceci: "+txt_convert)
input()
exit()
