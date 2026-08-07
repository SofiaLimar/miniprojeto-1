"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
import sys
from catalogo import Catalogo

def main():
  caminho = sys.argv[1]            
  catalogo = Catalogo(caminho)      

  while True:
    print("1. Listar todos os usuários")
    print("0. Sair")
    opcao = input("Informe a opção desejada: ")

    if opcao == "0":
      break
    elif opcao == "1":
      resultado = catalogo.listar_usuarios()
      print(resultado)
    else:
      print("Opção inválida")

if __name__ == "__main__":
    main()
