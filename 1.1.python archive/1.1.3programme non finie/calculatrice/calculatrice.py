###constante
Qtest=(4,6)
patron_Q=("combien font %s x %s ?\n>")
###fonction

###main
question = Qtest
invite = patron_Q%question
reponse=input (invite)
if int(reponse) == question[0]*question[1]:
    print("bonne reponse")
else:
    print("mauvaise reponse")
