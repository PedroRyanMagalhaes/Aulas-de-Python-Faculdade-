##Faça um algoritmo que receba tres valores representando os lado de um triangulo forncecido pelo usuario verifique se os valores formam um triangulo e classificque como equilatero, isosceles ou escaleno

l1 = int(input("Valor do Lado 1 do triangulo:  "))
l2 = int(input("Valor do Lado 2 do triangulo:  "))
l3 = int(input("Valor do Lado 3 do triangulo:  "))

if (l1 > 0 and l2 > 0 and l3 > 0 )and (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 ):##teste para ver se e triangulo ou nao
    if (l1 != l2 and l1 != l3 and l2 != l3):
        print ("ESCALENO")
    else:
        if (l1 == l2 and l2 == l3):
            print ("EQUILATERO")
        else:
            print("ISOSCELES")
else:
    print("Não é triangulo")

