import json

def main():
    with open("gabarito_publico.json", "r", encoding="utf-8") as f:
        gabarito = json.load(f)

    with open("respostas.json", "r", encoding="utf-8") as f:
        respostas = json.load(f)

    acertos = 0
    erros = []
    ausentes = []

    for chave, esperado in gabarito.items():
      if chave not in respostas:
          ausentes.append(chave)
          continue

        obtido = respostas[chave]

    if isinstance(esperado, float) and isinstance(obtido, (int, float)):
      correto = abs(esperado - obtido) < 1e-6
    else:
      correto = esperado == obtido

    if correto:
      acertos += 1
    else:
      erros.append((chave, esperado, obtido))

    total = len(gabarito)
    print(f"{acertos}/{total} corretas")

    if ausentes:
        print("\nAusentes (não geradas):")
        for chave in ausentes:
            print(f"  id {chave}")

    if erros:
        print("\nErradas:")
        for chave, esperado, obtido in erros:
            print(f"  id {chave}: esperado {esperado!r}, obtido {obtido!r}")

if __name__ == "__main__":
    main()

feat: adiciona conferir.py
