"""A classe Catalogo. Leia o README.md antes de começar.

Esta é a peça central do projeto: carrega o JSON uma vez, constrói os
índices no __init__ e expõe os 16 métodos que o main.py e o cli.py usam.
"""
import json
from collections import deque

class Catalogo:
    def __init__(self, caminho_json: str): 
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        self.conteudos = {}
        for conteudo in dados["conteudos"]:
            self.conteudos[conteudo["id"]] = conteudo

        self.usuarios = {}
        for usuario in dados["usuarios"]:
            self.usuarios[usuario["id"]] = usuario

        self.fila = deque()

    # --- usuários e playlists ---
    def listar_usuarios(self) -> list[str]: 
        nomes = []
        for usuario in self.usuarios.values():
            nomes.append(usuario["nome"])
        nomes.sort()
        return nomes

    
    def buscar_usuario_por_nome(self, nome: str) -> str | None:
        for usuario in self.usuarios.values():
            if usuario["nome"].lower() == nome.lower():
                return usuario["id"]

        return None

        
    def playlist_de(self, usuario_id: str) -> list[str] | None: 
        for usuario in self.usuarios.values():
            if usuario["id"] == usuario_id:
                return usuario["playlist"]
    
        return None
        
        
    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None: 
        playlist = self.playlist_de(usuario_id)
    
        if playlist is None:
            return None
    
        if posicao < 0 or posicao >= len(playlist):
            return None
    
        return playlist[posicao]

    
    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]: 
        playlists = []
        for usuario_id in usuario_ids:
            playlist = self.playlist_de(usuario_id)
            if playlist is None:         
                return []
            playlists.append(set(playlist))

        resultado = playlists[0]
        for p in playlists[1:]:
            resultado = resultado & p    

        return sorted(resultado)

    
    # --- dados de um conteúdo ---
    def rating_de(self, conteudo_id: str) -> float | None: 
        conteudo = self.conteudos.get(conteudo_id)
        if conteudo is None:
            return None
        if "rating" not in conteudo:
            return None
        rating = conteudo["rating"]
        if isinstance(rating, str):
            rating = float(rating)
        return rating

    
    def duracao_total_de(self, conteudo_id: str) -> int | None: 
        conteudo = self.conteudos.get(conteudo_id)
        if conteudo is None:
            return None
        if conteudo["tipo"] == "musica":
            return conteudo["duracao_seg"]
        total = 0
        for faixa in conteudo["faixas"]:
            if faixa["duracao_seg"] is not None:   
                total += faixa["duracao_seg"]
        return total

    
    def generos_de(self, conteudo_id: str) -> list[str] | None: 
        conteudo = self.conteudos.get(conteudo_id)
        if conteudo is None:
            return None

        def achatar(item):
            if isinstance(item, str):
                return [item]
            resultado = []
            for sub in item:
                resultado.extend(achatar(sub))
            return resultado

        return sorted(achatar(conteudo["generos"]))

    
    def plataformas_de(self, conteudo_id: str) -> list[str] | None: 
        conteudo = self.conteudos.get(conteudo_id)
        if conteudo is None:
            return None
        return sorted(conteudo.get("plataformas", []))


    def data_adicionado_de(self, conteudo_id: str) -> str | None: 
        conteudo = self.conteudos.get(conteudo_id)
        if conteudo is None:
            return None
        data = conteudo["data_adicionado"]
        if "/" in data:                   
            dia, mes, ano = data.split("/")
            data = f"{ano}-{mes}-{dia}"
        return data


    def execucoes_de(self, conteudo_id: str) -> int | None: 
        conteudo = self.conteudos.get(conteudo_id)
        if conteudo is None:
            return None
        execucoes = conteudo["engajamento"]["execucoes"]
        if isinstance(execucoes, str):
            execucoes = int(execucoes.replace(",", ""))
        return execucoes


    def conteudos_do_genero(self, genero: str) -> list[str]: 
        ids = []
        for conteudo_id in self.conteudos:
            generos = self.generos_de(conteudo_id)
            if genero in generos:
                ids.append(conteudo_id)
        return sorted(ids)


    # --- fila de reprodução ---
    def enfileirar(self, conteudo_id: str) -> bool: 
        if conteudo_id not in self.conteudos:
            return False
        self.fila.append(conteudo_id)
        return True


    def proximo(self) -> str | None:
        if len(self.fila) == 0:
            return None
        return self.fila.popleft()

        
    def fila_atual(self) -> list[str]: 
        return list(self.fila)


    def nome_conteudo(self, conteudo_id):
        conteudo = self.conteudos.get(conteudo_id)

        if conteudo is None:
            return None

        titulo = conteudo["titulo"]
        artista = conteudo["artista"]
        tipo = conteudo["tipo"]

        return f"{titulo}, de {artista} ({tipo})"


    def buscar_conteudo_por_titulo_artista(self, titulo: str, artista: str) -> str | None:
        for conteudo_id, conteudo in self.conteudos.items():
            if conteudo["titulo"].lower() == titulo.lower() and conteudo["artista"].lower() == artista.lower():
                return conteudo_id
        return None
