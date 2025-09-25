from time import sleep
from os import system
import json

# Função básica, que utiliza os comandos de CLI para limpar a tela.
# Utilizado para gegar erro genérico em muitos lugares do código.
def continuar():
    system('cls')
    print('Opção inválida. Tente novamente.')
    sleep(0.5)
    system('cls')


# Função que abre o JSON em uma variável e retorna ela, junto com uma lista que contém os nomes dos livros
def pegarJSON(): 
    try:
        livros = []
        # Adicionar o arquivo JSON à uma lista 'data', que contém todos os dicts
        with open('procedural/db.json', 'r', encoding='utf-8') as file:
            data = (json.load(file))
        
        # Armazena todas as keys (nomes dos livros) em uma lista 'livros', para acesso mais fácil nas outras funções
        # Primiero loop: itera sobre cada dicionário da lista de dicts
        # Segundo loop: Dentro desse dicionário, irá iterar sobre seu índice e o armazenar na lista 'livros'.
        for dicts in data:
            for key in dicts:
                livros.append(key)
        
        # As outras funções recebem essa tupla para manipular os dados, sempre no início dos loops de execução delas.
        # E desemapcotam a tupla em vars
        return data, livros
    
    except json.decoder.JSONDecodeError:
        # Retorna as duas listas vazias, correspondentes às listas de dicionários e de lista de chaves.
        # Forma mais fácil de tratar do que retornando False, pois 'data' nas outras funções recebe []
        # Logo, os livros serão adicionados a ela normalmente.
        return [], []


# Recebe uma lista 'data' e adiciona ela ao JSON com W, reescrevendo toda a DB.
# Melhor que append, pois ele adiciona uma outra lista e altera a indentação.
def adicionarAoJSON(data):
    with open('procedural/db.json', 'w', encoding='utf-8') as file:
        # Data sempre será uma lista, logo ele irá adicionar os valores à lista mesmo que ela se inicializar vazia
        # Facilidade de manutenção e padronização das escritas
        json.dump(data, file, ensure_ascii=False, indent=4)


# Usada para pegar nome e gênero do livro.
def pegarSTR(inputValue):
    string = (input(inputValue).title()).strip()
    return string


# Lógica para armazenar múltiplos autores em uma lista com visualização agradável para o usuário
def pegarAutores():
    autores = []
    c = 1 # Contador
    
    while True:
        system('cls')
        autor = (input(f'Digite o nome do {c}° autor do livro (enter para parar): ').title()).strip()
        # Se for diferente de enter, irá adicionar o valor à lista e seguir para a próxima iteração.
        if autor != '':
            autores.append(autor)
            c += 1
            continue
        # Se autor == enter e a lista estiver com algom valor, finaliza a execução e retorna.
        elif (autor == '') and (autores != []):
            system('cls')
            print('Todos os autores foram cadastrados.')
            return autores
        # Se autor == enter e a lista estiver vazia, apenas envia a mensagem padrão de erro.
        else:
            continuar()
            continue


# Função que cadastra um livro, com estrutura de dict.
# Parâmetro de retorno defaulta para False, já que só preciso dele uma vez (editar())
def cadastrar(retornar=False):
    data, livros = pegarJSON()
    autores = []
    
    while True:
        system('cls')
        print('Menu de cadastro de livros''\n')

        while True:
            system('cls')
            nome = pegarSTR('Digite o título do livro: ')
            # Se o nome inserido já estiver na lista, quebra
            # Só pode haver um livro com cada nome.
            if nome in livros:
                print('Esse nome já foi usado em outro livro. Insira outro.')
                sleep(1)
                continue
            else:
                break

        autores = pegarAutores()
        
        system('cls')
        genero = pegarSTR('Digite o gênero do livro: ')

        # Objeto dicionário que contém as informações obtidas do livro
        novoLivro = {nome : [autores, genero]}
        break

    system('cls')    
    print(f'Novo livro cadastrado: {novoLivro}')
    sleep(1)
    system('cls')

    # Se o valor de retorno for falso,irá seguir o normal e adicionar o livro ao JSON
    if retornar == False:
        data.append(novoLivro)
        adicionarAoJSON(data)
    # Se for verdadeiro, apenas retornará o novo livro
    # função editar() precisa d valor de retorno, para substituir na posição específica.
    else:
        return novoLivro


# Função que edita livros, apenas utilizando as funções anteriores
def editar():
    while True:

        data, livros = pegarJSON()
        print('Editor de livros cadastrados''\n')

        # Mostra as opções ao usuário imprimindo cada posição da lista de nomes
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
        
        # Se a escolha for bem sucedida
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
                        data[opt - 1].get(livros[opt - 1])[1] = pegarSTR('Digite o gênero do livro: ')
                        adicionarAoJSON(data)
                        break
                    case '3':
                        data[opt - 1] = cadastrar(retornar=True)
                        adicionarAoJSON(data)
                        sleep(0.5)
                        break
                    case '4':
                        print('Retornando ao menu de seleção de livros.')
                        sleep(0.5)
                        break
                    case _:
                        continuar()
                        continue
        else:
            system('cls')
            print('Retornando ao menu principal.')
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
            system('cls')
            print('Retornando ao menu principal.')
            sleep(0.5)
            break


# Função de execução, gera o menu inicial e redireciona o usuário para a função desejada
# A depender do input
def main():
    while True:
        data, livros = pegarJSON()

        system('cls')

        # Check para ver se a lista está vazia
        # Caso estiver, user pode apenas cadastrar um livro ou sair
        if livros == []:
            opt = (input('A lista de livros está vazia. Deseja cadastrar um livro? (s/n): ').lower()).strip()
            if opt == 's':
                system('cls')
                cadastrar()
                continue
            elif opt == 'n':
                system('cls')
                print('Adeus, amigo.')
                break
            else:
                continuar()
                continue
        else:
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

                    # Nested for loop, o primeiro itera sobre cada um dos dicts (livros) na lista
                    for livro in data:
                        # O segundo itera sobre as keys deles, e gera a visualização com os nome (key), autor (get() na posição 0)
                        # e gênero (get() na posição 1) para cada um dos livros.
                        for nome in livro:
                            print(f'Livro: {nome}')
                            print(f'Autor(es): {livro.get(nome)[0]}')
                            print(f'Gênero: {livro.get(nome)[1]}''\n')

                    sleep(5)
                    continue

                # A partir daqui, chama a função certa para cada opção do user.
                case '2':
                    system('cls')
                    cadastrar()
                    continue
                case '3':
                    system('cls')
                    editar()
                    continue
                case '4':
                    system('cls')
                    remover()
                    continue
                case '5':
                    system('cls')
                    print('Adeus, amigo.')
                    break
                case _:
                    continuar()
                    continue


main()

