"""Modo batch: lê consultas.json, responde em ordem, grava respostas.json.

Uso: python main.py consultas.json respostas.json
"""
import json
import sys
from catalogo import Catalogo

def main():
    caminho_consultas = sys.argv[1]
    caminho_respostas = sys.argv[2]

    catalogo = Catalogo("catalogo_final.json")

    with open(caminho_consultas, "r", encoding="utf-8") as f:
        dados = json.load(f)

    consultas = dados["consultas"]
    respostas = {}

    for consulta in consultas:
        id_consulta = str(consulta["id"])
        tipo = consulta["tipo"]
        parametros = consulta["parametros"]

        metodo = getattr(catalogo, tipo)
        resultado = metodo(**parametros)

        respostas[id_consulta] = resultado

    with open(caminho_respostas, "w", encoding="utf-8") as f:
        json.dump(respostas, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
