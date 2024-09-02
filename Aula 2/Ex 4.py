#menu com frutas e depos colocar quant e valor total a pagar
print("Escolhar oque deseja comprar")
print("1 = maça")
print("2 = laranja")

produto = int(input("Qual sua escolha? "))
qntd = int(input("Quantas unidades?"))

if (produto == 1): #maça
    pagar = qntd * 2.3
    print(f"Comprado {qntd} de maças valor total de {pagar}")
elif (produto == 2):
        pagar = qntd * 3.6
        print(f"Comprado {qntd} de banana valor total de {pagar}")
else:
        print("produto inesistente")
        
