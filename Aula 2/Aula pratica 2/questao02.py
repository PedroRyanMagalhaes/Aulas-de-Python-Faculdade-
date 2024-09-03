#traduza em python

idade = int(input("Qual sua idade? "))
if (idade > 60):
    print ("Voce tem direitos aos beneficios")
else:
   print ("Voce ta novinho ainda!")

##

dano = int(input("Este é o numero do dano que esse inimigo causa: "))
escudo = int(input("Qual valor do seu escudo? "))
if (dano > 10 and escudo == 0):
    print ("VOCÊ MORREU!")
elif (dano < escudo):
    print ("Voce matou o inimigo!")
elif (dano == escudo):
   print ("Empate")
else:
    print("TRAVOU O JOGO")

##

norte = True
sul = False
leste = False
oeste = False

if ((norte or sul or leste or oeste) == True):
    print ("Voce escapou!")
else:
    print ("JA ERA ")

