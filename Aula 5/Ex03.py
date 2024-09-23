#Listas
#esturtura de dados dinamica 

mochila = ["limao", "laranja"]
mochila[1] = "Maça"
print (mochila)

#consegue alterar item dentro da lista

mochila.append ("ovos")
print  (mochila) #.append = adiconad no fim da lista algum item

mochila.insert(1,"Canivete")
print  (mochila) #.insertt = adicona na posição informada

mochila.remove ("ovos") 
print  (mochila)#.remove = remove dado informado

del mochila [1] 
print (mochila) # del = deleta indice informado
