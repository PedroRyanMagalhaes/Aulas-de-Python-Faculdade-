#uma variavel global pode ser acessada pala funmçao local mas uma varival local nao pode ser usada no escopo global

#exceção usar a palavra global
def omelete ():
    global ovos
    ovos = 6

ovos = 12
omelete()
print (ovos)
