#Crie uma variavel de string que receba uma frase. Crie uma segunda variavel agroa contendo a metade da string digitada. Imprima na tela somente os dois ultimo caracteres da segunda variavel 

frase = input('diga uma frase:' )
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])