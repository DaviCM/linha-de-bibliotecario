from time import sleep
from os import system
from classes import Biblioteca
import json

# Função básica, que utiliza os comandos de CLI para limpar a tela.
# Utilizado para gegar erro genérico em muitos lugares do código.
def continuar():
    system('cls')
    print('Opção inválida. Tente novamente.')
    sleep(0.5)
    system('cls')


def pegarSTR(inputValue):
    string = (input(inputValue).title()).strip()
    return string


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


def main():
    while True:
        data, livros = Biblioteca.pegarJSON()
        system('cls')

        if livros == []:
            opt = (input('A lista de livros está vazia. Deseja cadastrar um livro? (s/n): ').lower()).strip()
            if opt == 's':
                system('cls')
                Biblioteca.cadastrar()
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

                    sleep(5)
                    continue

                case '2':
                    system('cls')
                    
                    continue
                case '3':
                    system('cls')
                    
                    continue
                case '4':
                    system('cls')
                    
                    continue
                case '5':
                    system('cls')
                    print('Adeus, amigo.')
                    break
                case _:
                    continuar()
                    continue


main()

