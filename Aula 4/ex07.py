while True:
    try:
        x = int(input("Digite um numero: "))
        break
    except ValueError:
        print ("OOPSSSS..... Tente novamente")

i = 0
while True:
    try:
        nome = input ("Por favor digite o seu nome: ")
        ind = int(input("Digite um indice para verificar "))
        print (nome[ind])
        break
    except ValueError:
        print ("OOPAAA AMIGA;;;;;; tenta dnv ")
    finally:
        print (f"Tentativa {i}")
        i += 1
