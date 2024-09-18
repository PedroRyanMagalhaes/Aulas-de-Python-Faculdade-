def borda (var):
    tam = len(var)
    #colocar um if para so executar se tiver palavra
    if tam:
        print ("+","-" * tam, "+") #para fazer a borda do tamanho da variavel so multiplicar o tamanho dela pelos caracteres que formam as bordas
        print ("&",var,"&")
        print ("+","-" * tam, "+")

borda("PEDRO")
borda("NEXTJSTHEBEST")

        
