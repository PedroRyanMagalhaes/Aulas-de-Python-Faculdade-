#for - para

for i in range (1,5,2): #valor inicial, valor final, e valor do passo de tanto em tanto
    print (i)

for i in range (10, 0 , -2):
    print (i)

##varredura de string
frase = "Vou viajar para o rock in rio"
for i in range (0, len(frase), 1):
    print(frase[i], end="")