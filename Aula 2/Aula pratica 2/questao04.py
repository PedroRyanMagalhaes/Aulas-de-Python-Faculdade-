print ("Calculadora")
print ("+ Adição")
print ("- Subtração")
print ("* Multipli.")
print ("/ Divisão")
print ("pressione outra tecla para sair ")

op = input ("Qual operação deseja?  ")

x = int(input("Escolha um numero:  "))
y = int(input("Escolha um numero:  "))

if (op == "+"):
    res = x + y
    print (res)
elif (op == "-"):
    res = x - y
    print (res)
elif (op == "*"):
    res = x * y
    print (res)
elif (op == "/"):
    res = x / y
    print (res)
else:
    print ("Programa encerrado")

