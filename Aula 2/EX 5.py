nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))

if nome == "Vinicius":
    print ("Ola Vinicius")
elif idade < 18:
    print("Você nao é o vinicius! E é menor de idade")
elif idade > 100:
    print ("Você tem 100 anos??? o Vinicius é bem mais novo")
else:
    print("Voce tem idade perto da do vinicius mas nao é ele")