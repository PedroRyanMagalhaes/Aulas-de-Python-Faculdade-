#Funçao qe calcue o fatorial de um numero recebiod como parametro e retorne o resultado
#so valor positivio
#crie a docstring

def validaPositivo (pergunta, min , max): 
    x = int(input(pergunta))
    while ((x < min or x > max)):
        x = int(input(pergunta))
    return x 
        
def fatorial (num):
    '''
    Funçao que calcula a fatorial de um numero passado pelo usuario 
    param num : 
    return: 
    '''
    fat = 1
    if num == 0:
        return fat
    #fatorial de 0 e 1 sempre 1
    for i in range (1, num + 1, 1):
        fat *= i
    
    return fat

x = validaPositivo ("Digite um valor para calcular a fatorial: ", 0,9999)
print (f"{x}! = {fatorial(x)}")
help (fatorial)