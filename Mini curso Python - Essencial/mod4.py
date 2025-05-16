# Módulo 4: Programação Orientada à Objetos

# classes são estruturas que permitem criar objetos com atributos e métodos
# classes são definidas usando a palavra-chave class
# métodos são funções definidas dentro de uma classe
# atributos são variáveis definidas dentro de uma classe
# instâncias são objetos criados a partir de uma classe
# herança é um mecanismo que permite criar uma nova classe a partir de uma classe existente 

#nome da classe, começa com letra maiúscula
# nome do arquivo, começa com letra minúscula
class Librarybook: 
	'''
	Classe que representa um livro em uma biblioteca.
	'''

# pass # A palavra-chave pass é usada para indicar que não há código a ser executado neste bloco.
# Isso é útil quando você deseja definir uma classe ou função, mas ainda não implementou a lógica.
pass 


# isto irá criar uma istância da classe Librarybook
my_book = Librarybook()


type(my_book)  # Exibe o tipo do objeto my_book (que é Librarybook)
# Exibe <class '__main__.Librarybook'>, indicando que my_book é uma instância da classe Librarybook

# outra maneira de verificar o tipo de algum objeto
isinstance(my_book, Librarybook)
# Exibe True, pois my_book é uma instância da classe Librarybook

# por que e quando usar classes?

# As classes são usadas para organizar e estruturar o código, permitindo criar objetos que representam entidades do mundo real.
# Elas ajudam a encapsular dados e comportamentos relacionados, facilitando a manutenção e reutilização do código.

# ENCAPSULAMENTO
# os dados e a funcionalidade são agrupados em objetos, o que ajuda a proteger os dados e a controlar o acesso a eles.
# os metodos fornecem uma interface para o objeto. O ideal é que os dados individuais sejam acessados apenas por meio de métodos.
# Isso significa que so detalhes sobre como a funcionalidade é implementada são ocultos do usuário.
# Por exemplo, não sabemos como o método de anexar em listas funciona, mas sabemos que ele funciona.
# Esta ideia permite que as classes sejam compartilhadas (em bibliotecas) e usadas por outros (ou reutilizadas por você mesmo) sem que você precise ler o código fonte da classe.


# --------------------------------------------------------------------------


# init, parâmetro Self

# Campo de dados - Cada instância de uma classe tem seu próprio conjunto de dados.
# Isso é feito usando o parâmetro self, que é uma referência à instância atual da classe.
# O método init(self, ...) é chamado automaticamente quando uma nova instância da classe é criada.
# Este método é chamado de construtor de classe; ele inicializa os dados da instância.

'''

    Um livro da biblioteca.
    '''
class Librarybook(object): 
	
    '''
    O parâmetro self é OBRIGATÓRIO dentro da classe,
    porque ele diz ao programa para buscar/atuar sobre o objeto de instância que a executou'''

    def __init__(self, title, author, year, call_no):
          self.title = title # Atributo de instância: título do livro
          self.author = author # Atributo de instância: autor do livro
          self.year - year # Atributo de instância: ano de publicação do livro
          self.call_no = call_no # Atributo de instância: número de chamada do livro
          self.checked_out = False # Atributo de instância: indica se o livro está emprestado ou não


'''
Como já criamos meu_livro como um objeto do librarybook,
agora podemos adicionar manualmente o título, autor, ... informações associadas ao livro.
'''

my_book.title = "Harry Potter e a Pedra Filosofal" # Atribui o título ao livro
my_book.author = "J.K. Rowling" # Atribui o autor ao livro
my_book.year = 1997 # Atribui o ano de publicação ao livro
my_book.call_no = "FIC ROW" # Atribui o número de chamada ao livro
my_book.checked_out = False # Atribui o status de empréstimo ao livro (não emprestado)

 # -------------------------------------------------------------

#Escrevendo um método 

# métodos contem a funcionalidade do objeto, são defndefinidos dentro da classe e podem ser chamados em instâncias do objeto


