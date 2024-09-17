#mostre quatro produtos a serem comprados em uma lanchonete 
#coxinha, pastel, cafe e suco

print("LANCHONETE")
print ("1 - Coxinha - 5,00")
print ("2 - Pastel - 7,00")
print ("3 - Cafe - 4,00")
print ("4 - Suco - 6,00")
print ("6 - Sair")

total = 0 
while True:
    op = int(input("Qual item ? "))
   

    if (op == 1):
        qtd = int(input("Quantas unidades? "))
        total = total + qtd * 5.00
    elif (op == 2):
        qtd = int(input("Quantas unidades? "))
        total = total + qtd * 7.00
    elif (op == 3):
        qtd = int(input("Quantas unidades? "))
        total = total + qtd * 4.00
    elif (op == 4):
        qtd = int(input("Quantas unidades? "))
        total = total + qtd * 6.00
    elif (op == 5):
        break
    else:
        print ("Invalido")

print (f"\nTotol: {total} ")