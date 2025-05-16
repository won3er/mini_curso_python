#Aprendendo utilizar range e while


for i in range(10):
  print(i)

  #isso significa que para um numero no alcance de até 10, print a quantidade de numeros.


#modo sequencial

for x in range(2, 10):
  print(i)

#isto acontece porque o segundo for não altera i, então imprime o último valor que i tinha: 9, repetidamente.
# porque dentro dele você está printando i, e não o x. 


#modo pulando
for i in range(0, 10, 3):
  print(i)

# Ele vai imprimir os números de 0 até 9, pulando de 3 em 3, ou seja: 0, 3, 6, 9
# O range(início, fim, passo)



"""
Loop 'for-Each' sobre cada caractere em uma string.

Neste exemplo, a variável 'i' representa cada elemento/caractere de 'hello'.
"""

for i in "hello!":
  print(i)


"""
Poderíamos também iterar sobre a string por indexação.

Considere o seguinte exemplo de iteração sobre a string por index, 
começando no índex 0 e terminando no último elemento, com os incrementos do contador em 2, 
portanto, imprimindo APENAS todos os outros elementos da string. 
"""
sapo = "sapo pula!"
for i in range(0, len(sapo), 2):
 print(str(i) + "o sapo pula " + sapo[i])




#  Nota: sem a atualização da variável no loop while, este será um loop INFINITO!!
count = 0
while (count < 10):
  print(count)
  # IMPORTANTE!!! Atualize o contador!
  count += 1


# --------------------------------------------------------------------


# 2.1.2: Continue/Break Keywords


# Como manipular loops (FOR e WHILE):

# Break: pular os códigos restantes no loop bem como as iterações remanecentes, quebrar (break) o loop mais interno.
# Continue: pular os códigos restantes no loop e continuar para a próxima iteração do loop.



#Esse programa roda infinitamete, exceto quando o usuário insere "end" para terminar.

while True:
  user = input("Coloque o valor: ")
  #quando o break é acionado, o print() não é executado.
  #o programa romperá o loop quando esta palavra-chave for lida. 
  if user == "end":
    print("Programa terminado!!! ")
    break
  print(user)


#Sem usar a palavra-chave "break", esta é outra implementação do mesmo programa de cima usando uma variável.

end = False
while end == False:
  user = input("Coloque o valor: ")
  if user == "end":
    print("Programa terminado!!!")
    end = True
  else:
    print(user)


#Para contar pulando de 5 a cada casa. 

count = 1
#impementação do loop while
while count + 1 <= 20: 
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count +=1
          

# Implementação do loop FOR 

for i in range (1, 20):
  if i % 5 == 0:
    print("Skip")
    continue
  print(i)

for n in range (1, 30):
  if n %3 == 0:
    print("divisivel")
    continue
  print(n)

for x in range (1, 50):
  if x %5 == 0:
    print("divisivel também")
    continue
  print(x)

# ----------------------------------------------------------------

# 2.2: Funções

def triangulo_quadrado (a, b, c):
  #reatribuir valores para garantir que C seja o comprimento mais longo
  if (max(a, b, c) !=c):
# o comando !=c, é um operador de comparação, onde !=c quer dizer diferente de C

    #tmp armazena os valores anteriores de C, que não é o comprimento mais longo
    ab = c
    c = max(a, b, c)
  # max(): Retorna o maior valor de um iterável ou entre dois ou mais valores.
    if a == c:
      a = ab
    elif b == c:
      b = ab

#aplicar a formula
  if a**2 + b**2 == c**2:
    print("Triangulo quadrado")
    
    #se o programa vê uma declaração return, este é o fim da função
    return True
  
  #Estas duas linhas funcionarão SOMENTE quando a condiçã IF for falsa
  print("Não é um trinagulo quadrado")
  return False

#Solicita ao usuário insirir 3 comprimentos
def main():
  a = input("Digite o primeiro comprimento: ")
  b = input("Digite o segundo comprimento: ")
  c = input ("Digite o terceiro comprimento: ")

#As entradas do usuário são armazenadas com uma string, então colocamos para ser "int"
  return triangulo_quadrado(int(a), int(b), int(c))  

if __name__ == "__main__":
  main()



# Outro exemplo


import string

def polidromo(str):
    # Cria um conjunto com todos os sinais de pontuação (como ., ,, !, ?, etc.)
    exclude = set(string.punctuation)
    
    # Cria uma nova string com somente os caracteres que NÃO são pontuação, ch for ch quer dizer "para cada caracteres"
    str = ''.join(ch for ch in str if ch not in exclude)
    #Substitui uma substring por outra dentro de uma string
    str = str.replace(" ", "").lower()
# lower() é um método que converte todos os caracteres de uma string para minúsculas


    # Verificar se a string é a mesma tanto em ordem invertida quanto na ordem original
    if str == str[::-1]:
        return True
    else:
        return False
#[::] é um fatiamento (slice). 
#O -1 no final significa: "Pegue todos os caracteres, mas andando de trás pra frente."

# Solicitar ao usuário que introduza a sentença
def main():
    userSetence = input("Enter a setence to be tested as a polidromo: ")
    
    if polidromo(userSetence):
        print(userSetence + " é um polidromo!")
    else:
        print(userSetence + " não é um polidromo!")

if __name__ == "__main__":
    main()


#Codigo acima resumido:
# 
#  # Considere esta implementação da função que RETURN (retorna) uma string.
# Anote a diferença entre main() e isPalindrom() após esta mudança. 
"""
import string

def isPalindrome(str):
  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(" ", "").lower()
  if str == str[::-1]:
    return str + " is a palindrome!"
  else:
    return str + " is NOT a palindrome!"

def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")
  print(isPalindrome(userSentence))

if __name__ == "__main__":
    main()


"""

#Lição: uma função para testar se uma palavra do usuário é um palindrome

# Definir a função
def polindromo():
    valor = input("Digite a palavra: ").lower()
    if valor == valor [::-1]:
      print(valor, "É um polindromo")
    else:
      print(valor, "Não é um polindromo! ")

polindromo()






