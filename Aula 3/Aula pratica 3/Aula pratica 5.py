#um Cinema cobra preços diferente para ingressos tiver menos de 3 anos é gratis, se tiver entre 3 e 12 custa 15,00 e se tiver mais de 12 custa 30,00
#pergunte idade e informa o preço
#encerre laço se digitar 0
#  total de pessoas, total de dinheiro e media de idades

totalPessoas = 0
totalDinheiro = 0
totalIdades = 0

while True:
    idade = int(input("Qual sua idade? " ))
    if idade == 0:
        break
    
    totalPessoas += 1
    totalIdades += idade

    if idade < 3:
        ingresso = 0
    else:
        if idade < 12:
            ingresso = 30
        else: ingresso = 15

    totalDinheiro += ingresso

if totalPessoas > 0:
    media = totalIdades / totalPessoas
    print (f"Total de pessoas: {totalPessoas}, total arrecadado: {totalDinheiro}, media de idade foi: {media}")

 

