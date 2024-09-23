def soma (*num):
    acumulador = 0
    print (f"tupla : {num}")
    for i in num:
        acumulador += i
    return acumulador
    
print (f"Resultado: {soma (1,2)}\n")
print (f"Resultado: {soma(1,2,3,4,5,6)}\n")