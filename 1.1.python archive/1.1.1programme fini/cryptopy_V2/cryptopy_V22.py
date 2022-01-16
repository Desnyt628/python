'''
cryptopy_v2.2 
encrypte and decrypte a file. can be use as a modul too.

dic to use:
    dic_encrypt    /crypted dictionary
    dic_decrypt    /decrypted dictionary

6/01/2021 - 23/01/2021
by: desnyt628
##################################################################
####_#####################_#######################_###############
###| |############_######| |#####################| |##############
###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _#
###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //#
###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// #
###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  #
###########__/ |#############################__/ |################
##########|___/############628##############|___/#####it's a cat!#
##################################################################''' 

###import
import string
###constante
special_caracter_string=string.printable[-5:]                        #juste the 5 laste caracter they will not change 
all_caracter = string.printable[:-5]                                 #variable name in book 'JEUCAR' create a string without the five last caracter because they will not change 
all_caracter_crypted = all_caracter[-3:]+all_caracter[:-3]           #variable name in book 'CARSUBSTI' create the crypted string
file_in='cryptopy_file_in.txt'
file_out='cryptopy_file_out.txt'
#generate the dictionary for encrypted and decrypted
dic_encrypt={}                                                       #crypted dictionary
dic_decrypt={}                                                       #decrypted dictionary
for n,k in enumerate(all_caracter):                                  #the temporary n variable is for the number in enumerate and k is for the keys of the dictionary /
    v=all_caracter_crypted[n]                                        #here i create the value for the dictionary i use the enumerate  methode to take teh good caracter in the string 
    dic_encrypt[k]=v                                                 #and we do the dictionary
    dic_decrypt[v]=k
for c in special_caracter_string:
    dic_decrypt[c]=c                                                 #add the 5 last unchanged special caracter of the string like \n and \t 
    dic_encrypt[c]=c                                                 #add the 5 last unchanged special caracter of the string like \n and \t 
###fonction
def crypted (clear_text,crypt_dic_to_use):
    '''crypt the text with the cesar methode 
    'A' become a 'D'and returne the crypted text'''
    secret_text=[]                                                   #make a list for joint to a str variable 
    for k in clear_text:                                             
        v=crypt_dic_to_use[k]
        secret_text.append(v)
    final_message=''.join(secret_text)                               #transforms the message frome list type to string type 
    return final_message                                             #returne the crypted text
def decrypted (crypted_text ,decrypt_dic_to_use):                    #dic for dictionary
    '''decrypt the text with the cesar methode 
    'D' become a 'A' and returne the crypted text'''
    secret_text=[]                                                   #make a list for joint to a str variable 
    for k in crypted_text:
        v=decrypt_dic_to_use[k]
        secret_text.append(v)
    final_message=''.join(secret_text)                              #transforms the message frome list type to string type 
    return final_message
###main
if __name__=="__main__":
    print('\n')
    print("###################################################################")
    print("####_#####################_#######################_################")
    print("###| |############_######| |#####################| |###############")
    print("###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _##")
    print("###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //##")
    print("###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// ##")
    print("###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  ##")
    print("###########__/ |#############################__/ |#################")
    print("##########|___/############628##############|___/######it's a cat!#")
    print("###################################################################")
    print('\n*******************cryptopy project, version 2.2*******************\n')
    ENCRYPTE=True
    with open(file_in,'r') as read_file:
        message=read_file.read()
      
        if ENCRYPTE:
            return_txt=crypted(message,dic_decrypt)
        else:
            return_txt=crypted(message,dic_decrypt)
        
    with open(file_out,'w') as write_file:
        write_file.write(return_txt)