class Librarybook(object):
      '''
      Um livro da biblioteca.
      '''

      def __init__(self, title, author, year, call_no):
            self,title = title # Atributo de instância: título do livro
            self.author = author # Atributo de instância: autor do livro
            self.year = year # Atributo de instância: ano de publicação do livro
            self.call_no = call_no # Atributo de instância: número de chamada do livro
            self.checked_out = False # Atributo de instância: indica se o livro está emprestado ou não

        
 # Métodos para o Librarybook
    
# Retorna o título e as informações do autor do livro como uma string
def title_and_author(self):
      return "{} {}: {}".format(self.author[1], self.author[0], self.title)

# Imprime todas as informações associadas a um livro neste formato:
def __str__(self): #certifique-se de que __str__ retorne uma string
      return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title)

#Retorna uma representação de string do livro com o título e call_no
def __repr__(self): #certifique-se de que __repr__ retorne uma string
      return "<Book: {} ({})>".format(self.title, self.call_no)

# print está desencadeando a __string__()
print(my_book) # Exibe a representação do livro como string
# Exibe <Book: Harry Potter e a Pedra Filosofal (FIC ROW)>, que é o resultado do método __str__() definido na classe Librarybook


# Exemplo simples de codigo para criar uma fruta: 
# A classe Fruta tem um método __str__ que retorna uma string formatada com o nome e a cor da fruta.

class Fruta:
    def __init__(self, nome, cor):
        self.nome = nome  # Atributo de instância: nome da fruta
        self.cor = cor  # Atributo de instância: cor da fruta

    def __str__(self):  # Método que retorna uma string formatada com o nome e a cor da fruta
        return "Fruta: {}, Cor: {}".format(self.nome, self.cor)
    

# ------------------------------------------------------------------------------------------------------------------    
# Chamada de método Interno/externo 

# A única diferença é: 
#Externamente, você chama o método com a instância do objeto (my_book.title_and_author())
#Internamente, você chama o método com o parâmetro self (self.title_and_author())

# Exemplo simples e rápido do uso de métodos internos e externos em Python:
class Exemplo:
    def metodo_interno(self):
        return "Método interno chamado!"

    def metodo_externo(self):
        return self.metodo_interno()  # Chama o método interno usando self


# ------------------------------------------------------------------------------------
# Herança
# A herança é um mecanismo que permite criar uma nova classe a partir de uma classe existente.
# A nova classe herda os atributos e métodos da classe pai, permitindo reutilizar código e criar hierarquias de classes.
# A classe filha pode adicionar novos atributos e métodos ou sobrescrever os existentes na classe pai.

class ClownFish(object):
     pass # A palavra-chave pass é usada para indicar que não há código a ser executado neste bloco.

      
nemo = ClownFish() # Cria uma instância da classe ClownFish chamada nemo
type(nemo) # Exibe o tipo do objeto nemo (que é ClownFish)
isinstance(nemo, ClownFish) # Exibe True, pois nemo é uma instância da classe ClownFish

#Mas Clownfish (peixe-palhaço) é um tipo de peixe, e cada um poderia ser uma classe separada.

# Neste caso, precisamos ter relações entre as classes.

# A classe ClownFish poderia ter a classe pai Fish, que poderia ter a classe pai Vertebrado, que poderia ter a classe pai Animal.
# Essa relação é chamada de relação is-a (é um), onde uma classe é um tipo específico de outra classe.
# Esta relação estabelece entre uma classe de filhos e sua classe de pais. 
# Cada classe em python tem pelo menos uma classe de pais. 
# Se você não especificar uma classe pai, a classe de pais padrão é object.
# Isso significa que todas as classes em Python herdam de object, mesmo que você não tenha especificado isso explicitamente.
# Isso é chamado de herança implícita.

# Note que a relação é uma relação transitória, portanto, todo ClownFish também é um Animal.)

# Há uma super classe em python, que é a classe object.
# Até agora, quando definimos classes, sempre fizemos do objeto o pai direto da classe. 

class Animal(object):
     pass

class Vertebral(Animal):
     pass

class Fish(Vertebral):
     pass

class ClownFish(Fish):
     pass

class TangFish(Fish):
     pass



