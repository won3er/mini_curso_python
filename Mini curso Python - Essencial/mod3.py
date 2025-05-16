
#Uso de listas em Python
# Listas são estruturas de dados que podem armazenar múltiplos valores em uma única variável
# Listas são mutáveis, ou seja, podem ser alteradas após a criação
# Listas podem conter diferentes tipos de dados, como strings, inteiros, floats, booleanos, etc.
# Listas são definidas entre colchetes [] e os elementos são separados por vírgulas
# Listas podem ser acessadas por meio de índices, que começam em 0
# Listas podem ser manipuladas com métodos como append(), insert(), remove(), pop(), sort(), reverse(), etc.
# Listas podem ser aninhadas, ou seja, uma lista pode conter outras listas como elementos
# Listas podem ser copiadas com o método copy() ou com a função list()
# Listas podem ser concatenadas com o operador + e repetidas com o operador *
# Listas podem ser fatiadas com o operador [:] e podem ser percorridas com loops for
# Listas podem ser verificadas com o operador in e podem ser contadas com o método count()
# Listas podem ser ordenadas com o método sort() e podem ser revertidas com o método reverse()
# Listas podem ser unidas com o método extend() e podem ser divididas com o método split()
# Listas podem ser convertidas para strings com o método join() e podem ser convertidas para tuplas com o método tuple()
# Listas podem ser convertidas para dicionários com o método dict() e podem ser convertidas para conjuntos com o método set()
# Listas podem ser convertidas para arrays com o método array() e podem ser convertidas para JSON com o método json.dumps()
# Listas podem ser convertidas para CSV com o método csv.writer() e podem ser convertidas para XML com o método xml.etree.ElementTree.Element()
# Listas podem ser convertidas para HTML com o método html.parser.HTMLParser() e podem ser convertidas para PDF com o método fpdf.FPDF()
# Listas podem ser convertidas para Excel com o método openpyxl.Workbook() e podem ser convertidas para Word com o método docx.Document()




# ========================
# Parte 1: Operações com Listas
# ========================

list1 = []  
list2 = ["a", "b", "c"]
list3 = ["John", "male", 3, 4.5, True]   

# Nota: em CS, a primeira posição é SEMPRE 0
print("First element in list2:", list2[0])
print("First element in list3:", list3[0])

# Manipulação de listas
list2.insert(1, 'hallo')  # Adiciona 'hallo' na posição 1 da lista 2
list2.append('bye')  # Adiciona 'bye' no final da lista 2
list2.pop(1)  # Remove o elemento na posição 1 da lista 2
list2.sort()  # Ordena a lista 2 em ordem alfabética

# Exibe os tamanhos das listas
print("size of list1 = " + str(len(list1)))
print("size of list2 = " + str(len(list2)))
print("size of list3 = " + str(len(list3)))

# Exibe a lista de resultados
resultados = [
    '-'.join(list1),
    '.'.join(list2),
    ','.join(map(str, list3)), # Converte os elementos da lista 3 para string antes de juntar
] # o map é uma função que aplica a função str a cada elemento da lista list3
print(resultados)


# =========================
# Parte 2: Listas Aninhadas
# =========================

nested_list = []  # Lista para listas aninhadas
nested_list.append([1, 2, 3])
nested_list.append(['a', 'b', 'c'])
print(nested_list[1][2])  # Acessa o elemento na posição 2 da lista 1


# ====================
# Parte 3: Tuplas
# ====================

# Tupla inicial
x = (1, 2, 3)

# Tuplas são imutáveis, então operações de adição geram novas tuplas
x + (4, 5, 6)  # Adiciona 4, 5 e 6 (mas não altera a tupla original)
x * 2  # Repete a tupla x duas vezes

# Mostra a tupla original
print(x)


# ============================
# Parte 4: Conversão de Tupla para Lista
# ============================

x = (1, 2, 3, 4)
x_list = list(x)  # Converte a tupla para uma lista
print(x_list)  # Exibe a lista convertida

# converte a lista de volta para uma tupla
x_tuple = tuple(x_list)  # Converte a lista de volta para uma tupla
print(x_tuple)  # Exibe a tupla convertida


# =========================
#declarar uma nova tupla com nome "person"
person = ('Jane', 'EUA', 21)

# "pacote"/ associar cada elemento da tupla com uma etiqueta. Observe a ordem das etiquetas.
name, local, age = person
print(age)  # Exibe a idade da pessoa


# outro exemplo
x = (1, 2, 3, 4)
a, b, c, d = x  # Atribui os valores da tupla x às variáveis a, b e c
print(d)  # Exibe o valor da variável d (que é 4)



# =========================
# Parte 5: Conjunto
# =========================

#inicializar um conjunto vazio
newSet = set()
print(newSet)

# um conjunto com elementos
ex1 = {1, 1, 3, 3, 5}
print(ex1)  # Exibe o conjunto (os elementos duplicados são removidos)

ex2 = {j for j in range(10)}  
print(ex2)  # Exibe o conjunto gerado por compreensão de conjunto (os elementos duplicados são removidos)

# 2 já existe no conjunto, então será adicionado novamente
ex2.add(2)
print(ex2)  # Exibe o conjunto (os elementos duplicados são removidos)

ex2.add(11) # Adiciona 11 ao conjunto
print(ex2)


