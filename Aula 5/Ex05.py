#realizar cadastro de lista de compra em um sistema nome quant e valor

item = [] #lista vazia
mercado = []

for i in range (3):
    item.append (input("Digite nome do item "))
    item.append (input("Quantidade "))
    item.append (input("Valor "))
    mercado.append(item[:])
    item.clear() #limpar a ista senao ele repete todos todas as vezes 
print (mercado)