# Estrutura de dados
#tuplas, listas e dicionarios 
#Strings

mochila = ("machado", " Camisa", "Bone", "Abacate")
print (mochila)
print (mochila[0])

#tuplas é imutavel nao tem como mudar 

for item in mochila:
    print (f"Na minha mochila tem {item}")

    #ou

tam = len(mochila)
for i in range (0,tam,1):
    print (f"Na minha mochla tem {mochila[i]}")

upgrade = ("Queijo","faca")
mochilaGrande = mochila + upgrade
print (mochilaGrande) 