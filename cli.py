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
    for conteudo_id in playlist:
    print(catalogo.nome_conteudo(conteudo_id))

def opcao_3(catalogo):
    nome = input("Nome do usuário: ")
    usuario_id = catalogo.buscar_usuario_por_nome(nome)
    if usuario_id is None:
        print("Usuário não encontrado.")
        return
        
    playlist = catalogo.playlist_de(usuario_id)
    print(f"Playlist de {nome} tem {len(playlist)} itens.")
    posicao = int(input("Informe a posição: "))
    resultado = catalogo.conteudo_na_posicao(usuario_id, posicao - 1)

    if resultado is None:
        print("Posição inválida.")
        return

    print(catalogo.nome_conteudo(conteudo_id))

def opcao_4(catalogo):
    quantidade = int(input("Quantos usuários? "))

    usuario_ids = []

    for i in range(quantidade):
        nome = input("Nome do usuário: ")

        usuario_id = catalogo.buscar_usuario_por_nome(nome)

        if usuario_id is None:
            print("Usuário não encontrado.")
            return

        usuario_ids.append(usuario_id)

    resultado = catalogo.intersecao_playlists(usuario_ids)

    for conteudo_id in resultado:
        print(catalogo.nome_conteudo(conteudo_id))
  

def main():
    caminho = sys.argv[1]
    catalogo = Catalogo(caminho)

    while True:
        print("TrilhaSonora")
        print("============")
        print("1. Listar todos os usuários")
        print("2. Ver playlist completa de um usuário")
        print("3. Conteúdo na posição N da playlist)")
        print("4. Interseção de playlists (N usuários)")
        print("5. Dados de um conteúdo (rating, duração, gêneros, plataformas, data, execuções)")
        print("6. Conteúdos de um gênero")
        print("7. Enfileirar conteúdo na fila de reprodução")
        print("8. Tocar próximo da fila")
        print("9. Ver fila atual")
        print("0. Sair")
        opcao = input("Informe a opção desejada: ")

        if opcao == "0":
            break
        elif opcao == "1":
            opcao_1(catalogo)
        elif opcao == "2":
            opcao_2(catalogo)
        elif opcao == "3":
            opcao_3(catalogo)
        
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
