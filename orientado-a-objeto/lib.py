from time import sleep
from os import system
from classes import Biblioteca

def continuar(mensagem):
    system('cls')
    print(mensagem)
    sleep(1)
    system('cls')
    

def pegarSTR(mensagem, erro):
    while True:
        string = (input(mensagem).title()).strip()
        
        if string == '':
            continuar(erro)
        else:
            return string


def pegarAutores():
    autores = []
    c = 1
    
    while True:
        system('cls')
        autor = (input(f'Insira o {c}° autor do livro (enter para parar): ').title()).strip()
        
        if autor != '':
            autores.append(autor)
            c += 1
            continue
        elif (autor == '') and (c == 1):
            continuar('Valor inválido. Insira pelo menos um autor.')
            continue
        else:
            continuar('Todos os autores cadastrados.')
            return autores      


def cadastrar(id=None, staticID=False, mode='append'):
    lib = Biblioteca()
    
    system('cls')
    print('--- Menu de Cadastro de Livro --- \n')
    nome = pegarSTR('Insira o nome do livro: ', 'Nome inválido. Tente novamente.')
    autores = pegarAutores()
    genero = pegarSTR('Insira o gênero do livro: ', 'Valor inválido. Tente novamente.')
    
    if staticID == True:
        lib.cadastrarLivro(nome, autores, genero, id, mode='replace')
    else:
        lib.cadastrarLivro(nome, autores, genero)
    
    print(f'Nome: {nome}')
    print(f'Autores: {autores}') 
    print(f'Gênero: {genero}')
    print('Livro cadastrado com sucesso!')
    sleep(1)
            
            
def visualizar(returnID=False):
    lib = Biblioteca()
    if returnID == False:
        lib.visualizarLivros()
    else:
        id = lib.visualizarLivros(returnID=True)
        return id
    
    
def editar():
    lib = Biblioteca()
    
    while True:
        system('cls')
        print('--- Menu de Edição de Livro --- \n')
        id = visualizar(returnID=True)
        print(f'{id + 1}: Retornar ao menu principal \n')
        opt = input('Escolha o que deseja fazer: ')
        
        try:
            opt = (int(opt))
            if (opt < 0) or (opt > (id + 1)):
                raise ValueError  
        except ValueError:
            continuar('Valor inválido. Por favor, tente novamente.')
            continue
            
        if opt < (id + 1):
            while True:
                system('cls')
                print(f'Editando livro: {lib.IDParaInfo(opt)}')
                print('1 - Editar nome do livro')
                print('2 - Editar autores do livro')
                print('3 - Editar gênero do livro')
                print('4 - Editar tudo (recadastrar livro)')
                print('5 - Retornar ao Menu Principal \n')

                opt2 = input('Escolha o que deseja fazer: ').strip()

                match opt2:
                    case '1':
                        system('cls')
                        nome = pegarSTR('Insira o nome do livro: ', 'Nome inválido. Por favor, tente novamente.')
                        lib.editarLivros(opt, nome, 'nome')
                        continuar('Nome do livro alterado com sucesso!')
                        break              
                    case '2':
                        system('cls')
                        autores = pegarAutores()
                        lib.editarLivros(opt, autores, 'autores')
                        break
                    case '3':
                        system('cls')
                        genero = pegarSTR('Insira o gênero do livro: ', 'Valor inválido. Por favor, tente novamente.')
                        lib.editarLivros(opt, genero, 'genero')
                        continuar('Gênero do livro alterado com sucesso!')
                        break
                    case '4':
                        cadastrar(opt, staticID=True, mode='replace')
                        break
                    case '5':
                        continuar('Retornando ao menu principal.')
                        break
                    case _:
                        continuar('Valor inválido. Por favor, tente novamente.')
                        continue
        elif opt == (id + 1):
            continuar('Retornando ao menu principal.')
            break
        else:
            continuar('Valor inválido. Por favor, tente novamente.')
            continue
        
        break
    

def remover():
    lib = Biblioteca()
    
    while True:
        system('cls')
        print('--- Menu de Deleção de Livro --- \n')
        id = visualizar(returnID=True)
        print(f'{id + 1}: Retornar ao menu principal \n')
        
        opt = input('Escolha o livro que deseja deletar: ')
        
        try:
            opt = (int(opt))
            if (opt < 0) or (opt > (id + 1)):
                raise ValueError  
        except ValueError:
            continuar('Valor inválido. Por favor, tente novamente.')
            continue
            
        if opt < (id + 1):
            while True:
                system('cls')
                print(f'{lib.IDParaInfo(opt)}')
                opt2 = (input('Tem certeza que deseja deletar o livro? (s/n): ').lower()).strip()

                match opt2:
                    case 's':
                        print(f'Deletando o livro: {lib.IDParaInfo(opt)}...')
                        lib.deletarLivro(opt)
                        continuar('Livro deletado com sucesso!')
                        break
                        
                    case 'n':
                        continuar('Operação cancelada. Retornando ao menu principal.')
                        break
                        
                    case _:
                        continuar('Valor inválido. Por favor, tente novamente.')
                        continue
                        

        elif opt == (id + 1):
            continuar('Retornando ao menu principal.')
            break
        else:
            continuar('Valor inválido. Por favor, tente novamente.')
            continue
        
        break
    
        
def main():
    while True:
        lib = Biblioteca()

        system('cls')
        if lib.data == []:
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
                continuar('Valor inválido. Por favor, tente novamente.')
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
                    lib.visualizarLivros()
                    sleep(8)
                    continue
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
                    continuar('Valor inválido. Por favor, tente novamente.')
                    continue


main()