#Variáveis: um conjunto que contém algumas informações.
#Não se pode usar palavras chaves como variáveis, ex: global, class, if, etc.

# Exemplos de declarações de variáveis
width = 10
# Note que o "H" está em letra maiúscula
height = 5
area = 0


# Mais declarações para diferentes tipos de variáveis 

# armazenando uma string
helloMessage = "Hello World!"
first_name = "John"

# armazenando um caractere
character_example = 'a'

# armazenando um float
_newFloat = 1.0

# armazenando um valor booleano
bool_Condition = True


# Como declarar corretamente um nome variável para diferentes tipos de dados.

# Uma função útil: type() define o tipo dos dados.

# A partir da declaração acima, width = 10 e 10 é int, então esperamos que a função retorne int
type(width)
type(helloMessage)
type(bool_Condition)

# Vamos computar um float em um int e vice-versa
# Computaremos o tipo e depois o armazenaremos em uma nova variável
width_float = float(width)
type(width_float)

# Computar de float para int
width_int = int(width_float)
type(width_int)

# Computar entre string e int
# Lembrar que width armazena um int

'''
float: Representa números com ponto flutuante (decimais), como 3.14 ou -2.5.
int: Representa números inteiros, sem parte decimal, como 5, -3 ou 0.
str: Representa uma sequência de caracteres, ou seja, texto, como "olá", "123" ou "Python".
'''

# Converter width para string
width_string = str(width)
type(width_string)

# Converter width_string de volta a um int
type(int(width_string))


#------------------------------------------------------------

# Operações aritiméticas 

# Adição
print(5+23)

# Subtração
print(100-25)

# Multiplicação
print(5*10)

# Potência/Exponente
# o operador ** é equivalente ao expoente
print(5**2)

# 5*5 = 5^2 = 5**2 
print(5*5)


# Divisão (float)
# Retornar o valor decimal real da divisão
print(36/4)
print(10/3)         

# Divisão (int)
# Retornar um int. Se o quociente real for um valor decimal, apenas um número inteiro irá retornar
print(10//3)
print(19//6)

# Divisão Modular: retornar o restante da divisão
print(10%3)


# Operações com Strings e Caracteres
print("foo" * 5)
print('x'*3)

# Não se pode concatenar um int com uma string, forma errada: print("hello" + 5)
# Fix
print("hello " + str(5))


#--------------------------------------------

# Comparadores: retornar valor booleano

# Igualdade ==
# Nota: DEVE ser sinais de igual Duplos, um sinal de igual único é atribuição
print(5 == 5.0)

# Maior do que >
print(7 > 1)

# Menor do que <
print(1.5 < 90)

# Maior ou igual a >=
print(5.0 >= 5)
print(5.0 >= 4)
print(5 >= 13)

# Menor ou igual a <=
print(10 <= 10.0)
print(10 <= 20)
print(8 <= 3)


# Comparadores em Strings

print("hello" < "world")
print("hello" == "world")
print("hello" > "world")

print("hello" == "hello")

print("cat" < "dog")



# -----------------------------------------

# Declarações Condicionais

# elif" = "else if"
# "elif" expressa o mesmo significado que "else if"

# Pelo menos uma condição DEVE ser prevista para ambas as cláusulas if e elif, senão ERROR!
# Os parênteses para if e elif são opcionais. Seu código funcionará com ou sem o ().



x = 7
y = 6

if (2*x == y):
    print("y é o dobro de x")
elif (x**2 == y):
    print("y é o quadrado de x")
elif (x-2 == y):
    print("y é menor que x")
else:
    print("y não é o dobro de x")



x = 7
y = 49
if(2*x == y):
    print("y é o dobro de x")
elif (x**2 == y):
    print("y é o quadrado de x")
else:
    print("y não está relacionado a x ")

x = 7
y  = 50

if (2*x == y):
    print("y é o dobro de x")
elif (x**2 == y):
    print("y é o quadrado de x")
else:
    print("y não é o dobro nem quadrado de x")


def switcher(number):
    #usar dicionario para armazenar swtich cases
    #se não for encontrado, o get() será o valor padrão
    return {
        '0':"Entered 0",
        '1':"Entered 1",
        '2':"Entered 2",
    }.get(number,"Número inválido!")

#input()lê a entrada do usuário stdin
number=input("Disque um número: ")
print(switcher(number))

#exercíci: implementar switch case acima usando as condições "if/else"]

number = input("Digite um número: ")
if number== '0':
    print("Entou 0")
elif number == '1':
    print("entrou 1")
elif number == '2':
    print("entrou 2")
else:
    print("Número inválido!")


