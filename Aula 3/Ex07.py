soma = 0
qtd = 0

for i in range (1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print (f"A média de 0 ate 100 dos numeros pares é {media}")