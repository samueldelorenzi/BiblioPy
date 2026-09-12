import json
import os
from livro import Livro

class Biblioteca:
    def __init__(self):
        self.arquivo = "acervo.json"
        self.livros = []
        self.carregar_dados()

    def adicionar_livro(self, titulo: str, autor: str, ano: int) -> Livro:
        codigo = 1 if not self.livros else max(l.codigo for l in self.livros) + 1
        novo_livro = Livro(codigo, titulo, autor, ano)
        self.livros.append(novo_livro)
        self.salvar_dados()
        return novo_livro

    def remover_livro(self, termo: str) -> bool:
        for livro in self.livros:
            if str(livro.codigo) == termo or livro.titulo.lower() == termo.lower():
                self.livros.remove(livro)
                self.salvar_dados()
                return True
        return False

    def buscar_livro(self, termo: str) -> list[Livro]:
        encontrados = []
        for livro in self.livros:
            if str(livro.codigo) == termo or termo.lower() in livro.titulo.lower():
                encontrados.append(livro)
        return encontrados

    def listar_livros(self) -> list[Livro]:
        return self.livros
        
    def emprestar_livro(self, termo: str) -> str:
        for livro in self.livros:
            if str(livro.codigo) == termo or termo.lower() in livro.titulo.lower():
                if livro.emprestar():
                    self.salvar_dados()
                    return f"\nLivro {livro.titulo} emprestado com sucesso"
                else:
                    return f"\nO livro {livro.titulo} já está emprestado"
        return "\nLivro não encontrado!"

    def devolver_livro(self, termo: str) -> str:
        for livro in self.livros:
            if str(livro.codigo) == termo or termo.lower() in livro.titulo.lower():
                if livro.devolver():
                    self.salvar_dados()
                    return f"\nLivro {livro.titulo} devolvido com sucesso"
                else:
                    return f"\nO livro {livro.titulo} não está emprestado"
        return "\nLivro não encontrado!"

    def carregar_dados(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.livros = [Livro.from_dict(d) for d in dados]
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def salvar_dados(self):
        try:
            dados = [livro.to_dict() for livro in self.livros]
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
