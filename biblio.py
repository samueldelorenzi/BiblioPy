# Aplicativo de gerência de biblioteca comunitária
# Desenvolvedor: Samuel De Lorenzi Ribeiro
import os
from enum import IntEnum

class StatusLivro(IntEnum):
    DISPONIVEL = 1
    EMPRESTADO = 2

def carregar_livros():
    livros = []
    if os.path.exists("livros.csv"):
        with open("livros.csv", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(";")
                    if len(partes) >= 5:
                        try:
                            livros.append({
                                "codigo": int(partes[0]),
                                "titulo": partes[1],
                                "autor": partes[2],
                                "ano": partes[3],
                                "status": int(partes[4])
                            })
                        except ValueError:
                            pass
    return livros

def salvar_livros():
    with open("livros.csv", "w", encoding="utf-8") as f:
        for livro in livros:
            f.write(f"{livro['codigo']};{livro['titulo']};{livro['autor']};{livro['ano']};{livro['status']}\n")

def exibirTabela(lista):
    if not lista:
        print("\nNenhum livro cadastrado!")
        return

    largura_cod = max(max(len(str(l["codigo"])) for l in lista), 6)
    largura_titulo = max(max(len(str(l["titulo"])) for l in lista), 6)
    largura_autor = max(max(len(str(l["autor"])) for l in lista), 5)
    largura_ano = max(max(len(str(l["ano"])) for l in lista), 4)
    largura_status = 12

    cabecalho = f"| {'Código':<{largura_cod}} | {'Título':<{largura_titulo}} | {'Autor':<{largura_autor}} | {'Ano':<{largura_ano}} | {'Status':<{largura_status}} |"
    divisor = f"|{'-' * (largura_cod + 2)}|{'-' * (largura_titulo + 2)}|{'-' * (largura_autor + 2)}|{'-' * (largura_ano + 2)}|{'-' * (largura_status + 2)}|"

    print("\n" + divisor)
    print(cabecalho)
    print(divisor)
    for livro in lista:
        status_str = "Disponível" if livro["status"] == StatusLivro.DISPONIVEL.value else "Emprestado"
        print(f"| {str(livro['codigo']):<{largura_cod}} | {str(livro['titulo']):<{largura_titulo}} | {str(livro['autor']):<{largura_autor}} | {str(livro['ano']):<{largura_ano}} | {status_str:<{largura_status}} |")
        print(divisor)
    print()

def adicionarLivro():
    print("\n--- Adicionar Livro ---")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    
    while True:
        try:
            ano = input("Digite o ano de lançamento do livro: ")
            ano = int(ano)
            break
        except ValueError:
            print("Erro: O ano deve ser um número inteiro. Tente novamente.")
            
    codigo = 1
    if livros:
        codigo = max(livro["codigo"] for livro in livros) + 1
        
    livros.append({
        "codigo": codigo,
        "titulo": titulo, 
        "autor": autor, 
        "ano": str(ano),
        "status": StatusLivro.DISPONIVEL.value
    })
    salvar_livros()
    print("\nLivro adicionado com sucesso!")

def removerLivro():
    print("\n--- Remover Livro ---")
    titulo = input("Digite o título ou o código do livro que deseja remover: ")
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower() or str(livro["codigo"]) == titulo:
            livros.remove(livro)
            salvar_livros()
            print("\nLivro removido com sucesso!")
            return
    print("\nLivro não encontrado!")

def buscarLivro():
    print("\n--- Buscar Livro ---")
    titulo = input("Digite o título ou o código do livro que deseja buscar: ")
    encontrados = [livro for livro in livros if titulo.lower() in livro["titulo"].lower() or str(livro["codigo"]) == titulo]
    if encontrados:
        print("\nLivro(s) encontrado(s):")
        exibirTabela(encontrados)
    else:
        print("\nLivro não encontrado!")

def listarLivros():
    print("\n--- Lista de Livros Cadastrados ---")
    exibirTabela(livros)

def emprestarLivro():
    print("\n--- Emprestar Livro ---")
    titulo = input("Digite o título ou o código do livro para emprestar: ")
    for livro in livros:
        if titulo.lower() in livro["titulo"].lower() or str(livro["codigo"]) == titulo:
            if livro["status"] == StatusLivro.EMPRESTADO.value:
                print(f"\nO livro {livro['titulo']} já está emprestado")
            else:
                livro["status"] = StatusLivro.EMPRESTADO.value
                salvar_livros()
                print(f"\nLivro {livro['titulo']} emprestado com sucesso")
            return
    print("\nLivro não encontrado!")

def devolverLivro():
    print("\n--- Devolver Livro ---")
    titulo = input("Digite o título ou o código do livro para devolver: ")
    for livro in livros:
        if titulo.lower() in livro["titulo"].lower() or str(livro["codigo"]) == titulo:
            if livro["status"] == StatusLivro.DISPONIVEL.value:
                print(f"\nO livro {livro['titulo']} não está emprestado")
            else:
                livro["status"] = StatusLivro.DISPONIVEL.value
                salvar_livros()
                print(f"\nLivro {livro['titulo']} devolvido com sucesso")
            return
    print("\nLivro não encontrado!")

livros = carregar_livros()

print("=============================================================================")
print("Bem-vindo ao BiblioPy. Aplicativo de gerenciamento de biblioteca comunitária.")
print("=============================================================================")

while True:
    print("\nMenu de Opções:")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Buscar livro")    
    print("4. Listar livros")
    print("5. Emprestar livro")
    print("6. Devolver livro")
    print("7. Sair")

    escolha = input("\nDigite o número da opção desejada: ")

    if escolha == "1":
        adicionarLivro()
    elif escolha == "2":
        removerLivro()
    elif escolha == "3":
        buscarLivro()
    elif escolha == "4":
        listarLivros()
    elif escolha == "5":
        emprestarLivro()
    elif escolha == "6":
        devolverLivro()
    elif escolha == "7":
        print("\nObrigado por usar o BiblioPy. Até logo!")
        break
    else:
        print("\nOpção inválida.")
