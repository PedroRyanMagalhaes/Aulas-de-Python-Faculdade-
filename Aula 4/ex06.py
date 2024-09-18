#Valide a string, funçao recebe a string em sil, o minimo e o maximo se o tamanho da string estive entre os vlores de minimo e maximo e falso caso contratio. 

def validaString (pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min)) or ((tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = validaString("Digite uma string:", 1,4)
print ("Voce digitou uma boa string pro mestre")