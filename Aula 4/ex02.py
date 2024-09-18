#parametros
#def nome_da_funçao (variavel):

def realce (s1): 
    print (", ---- ,")
    print (s1)
    print (", ---- .")

realce("  Menu")

def sub (x,y):
    res = x - y
    print (res)

sub(10,4) #passou os parametros de x e y 

#parametros opcionais
def soma (x=0, y=0, z=0): # set os paramentros em valor fixo e se nao parametrizar nada ele vai assumir esse valor fixo
    res = x + y + z
    print (res)

soma (4,5)
soma (4,5,7)
soma ()