#objetos mutáveis não podem ser adicionados a um conjunto
# ex3 = {1, 2, 3}
# ex3.add([1, 2])  # Isso causará um erro, pois [1, 2] é uma lista (mutável)


# Converte a lista de idades em um conjunto 
ages = [10, 5, 4, 5, 2, 1 ,5] # Lista de idades
set_of_ages = set(ages)  # Converte a lista de idades em um conjunto 
print(set_of_ages)  # Exibe o conjunto de idades (os elementos duplicados são removidos)

# Converte o conjunto para uma lista
list_of_ages = list(set_of_ages)  # Converte o conjunto de idades de volta para uma lista
print(list_of_ages)  # Exibe a lista de idades (os elementos duplicados são removidos)

#converter um conjunto em uma tupla
tuple_of_ages = tuple(list_of_ages)
print (tuple_of_ages)  # Exibe a tupla de idades (os elementos duplicados são removidos)

# a ordem é irrelevante, uma vez que os elementos são ordenados em ordem crescente

# -------------------------------------------------------------------------------------------------------



# 3.4: Dicionário
# Dicionários são estruturas de dados que armazenam pares de chave-valor
#Todo dicionário em Python é formado por pares no formato chave:valor
# As chaves devem ser únicas e imutáveis (strings, números, tuplas)
# Os valores podem ser de qualquer tipo e podem ser duplicados
'''
Ex de objetos imutáveis
inteiro = 5
string = "Python"
tupla = (1, 2, 3)

Tentando alterar um objeto imutável (isso não funciona)
 inteiro = inteiro + 1  # Cria um novo objeto com o valor 6
'''

# Inicializar um dicionário vazio
# O mesmo do conjunto, mas com:
dict = {}

# Declare um dicionário com pares de chaves/valores
dict2 = {'a': 5, 'b': 10, 'c': 100, 'd': 9.5}

# Acessar dados em um dicionário com uma chave
dict2['b']

# Atualização do valor de uma chave existente
dict2['b'] = 20  # Atualiza o valor da chave 'b' para 20
print(dict2['b'])  # Exibe o valor atualizado da chave 'b' (20) 

# Se buscarmos uma chave que não existe, teremos um erro
# ex: dict2['e']  # Isso causará um erro, pois a chave 'e' não existe no dicionário
# Para evitar isso, podemos usar o método get() que retorna None se a chave não existir 
# ex: dict2.get('e')  # Isso retornará None, pois a chave 'e' não existe no dicionário

#Forma correta:
dict2 = {} 
dict2['e'] = 100  # Adiciona a chave 'e' com o valor 100 ao dicionário
print(dict2["e"])  # Exibe o valor da chave 'e' (100)

# Os valores no dicionario podem ser misturados
# Vejamos um exemplo com dict {}, um dicionário vazio iniciado acima
# Primeiro, vamos inserir alguns pares e chaves/valores no programa.

dict["greetings"] = "hello"
dict["alphabet"] = ['a', 'b','c']
dict["check-in"] = False
dict["PhoneNumber"] = 40028922

# dict1 = {}
# dict1[['a', 'b', 'c']] = ["1", "2", "3"] # Isso causará um erro, pois a chave deve ser uma string ou um número, não uma lista
# dict[1, 2, 3] = "abc" # Isso causará um erro, pois a chave deve ser uma string ou um número, não uma tupla 
# Ex: dict[1] = "abc" # Isso funcionará, pois a chave é um número (1) e o valor é uma string ("abc")
# Só assim para adicionar uma chave/valor ao dicionário
# print(dict1)

# Forma correta:
dict1 = {} 
dict1['a'] = "1"  # Adiciona a chave 'a' com o valor "1" ao dicionário
dict1['b'] = "2"  # Adiciona a chave 'b' com o valor "2" ao dicionário
dict1['c'] = "3"  # Adiciona a chave 'c' com o valor "3" ao dicionário
print(dict1)  # Exibe o dicionário (as chaves e valores são exibidos na ordem em que foram adicionados)


# É possivel mudar uma lista dentro de um dicionário
# Exemplo de dicionário com uma lista como valor 
dict3 = {'a': [1, 2, 3], 'b': [4, 5, 6]}

dict3['a'].append(4)  # Adiciona 4 à lista da chave 'a'
dict3['b'].remove(5)  # Remove 5 da lista da chave 'b'
print(dict3)  # Exibe o dicionário (as listas são exibidas com os elementos atualizados)


# Como tupla é imutável, podemos substituir a lista por uma tupla
dict4 = {'a': [1, 2, 3], 'b': [4, 5, 6]} # Dicionário com tuplas como valores 
dict4['a'] = (1, 2, 3)  # Substitui a lista da chave 'a' por uma tupla
dict4['b'] = (4, 5, 6)  # Substitui a lista da chave 'b' por uma tupla
print(dict4)  # Exibe o dicionário (as tuplas são exibidas com os elementos atualizados)


# Podemos buscar todas as chaves de um dicionário com o método keys()
# Podemos buscar todos os valores de um dicionário com o método values()
# Podemos buscar todos os pares de chave-valor de um dicionário com o método items()

dict4.keys()  # Retorna todas as chaves do dicionário
dict4.values()  # Retorna todos os valores do dicionário
dict4.items()  # Retorna todos os pares de chave-valor do dicionário

