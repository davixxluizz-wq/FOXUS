#classe 1.
import os
import webbrowser as wb

#inicio/saudaçaes

print("bem-vindo(a) a foxus terminal dijite help para  ver os comandos do sistema!")

class FOXUS():

    #defs do cmd v1.0.0
    def foxus_print(text):
        print(text)

    def foxus_color(color):
        os.system(f"color {color}")

    def HELP():
        print("""foxus_print - printar texto
foxus_color - cor do terminal
foxus_url - entar em uma url""")

    def foxus_url(link):
        wb.open(link)
#sistema principal de funcionamento
while True:
    player = input("@player>$ ")

    if player in ("HELP", "help"):
        FOXUS.HELP()

    if player.startswith("foxus_color "):
        tita =  player[len("foxus_color "):]
        FOXUS.foxus_color(tita)

    if player.startswith("foxus_print "):
        texto = player[len("foxus_print "):]
        FOXUS.foxus_print(texto)

    if player.startswith("foxus_url "):
        linkk = player[len("foxus_url "):]
        FOXUS.foxus_url(linkk)