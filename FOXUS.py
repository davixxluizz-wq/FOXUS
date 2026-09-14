import os
import webbrowser as wb
from pathlib import Path

# início / saudações
print("Bem-vindo(a) ao Foxus Terminal v1.0.2 (beta)")
print("Digite help para ver os comandos do sistema!")


class FOXUS:

    # comandos do Foxus
    @staticmethod
    def foxus_print(text):
        print(text)

    @staticmethod
    def foxus_color(color):
        os.system(f"color {color}")

    @staticmethod
    def HELP():
        print("""foxus_print - printar texto
foxus_color(cor) - cor do terminal
foxus_url(url) - entrar em uma URL
foxus_creat_file(nome) - criar um arquivo
foxus_creat_write_file(nome, texto) - criar arquivo e escrever
foxus_open_file(nome) - abrir um arquivo
foxus_del_file(nome) - deletar um arquivo
foxus_creat_folder(nome) - criar uma pasta
foxus_open_folder(nome) - abrir uma pasta
foxus_shutdown(temp) - desligar seu cumputador""")

    @staticmethod
    def foxus_url(link):
        wb.open(link)

    @staticmethod
    def foxus_creat_file(name):
        with open(name, "w", encoding="utf-8"):
            pass

    @staticmethod
    def foxus_creat_write_file(name, write):
        with open(name, "w", encoding="utf-8") as arquivo:
            arquivo.write(write)

    @staticmethod
    def foxus_delet_file(name):
        os.remove(name)

    @staticmethod
    def foxus_open_file(name):
        os.system(f'start "" "{name}"')

    @staticmethod
    def  foxus_creat_folder(name):
         pasta = Path(f"{name}")
         pasta.mkdir(exist_ok=True)

    @staticmethod
    def foxus_open_folder(name):
        os.system(f"start {name}")

    @staticmethod
    def foxus_shutdown(temp):
        os.system(f"shutdown -s -t {temp}")

    


# sistema principal de funcionamento
while True:
    player = input("@player>$ ")

    if player.lower() == "help":
        FOXUS.HELP()

    elif player.startswith("foxus_color "):
        cor = player[len("foxus_color "):]
        FOXUS.foxus_color(cor)

    elif player.startswith("foxus_print "):
        texto = player[len("foxus_print "):]
        FOXUS.foxus_print(texto)

    elif player.startswith("foxus_url "):
        link = player[len("foxus_url "):]
        FOXUS.foxus_url(link)

    elif player.startswith("foxus_creat_file "):
        nome = player[len("foxus_creat_file "):]
        FOXUS.foxus_creat_file(nome)

    elif player.startswith("foxus_open_file "):
        nome = player[len("foxus_open_file "):]
        FOXUS.foxus_open_folder(nome)

    elif player.startswith("foxus_del_file "):
        nome = player[len("foxus_del_file "):]
        FOXUS.foxus_delet_file(nome)

    elif player.startswith("foxus_creat_write_file "):
        dados = player[len("foxus_creat_write_file "):]

        # separa o nome do arquivo e o texto
        partes = dados.split(" ", 1)

        if len(partes) == 2:
            nome = partes[0]
            texto = partes[1]

            FOXUS.foxus_creat_write_file(nome, texto)
        else:
            print("Uso: foxus_creat_write_file arquivo.txt texto")

    elif player.startswith("foxus_creat_folder "):
         name_folder = player[len("foxus_creat_folder "):]
         FOXUS.foxus_creat_folder(name_folder)

    elif player.startswith("foxus_open_folder "):
        name_open = player[len("foxus_open_folder "):]
        FOXUS.foxus_open_folder(name_open)

    elif player.startswith("foxus_shutdown "):
        temp = player[len("foxus_shutdown "):]
        FOXUS.foxus_shutdown(temp)