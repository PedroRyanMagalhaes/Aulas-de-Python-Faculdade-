#dados as notas dos alunos escreva expressao para 
#a)Encontrar quantos alunos tiraram nota 7 
#b) Alterar a ultima nota para 4
#c) Maior nota
#d)Ordenar lista de notas
#e) A media das notas

notas = [9,7,7,10,3,9,6,6,2]

#a
print (notas.count(7))

#b
notas [-1] = 4
print (notas)

#c
print(max(notas))

#d
print (notas.sort())

#e
notas.sort()
print (notas)


print (sum(notas) / len(notas))
