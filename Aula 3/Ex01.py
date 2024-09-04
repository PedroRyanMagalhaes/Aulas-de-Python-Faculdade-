x = 1 
while (x <= 5 ):# o x ta recebendo 1, nessa linha confirma se é menor ou igual a 5 e pula pra de baixo
    print (x)#printa na tela o x que agora é 1 e pula pra baixo
    x = x + 1#aument 1 no x pois esse é o sinal matematico e volta la pra o WHILE e faz o mesmo processo so que agora com x = 2 pois aumentou 1, isso vai indo ate chegar no 6 quando voltar pro while vai verificar que 6 não é menor ou igual a 5 e parar de printar.

    inicial = int(input("Qual valor deseja iniciar? "))
    final = int(input("Qual valor deseja finalizar? "))

    x = inicial 
    while (x <= final):
        if (x % 2 == 0):
            print (x)
        else:
            print ("não é par")
        x = x + 1

##

soma = 0 
cont = 1
while (cont >= 5):
    x = float(input(f"Digite a {cont}° nota "))
    soma = soma + x ## ou soma += x
    cont = cont + 1 ## ou cont += 1
media = soma / 5
print (f"Media final: {media}")
