"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
import sys
from catalogo import Catalogo

def opcao_1(catalogo):
    resultado = catalogo.listar_usuarios()
    for nome in resultado:
        print(nome)

def opcao_2(catalogo):
    nome = input("Nome do usuário: ")
    usuario_id = catalogo.buscar_usuario_por_nome(nome)
    if usuario_id is None:
        print("Usuário não encontrado.")
        return
    playlist = catalogo.playlist_de(usuario_id)
    print(playlist)

def main():
    caminho = sys.argv[1]
    catalogo = Catalogo(caminho)

    while True:
        print("1. Listar todos os usuários")
        print("2. Ver playlist completa de um usuário")
        print("0. Sair")
        opcao = input("Informe a opção desejada: ")

        if opcao == "0":
            break
        elif opcao == "1":
            opcao_1(catalogo)
        elif opcao == "2":
            opcao_2(catalogo)
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
