#Escreva algoritmo que crie uma tupla com 5 palavra. Encontre dentro as vogais e faça print com nome e as vogais

palavras = ("Pedro", "Pape", "Cadeira","Boulos", "Ronaldinho")

for palavra in palavras:
    print (f"\n {palavra.upper()}, Vogais: ")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print (letra.upper(), end = " ")
