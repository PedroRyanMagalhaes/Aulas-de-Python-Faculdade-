#algoritimo que permita cadastrar jogos informado nome e qual videogame ele pertence , crie um menu de opções e armazene os dados em arquivo 

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open (nomeArquivo, "at")
    except:
        print ("Erro ao abri o arquivo")
    else:
        a.write (f"{nomeJogo}; ^{nomeVideoGame}\n")
    finally:
        a.close()

def validaNumero (pergunta, min , max): 
    x = int(input(pergunta))
    while ((x < min or x > max)):
        x = int(input(pergunta))
    return x 

def existeArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, "wt")
        a.close()
    except:
        print ("Erro na criação do arquivo")
    else:
        print ("Arquivo Criado com Sucesso\n")

def listarTodos (nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
    except:
        print ("Erro ao ler o arquivo.")
    else: 
        print (a.read())
    finally:
        a.close()


arquivo = "games.txt"
if existeArquivo (arquivo):
    print ("Arquivo localizado no PC")
else:
    print("Arquivo Inexistente")
    criarArquivo (arquivo)


 
while True:
    print ("Menu")
    print ("1 - Novo item")
    print("2 - Listar todos")
    print("3 - Sair ")

    op = validaNumero ("Escolha a opção:", 1, 3)
    if (op == 1): #novo item
        print ("Opçao De novo item selecionada\n")
        nomeJogo = input ("Nome do jogo ")
        nommeVIdeoGame = input ("Nome do Video Game ")
        cadastrarJogo (arquivo, nomeJogo, nommeVIdeoGame)


    elif (op == 2): #listas tudo
        print ("Opçao De listar todos selecionada\n")
        listarTodos(arquivo)


    elif (op == 3): #sair
        print ("Encerrando programa\n")
        break