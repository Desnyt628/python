'''cryptopy_v2.0 je recomence le projet cryptopy car je les 
prolonger sur 5-6 mois je vais le refair mais en moin 
longtemp pour bien comprendre lutilisation des dictionaire
6/01/2021
by: desnyt628
##################################################################
####_#####################_#######################_###############
###| |############_######| |#####################| |##############
###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _#
###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //#
###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// #
###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  #
###########__/ |#############################__/ |################
##########|___/############628#############|___/######it's a cat!#
##################################################################''' 

###import

import string

###constante
special_caracter_string=string.printable[-5:]                        #juste the 5 laste caracter they will not change 
all_caracter = string.printable[:-5]                                 #variable name in book 'JEUCAR' create a string without the five last caracter because they will not change 
all_caracter_crypted = all_caracter[-3:]+all_caracter[:-3]           #variable name in book 'CARSUBSTI' create the crypted string
'''test_message = input('what to encrypte : ')'''                    #variable name in book 'MSG_TEST'
test_message='allo'

#generate the dictionary for encrypted
dic_encrypt={}   
dic_decrypt={}                                                       #variable name in book '
for n,k in enumerate(all_caracter):                                  #the temporary n variable is for the nomber in enumerate and k is for the keys of the dictionary /
    v=all_caracter_crypted[n]                                        #here i create the value for the dictionary i use the enumerate  methode to take teh good caracter in the string 
    dic_encrypt[k]=v                                                 #and we do the dictionary
    dic_decrypt[v]=k
for c in special_caracter_string:
    dic_decrypt[c]=c                                                 #add the 5 last unchanged special caracter of the string like \n and \t 
    dic_encrypt[c]=c                                                 #add the 5 last unchanged special caracter of the string like \n and \t 
#generate the dictionary for decrypted
k=dic_encrypt.values()


###fonction
def crypted (clear_text,crypt_dic_to_use):
    ''' crypt the text with the cesar methode 
    'A' become a 'D'and returne the crypted text '''
    secret_text=[]                                                   #make a list for joint to a str variable 
    for k in clear_text:                                             
        v=crypt_dic_to_use[k]
        secret_text.append(v)
    final_message=''.join(secret_text)                              #transforms the message frome list type to string type 
    return final_message      

                                       #returne the crypted text
def decrypted (crypted_text ,decrypt_dic_to_use):                    #dic for dictionary
    ''' crypt the text with the cesar methode 
    'A' become a 'D'and returne the crypted text '''
    secret_text=[]                                                   #make a list for joint to a str variable 
    for k in crypted_text:                                             
        v=decrypt_dic_to_use[k]
        secret_text.append(v)
    final_message=''.join(secret_text)                              #transforms the message frome list type to string type 
    return final_message
###main
crypted_text = crypted(test_message,dic_encrypt)                     #variable name in book 'text_secret 
clear_text = crypted(crypted_text,dic_decrypt) 
if test_message==clear_text:
    result='yes'
else:
    result='no'
print('clear text => ' + test_message)
print('crypted text => ' + crypted_text)
print('decrepted text => '+ clear_text)
print('the original message is same to the encrypted and decrypted text?'+'\n'+result)
input('press enter to exit')
#########-variable value-#########
'''
all_caracter = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '
all_caracter_crypted = '}~ 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|'
test_message = 'Comment sa vas?'
'''