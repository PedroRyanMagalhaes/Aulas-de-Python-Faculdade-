
while True:
    nome = input ("Qual seu nome? ")
    if (nome != "Pedro"):
        print ("RESPOSTA INCORRETA")
        continue #volta para o while ou seja vai perguntar dnv qual seu nome
    senha = input("Qual a senha? ")
    if (senha != "2003"):
        print ("INVASOR")
        continue
    else:
        print ("Acesso concedido")
        break
