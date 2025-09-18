from time import sleep
from os import system
import json

def continuar():
    system('cls')
    print('Opção inválida. Tente novamente')
    sleep(0.5)
    system('cls')


def pegarJSON():
    try:
        livros = []
        
        with open('projeto-final/db.json', 'r', encoding='utf-8') as file:
            data = (json.load(file))
        
        # Armazena todas as keys (nomes dos livros) em um dict, para acesso mais fácil nas outras funções
        for dicts in data:
            for key in dicts:
                livros.append(key)
        
        return data, livros
    
    except json.decoder.JSONDecodeError:
        # Retorna as duas listas vazias, correspondentes a lista de dicionários e a lista de chaves.
        # Forma mais fácil de tratar do que retornando False, pois permite a criação fácil de novas categorias no JSON
        # Permite um menu diferete em 'modificar' caso a lista data esteja vazia
        # E permite que o tratamento seja mais conciso.
        return [], []


def adicionarAoJSON(data):
    with open('projeto-final/db.json', 'w', encoding='utf-8') as file:
        # Data sempre será uma lista, logo ele irá adicionar os valores à lista mesmo que ela se inicializar vazia
        # Facilidade de manutenção e padronização das escritas
        json.dump(data, file, ensure_ascii=False, indent=4)


def pegarNome():
    nome = (input('Digite o título do livro: ').title()).strip()
    return nome


def pegarAutores():
    autores = []
    c = 1
    
    while True:
        system('cls')
        autor = (input(f'Digite o nome do {c}° autor do livro (enter para parar): ').title()).strip()
        if autor != '':
            autores.append(autor)
            c += 1
            continue
        elif (autor == '') and (autores != []):
            system('cls')
            print('Todos os autores foram cadastrados.')
            return autores
        else:
            continuar()
            continue


def cadastrar():
    data, livros = pegarJSON()
    autores = []
    c = 1
    
    while True:
        system('cls')
        print('Menu de cadastro de livros''\n')

        while True:
            system('cls')
            nome = pegarNome()
            if nome in livros:
                print('Esse nome já foi usado em outro livro. Insira outro.')
                sleep(1)
                continue
            else:
                break

        autores = pegarAutores()
        
        system('cls')
        genero = (input('Digite o gênero do livro: ').title()).strip()
        novoLivro = {nome : [autores, genero]}
        data.append(novoLivro)
        adicionarAoJSON(data)
    
        break

    system('cls')    
    print(f'Novo livro cadastrado: {novoLivro}')
    sleep(1)


def editar():
    while True:

        data, livros = pegarJSON()
        print('Editor de livros cadastrados''\n')

        for i in range(len(livros)):
            print(f'{i + 1} - (Livro) {livros[i]}')
        print(f'{i + 2} - Voltar ao menu principal''\n')

        opt = input('Escolha o que deseja fazer: ').strip()

        # Lógica emprestada do jogo da forca, pega a opção e tenta transformar em int para match com o livro certo.
        # Caso esteja fora do escopo (1 - i + 1) entrará no erro de valor também
        try:
            opt = int(opt)
            if (opt < 1) or (opt > (i + 2)):
                raise ValueError
            
        except ValueError:
            continuar()
            continue

        if opt < (i + 2):
            while True:
                system('cls')
                print(f'Editando livro: {livros[opt - 1]}''\n')
                print('1 - Editar autor(es)')
                print('2 - Editar gênero')
                print('3 - Editar tudo (substituir livro)')
                print('4 - Voltar ao menu de seleção de livros')
                opt2 = input('\n''Escolha o que deseja fazer: ').strip()

                match opt2:
                    case '1':
                        data[opt - 1].get(livros[opt - 1])[0] = pegarAutores()
                        adicionarAoJSON(data)
                        break

                    case '2':
                        system('cls')
                        data[opt - 1].get(livros[opt - 1])[1] = (input('Digite o gênero do livro: ').title()).strip()
                        adicionarAoJSON(data)
                        break

                    case '3':
                        data.pop(opt - 1)
                        data.insert(opt - 1, cadastrar())
                        adicionarAoJSON(data)
                        break

                    case '4':
                        print('Retornando ao menu de seleção de livros.')
                        sleep(0.5)
                        break

                    case _:
                        continuar()
                        continue
        else:
            print('Retornando ao menu principal')
            sleep(0.5)
            break


def remover():
    # Mesma lógica de editar() - Poderia ser função, mas falta tempo
    # Crime de guerra

    while True:
        data, livros = pegarJSON()
        print('Deleção de livro cadastrado''\n')

        for i in range(len(livros)):
            print(f'{i + 1} - (Livro) {livros[i]}')
        print(f'{i + 2} - Voltar ao menu principal''\n')

        opt = input('Escolha que livro deseja deletar: ').strip()

        # Lógica emprestada do jogo da forca, pega a opção e tenta transformar em int para match com o livro certo.
        # Caso esteja fora do escopo (1 - i + 1) entrará no erro de valor também
        try:
            opt = int(opt)
            if (opt < 1) or (opt > (i + 2)):
                raise ValueError
            
        except ValueError:
            system('cls')
            print('Opção inválida. Tente novamente.')
            sleep(0.5)
            system('cls')
            continue

        if opt < (i + 2):
            while True:
                system('cls')
                print(f'Deletando livro: {livros[opt - 1]}''\n')
                opt2 = (input('Tem certeza que deseja deletar o livro? (s/n): ').lower()).strip()

                match opt2:
                    case 's':
                        system('cls')
                        print('Deletando livro.')
                        sleep(0.5)

                        data.pop(opt - 1)

                        system('cls')
                        print('Livro deletado.')
                        adicionarAoJSON(data)
                        break

                    case 'n':
                        system('cls')
                        print('Retornando ao menu de deleção.')
                        sleep(0.5)
                        break

                    case _:
                        continuar()
                        continue
        else:
            print('Retornando ao menu principal')
            sleep(0.5)
            break


def main():
    while True:
        data, livros = pegarJSON()

        system('cls')
        print('Bem-vindo ao gerenciador de livros da biblioteca!''\n')
        print('1 - Visualizar livros cadastrados')
        print('2 - Cadastrar novo livro')
        print('3 - Editar informações de um livro')
        print('4 - Remover livro')
        print('5 - Sair')
        opt = input('\n''Escolha o que deseja fazer: ').strip()

        match opt:
            case '1':
                system('cls')
                if livros != []:
                    for livro in data:
                        for nome in livro:
                            print(f'Livro: {nome}')
                            print(f'Autor(es): {livro.get(nome)[0]}')
                            print(f'Gênero: {livro.get(nome)[1]}''\n')
                    
                    sleep(5)
                    continue
                # Crime
                else:
                    print('Não há livros cadastrados. Cadastre um livro antes de prosseguir.')
                    sleep(0.5)
                    continue

            case '2':
                system('cls')
                cadastrar()

            case '3':
                system('cls')
                if livros != []:
                    editar()
                # Crime
                else:
                    print('Não há livros cadastrados. Cadastre um livro antes de prosseguir.')
                    sleep(0.5)
                    continue

            case '4':
                system('cls')
                if livros != []:
                    remover()
                # Crime
                else:
                    print('Não há livros cadastrados. Cadastre um livro antes de prosseguir.')
                    sleep(0.5)
                    continue

            case '5':
                system('cls')
                print('Adeus, amigo.')
                break

            case _:
                continuar()
                continue


main()

