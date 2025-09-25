from time import sleep
from os import system
import json

def continuar():
        system('cls')
        print('Opção inválida. Tente novamente.')
        sleep(0.5)
        system('cls')



class Livro:
    def __init__(self, nome, autores, genero):
        self.__nome = nome
        self.__autores = autores
        self.__genero = genero

    # Decorador que permite o acesso do método nome como propriedade, para acessar nome
    # (indiretamente) no código principal.
    @property  
    def nome(self):
        return self.__nome
    
    # Setter permite que o valor recebido de nome (no código principal) seja atrobuído
    # Na instância da classe.
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    

    @property  
    def autores(self):
        return self.__autores
    
    @autores.setter
    def nome(self, autores):
        self.__autor = autores
    

    @property  
    def genero(self):
        return self.__genero
    
    @genero.setter
    def nome(self, genero):
        self.__genero = genero



class Biblioteca:
    def pegarJSON(): 
        try:
            livros = []
            with open('orientado-a-objeto/db.json', 'r', encoding='utf-8') as file:
                data = (json.load(file))

            for dicts in data:
                for key in dicts:
                    livros.append(key)

            return data, livros
        
        except json.decoder.JSONDecodeError:

            return [], []


    def adicionarAoJSON(data):
        with open('orientado-a-objeto/db.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def cadastrar(nome, autores, genero):
        novoLivro = Livro(nome, autores, genero)
        system('cls')    
        print(f'Novo livro cadastrado: {novoLivro}')
        sleep(1)
        system('cls')


    def editar():
        print('Editor de livros cadastrados''\n')


    def remover():
        while True:
            print('Deleção de livro cadastrado''\n')