'''
isinstance em Python serve pra ver se uma coisa é de um tipo específico.
Exemplo:
x = 5
print(isinstance(x, int))  # Isso dá True, porque x é um número inteiro (int)

--------------------------------------------------------------------------------------------------------
Para ver se uma classe herda outro usamos assim:
class Animal:
    pass

class Cachorro(Animal):
    pass

dog = Cachorro()
print(isinstance(dog, Animal))  # True, porque Cachorro vem de Animal

---------------------------------------------------------------------------------------------
Exemplo comum com uma classe: 
class Pessoa:
    pass

p = Pessoa()
print(isinstance(p, Pessoa))  # True


'''

nemo = ClownFish()
isinstance (nemo, ClownFish)
# Dará True 

isinstance(nemo, TangFish)
#Dará False

# A relação is-a (é-um) é transitiva
isinstance (nemo, Animal)
#Dará True

#Todas as classes têm uma classe pai de Objeto
isinstance (nemo, object)
#Dará True

#Regra de ouro:
# isinstance(obj, Classe) dá True quando a classe está na cadeia de herança do objeto (ou seja, quando obj é uma instância direta ou indireta da classe).



# ------------------------------------------------------------------------------------------------------------------

# 4.3.1 Métodos Herdados

#Por que usar a herança?

# Toda classe também tem acesso aos atributos de classe da classe pai. 
# Em particular, os méodos definidos na classe pai podem ser chamados em instâncias de seus "decendentes".

class Fish(Animal):
     def speak(self):
          return "Blub"
     
class ClownFish(Fish):
    pass

class TangFish(Fish):
     pass

dory = TangFish
# A classe TangFish é filha da classe Fish, assim pode acessar speak() da classe Fish.
# Esta classe procura primeiro o método de chamada dentro de sua classe e, se não for encontrado, então repete a busca por cada nível hierárquico superior. 

dory.speak
# A saída será 'Blub'

nemo = ClownFish()
#ClownFish é uma classe filha de Fish, por isso pode acessar speak() da classe Fish.

nemo.speak
# A saída será 'Blub'



# E se quisermos uma funcionalidade diferente para uma classe filha? Podemos substituir o método (escrevendo um novo com o mesmo nome).

class TangFish(Fish):
     def speak(self):
          return "Olá, eu sou da instância TangFish"

dory = TangFish()
# Este speak() é da classe TangFish
dory.speak()
# Vai aparecer "Olá, eu sou da instância TangFish"


# --------------------------------------------------------------------------------------------

# 4.3.2: Acessando Variáveis em uma Relação

# Em uma relação is-a(é-um), a classe filha pode acessar atributos da classe pai se não estiver definida na classe filha, ou substituir o valor
# do atributo do mesmo atributo existente na classe filha. 


class Fish(Vertebral):
     # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
     def __str__(self):
          return "Olá, meu nome é {}".format(self.name)

# A classe Fish não tem um atributo chamado name, mas a classe ClownFish tem.
class ClownFish(Fish):
     def __initi__(self,name):
          self.name = name


nemo = ClownFish("Nemo")
# O atributo self.name para __str__() é da classe ClownFish.
# mas o método __str__() é da classe Fish.

nemo = Fish()
print(nemo) # Exibe "Olá, meu nome é None", pois o atributo name não foi definido na classe Fish.


class Fish(Vertebral):
     def __init__(self, name):
          self.name = name
    # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
     def __str__(self):
          return "Olá, meu nome é {}".format(self.name)
     
class ClownFish(Fish):  
     def __init__(self, name): 
          self.name = name # A classe ClownFish herda de Fish e define o atributo name na inicialização.
            # A classe ClownFish tem um atributo chamado name, que é definido na classe Fish.
          
nemo = ClownFish("Nemo")
# __str__() está acessando o self.name a partir da classe Fish, que é o nome do peixe.
print(nemo) # Exibe "Olá, meu nome é Nemo", pois o atributo name foi definido na classe ClownFish e acessado na classe Fish.

nemo = Fish("ClownFish")
print(nemo) # Exibe "Olá, meu nome é ClownFish", pois o atributo name foi definido na classe Fish e acessado na classe Fish.
