from os import getcwd
import json

# Classe - descrição de um 'formato geral' que os objetos devem ter
# Atributos - as variáveis da classe, que são únicas para cada instância dela (características do objeto)
# Métodos - Funções, as ações que os objetos podem realizar

# self - 'nome da classe', porém referido apenas dentro dela mesma - usado para referenciar atributos de dentro.
# construtor - necessário para acessar os atributos da classe, ao criar um objeto.
# construtor é o __init__

# Os atributos podem ser encapsulados como:
# public - atributo público, pode ser acessado por todas as classes (sem underscore)
# private - atributo encapsulado e contido em uma única classe (__ antes do nome) - não será possível chamar a porpriedade diretamente.
# protect - envia um 'sinal de captura' para o acesso por outra classe ser permitido (_ antes do nome)

# @property - decorador que remove parênteses do chamado e retorna o valor que foi dado para o atributo
# '__atributo' no nosso init irá chamar nosso método getter para atualizar os atributos
# @atributo.setter - recebe o valor do getter no atributo da classe.

# Caminho do atributo: atribuição (criação do obj) - construtor - getter - setter
# A setter recebe o valor que foi atribuido na criação do objeto e iguala ele ao atributo.

class Livro:
    def __init__(self, nome, autores, genero, id):
        self.__id = id # Método getter
        self.__nome = nome
        self.__autores = autores
        self.__genero = genero
        
    
    # Declaração do getter
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id # id é a função getter, logo ele pega o valor da getter e atribui no parâmetro correto - ele 'seta'.
    
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def id(self, nome):
        self.__nome = nome
        
    
    @property
    def autores(self):
        return self.__autores
    
    @autores.setter
    def autores(self, autores):
        self.__autores = autores
        
    
    @property
    def genero(self):
        return self.__genero
    
    @id.setter
    def genero(self, genero):
        self.__genero = genero
        
    
    def getDict(self):
        return {self.__id : {'nome' : self.__nome, 'autores' : self.__autores, 'genero' : self.__genero}}
    


# OBS: 'id' SEMPRE irá se referir ao ID do livro no JSON, NUNCA à posição dele na lista (um index abaixo).
class Biblioteca:
    def __init__(self):
        self.__data = self.pegarJSON()
        
        
    @property
    def data(self):
        return self.__data
    
    
    def pegarJSON(self): 
        try:
            with open(f'{'orientado-a-objeto'}/db.json', 'r', encoding='utf-8') as file:
                self.__data = json.load(file)
                return self.__data

        except json.decoder.JSONDecodeError:
            return []


    def adicionarAoJSON(self, data):
        with open(f'{'orientado-a-objeto'}/db.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
    
    def pegarID(self):
        data = self.pegarJSON()
        id = 0
        
        if data != []:
            for dicts in data:
                for key in dicts:
                    id = int(key)
                
            return (str(id + 1))
        else:
            return 1
            

    def cadastrarLivro(self, nome, autores, genero, id=None, mode='append'):
        if id == None:
            id = self.pegarID()
        
        novoLivro = Livro(nome, autores, genero, id)
        
        if mode == 'replace':
            self.__data[id] = novoLivro.getDict()
            self.adicionarAoJSON(self.__data)
        else:
            self.__data.append(novoLivro.getDict())
            self.adicionarAoJSON(self.__data)
    
    
    def visualizarLivros(self, returnID=False):
        data = self.pegarJSON()
        
        if data != []:
            for dicts in data:
                for id in dicts:
                    print(f'Livro {id}: ')
                    print(f'Nome: {dicts[id]['nome']}')
                    print(f'Autores: {dicts[id]['autores']}')
                    print(f'Gênero: {dicts[id]['genero']} \n')
        else:
            print('Não há nenhum livro cadastrado.')
            
        if returnID == True:
            return int(id)
        
        
    def IDParaInfo(self, id, autores=False, genero=False):
        data = self.pegarJSON()
        
        for dicts in data:
            if str(id) in dicts: # Preciso checar se o id fornecido é key, para poder manipular
                                # caso contrário, teria que manipular com um intervalo fixo - o que gera conflito
                                # com IDs que não são subsequentes.
                if autores == True:
                    return dicts[str(id)]['autores']
                elif genero == True:
                    return dicts[str(id)]['genero']
                else:
                    return dicts[str(id)]['nome']

    
    def editarLivros(self, id, modified, toEdit):
        data = self.pegarJSON()
        
        try:
            for dicts in data:
                if str(id) in dicts:
                    if toEdit == 'nome':
                        dicts[str(id)]['nome'] = modified
                    elif toEdit == 'autores':
                        dicts[str(id)]['autores'] = modified
                    elif toEdit == 'genero':
                        dicts[str(id)]['genero'] = modified

            self.adicionarAoJSON(data)
        except Exception as e:
            print(e)
            
    
    def deletarLivro(self, id):
        data = self.pegarJSON()
        
        try:
            for index, dicts in enumerate(data):
                if str(id) in dicts:
                    data.pop(index)
                        
            self.adicionarAoJSON(data)
        except Exception as e:
            print(e)
            

