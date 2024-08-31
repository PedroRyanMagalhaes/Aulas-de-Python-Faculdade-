#Escreva um programa que pergunte a quant. de KM percorrido ppor um carro alugado pelo usuario, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$6- por dia e R$0,15 por km rodado

kmPercorrido = int(input("Quantos KM voce percorreu? "))
diasAlugado = int(input("E quantos dias você ficou com o carro? "))

kmPagar = (kmPercorrido * 0.15)
diasPagar = (diasAlugado * 60)

precoTotal = (kmPagar + diasPagar)

print (f"O valor total foi de R${precoTotal}, R${kmPagar} de KM e R${diasPagar} de dias alugado")