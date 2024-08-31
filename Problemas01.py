#Exercicio 1 
#Desenvolva um algoritmo que solicite ao usuario o preço de um produtdo e um percentual de desconto a ser aplicado, calcule e exiba o valro do desconto e o preço final do produto.

preco = float(input("digite o preço do produto "))
percentual = float (input("escolha um percentual de desconto entre 0 - 100% "))

desconto = (preco * percentual / 100)
precoFinal = preco - desconto

print(f"o preco do produto é {precoFinal} com {desconto}% de deconto")