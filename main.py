from biblioteca import Biblioteca

def exibir_tabela(lista):
    if not lista:
        print("\nNenhum livro cadastrado!")
        return

    largura_cod = max(max(len(str(l.codigo)) for l in lista), 6)
    largura_titulo = max(max(len(str(l.titulo)) for l in lista), 6)
    largura_autor = max(max(len(str(l.autor)) for l in lista), 5)
    largura_ano = max(max(len(str(l.ano)) for l in lista), 4)
    largura_status = 12

    cabecalho = f"| {'Código':<{largura_cod}} | {'Título':<{largura_titulo}} | {'Autor':<{largura_autor}} | {'Ano':<{largura_ano}} | {'Status':<{largura_status}} |"
    divisor = f"|{'-' * (largura_cod + 2)}|{'-' * (largura_titulo + 2)}|{'-' * (largura_autor + 2)}|{'-' * (largura_ano + 2)}|{'-' * (largura_status + 2)}|"

    print("\n" + divisor)
    print(cabecalho)
    print(divisor)
    for livro in lista:
        status_str = "Disponível" if livro.disponivel else "Emprestado"
        print(f"| {str(livro.codigo):<{largura_cod}} | {livro.titulo:<{largura_titulo}} | {livro.autor:<{largura_autor}} | {str(livro.ano):<{largura_ano}} | {status_str:<{largura_status}} |")
        print(divisor)
    print()

def main():
    biblio = Biblioteca()

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
            biblio.adicionar_livro(titulo, autor, ano)
            print("\nLivro adicionado com sucesso!")

        elif escolha == "2":
            print("\n--- Remover Livro ---")
            termo = input("Digite o título ou o código do livro que deseja remover: ")
            if biblio.remover_livro(termo):
                print("\nLivro removido com sucesso!")
            else:
                print("\nLivro não encontrado!")

        elif escolha == "3":
            print("\n--- Buscar Livro ---")
            termo = input("Digite o título ou o código do livro que deseja buscar: ")
            encontrados = biblio.buscar_livro(termo)
            if encontrados:
                print("\nLivro(s) encontrado(s):")
                exibir_tabela(encontrados)
            else:
                print("\nLivro não encontrado!")

        elif escolha == "4":
            print("\n--- Lista de Livros Cadastrados ---")
            exibir_tabela(biblio.listar_livros())

        elif escolha == "5":
            print("\n--- Emprestar Livro ---")
            termo = input("Digite o título ou o código do livro para emprestar: ")
            mensagem = biblio.emprestar_livro(termo)
            print(mensagem)

        elif escolha == "6":
            print("\n--- Devolver Livro ---")
            termo = input("Digite o título ou o código do livro para devolver: ")
            mensagem = biblio.devolver_livro(termo)
            print(mensagem)

        elif escolha == "7":
            print("\nObrigado por usar o BiblioPy. Até logo!")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()
