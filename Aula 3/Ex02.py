##Programa so deve aceitar numero positivo 

x = int(input("Digite um valor maior que zero: "))
while (x <= 0):
    x = int(input("Digite um valor maior do que zero: "))
print(f'Voce digitou {x}. encerrando o programa')