# Módulo 5: Usos e Aplicações de Bibliotecas

# Objetivos de aprendizagem:

# 1 - Aplicar a biblioteca Math para resolver funções matemáticas;
# 2 - Aplicar as bibliotecas Numpy, Matplotlib, e Scipy para análise de dados e geração de gráficos;
# Aplicar o framework Flask para desenvolvimento web e entender a relação com o HTML.

# 5.1 Math

#Funções matemáticas comuns, ex valor absoluto, exponencial ou log, são definidas dentro da biblioteca matemática.

# Exemplo como usar a biblioteca Math

import math
#Função de potência
print("2^5 = " + str(math.pow(2,5)))
# o resultado é 2^5 = 32.0


#Função Teto (arredonda para cima)
print(math.ceil(3.45))
print(math.ceil(10.01))
#resultado 4 e 11


#Função de piso (arredonda para baixo)
print(math.floor(5.25))
print(math.floor(11.01))
#resultado 5 e 11


#Valor absoluto
print(math.fabs(-10.33))
print(math.fabs(5.25))
#resultado 10.33 e 5.25


#Log com base "e", ou log natural
print(math.log(1000))
#resultado 6.907755278982137
#isso porque e≈2.718281828459045...
# logo: e6.907755278982137 ≈1000


#Log com uma base específica no valor de 10
print(math.log(1000,10))
#resultado 2.9999999999999996 


# 5.2 Análise de dados com Numpy, Matplotlib, Scipy

#Numpy é um pacote para computação numérica em Python.
#Fornece uma estrutura de dados eficiente para matrizes numéricas, n-dimensionais (ndarray)
#Suporta operações veoriais e matriciais. 
#O Numpy é implementado em C, portante é realmente rápido e eficiente.

#O formato básico de dados em Numpy é a matriz n-dimensional. Estas podem ser usadas para representar vetores (1D), matrizes (2D) ou tensores (nD).

#Uma matriz numérica de uma dimensão é frequentemente usada para representar uma série de dados.
#As matrizes n-dimensionais muitas vezes representam conjuntos completos de dados (cada coluna é um tipo de medida).

#As matrizes númericas são parecidas com listas de Python. A indexação e o fatiamente funcionam da mesma forma (incluindo atribuições).
#No entanto, todas as células de uma matriz devem conter o mesmo tipo de dados.

#Os operadores não trabalham da mesma forma para listas e matrizes e há muitos métodos adicionais definidos nelas.

#Vamos ver o que acontece se usarmos uma lista para representar um vetor?
[1, 2, 3] * 3
#resultado [1, 2, 3, 1, 2, 3, 1, 2, 3]

#Não foi o resultado esperado com multiplicação vetorial por um escalar. 
#É necessário fazer assim:
[i*3 for i in [1, 2, 3]]
#resultado [3, 6, 9]


#E quanto a soma de dois vetores?
#Tratado como concatenação de lista:
[1,2,3]+[4,5,6]
#resultado [1., 2, 3,4 ,5 ,6]


#Soma de dois vetores
a = [1,2,3]
b = [4,5,6]
[a[i] +b[i] for i in range (len(a))]
#resultado 5, 7, 9
#O que o código faz é somar os valores da mesma posição nas duas listas.

# Você pode usar zip, que só vai até o menor tamanho das listas:
#[a + b for a, b in zip(a, b)]


#Produto vetorial ou produto escalar?
[1,2,3] * [4, 5, 6]

#Poderíamos calcular o produto escalar assim:
u = [1,2,3]
v = [4, 5, 6]

total = 0

for x in range(len(u)):
    total += u[x] * v[x]
total
#resultado 32
#O código calcula a soma dos produtos dos elementos de u e v.


#Vamos ver o que acontece se usarmos Numpy
#np é uma convenção comum para se referir a numpy ao longo de todo código

import numpy as np

c = np.array([1, 2, 3])
d = np.array([4,5,6])

#dot( calcula o produto escalar de dois vetores)
np.dot(c,d)
#resultado 32
#posso por por ex: resultado = np.dot(c,d), e posteriormente: print(resultado) para ver o resultado.
#dot é uma função do Numpy que calcula o produto escalar (ou produto ponto) entre dois vetores ou matrizes.

#Mais algumas operações em matrizes 1D:

import numpy as np
e = np.array([1,2,3])
f = np.array([4,5,6])

print("Vector addition with another vector ---> " + str(e+f))
print("Vector addition with a scalar ---> " + str(e+4))
print("Vector multiplication by a scalar ---> " + str(e* 4))
print("Vector multiplication (Not dot nor cross product) ---> " + str(e*f))
print("Vector sum ---> " + str(np.sum(e*f)))
print("Dot product ---> " + str(np.dot(e,f)))

#resultado
'''
Vector addition with another vector ---> [5 7 9]
Vector addition with a scalar ---> [5 6 7]
Vector multiplication by a scalar ---> [ 4  8 12]
Vector multiplication (NOT dot nor cross product) ---> [ 4 10 18]
Vector sum ---> 32
Dot product ---> 32
'''
              
# ----------------------------------------------------------------------------------


#Vejamos as matrizes multidimensionais: 'matrizes dentro de matrizes'.
# O seguinte código cria um total de três matrizes 3*3 com todas elas:

e = np.ones((3,3,3))

'''

Esse código cria um array 3D (3 dimensões), onde:

São 3 blocos

Cada bloco tem 3 linhas

Cada linha tem 3 colunas

E todos os valores são 1.0

'''

#resultado 
'''
[[[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]]

'''

#e.shape mostra o formato (as dimensões) do array e, que é: (3, 3, 3)

#outros exemplos simples de uso

np.ones((2,3))
#cada bloco tem 2 linhas e 3 colunhas

np.ones((3, 2))
#cada bloco tem 3 linnhas e 2 colunas 

#------------------------------------------------------------

#Scipy é um pacote para analisar o ajuste da curva.
#Matplotlib é um pacote para dados gráficos.
#Veja como Scipy, Numpy e Matplotlib poderiam ser usados juntos na análise de dados.

#Importar diferents pacotes usados para análise de dados
#... "as opt" significa que o programador poderia usar a abreviatura de "opt" para se referir a esta biblioteca, em vez de digitar o nome completo.

#------------------------------------------------------------------------------

import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt

# Dados corrigidos
I = [4.0, 3.5, 3.0, 2.0, 1.0]
B = [1.31, 1.14, 0.97, 0.81, 0.76]
IError = [0.2, 0.2, 0.2, 0.2, 0.2]
BError = [0.03, 0.02, 0.04, 0.02, 0.05]

# Conversão para arrays numpy
xdata = np.array(I)
ydata = np.array(B)
xerror = np.array(IError)
yerror = np.array(BError)

# Função linear
def func(h, m, b):
    return m*h + b

# Ajuste da curva — ISSO RESOLVE O ERRO
w, u = opt.curve_fit(func, xdata, ydata, sigma=yerror)

# Gera os valores ajustados
yfit = func(xdata, *w)

# Plot
plt.errorbar(I, B, xerr=IError, yerr=BError, fmt='o', ms=3)
plt.plot(xdata, yfit, label="Fit", linewidth=1.5, linestyle='dashed')
plt.title('I vs. B of the Electromagnet')
plt.xlabel('Electromagnet Current I (A)')
plt.ylabel('Magnetic Field B (T)')
plt.legend()

# Exibe os parâmetros estimados
print("\nEstimated parameters of m and b: ", w)
print("\nEstimated standard deviation of m & b: ", np.sqrt(np.diag(u)))

plt.show()

#--------------------------------------------------------------------------------------------------------------

# 5.3: Desenvolvimento Web com Flask

'''
@app.route define qual URL leva a qual função no site.

A URL '/' é a página inicial, que mostra a mensagem:
"WELCOME to My Home Page" em letra grande (título).

Se a URL tiver um nome (ex: /João), o site usa esse nome para gerar a página.
Isso se chama página dinâmica.

Se a URL for /admin, a função admin() é chamada e redireciona para a página inicial.
'''


from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    return '''
        <h1>Bem-vindo à minha Página Inicial</h1>
        <p><a href="/admin">Ir para o Admin</a></p>
        <p><a href="/fale_conosco">Fale Conosco</a></p>
    '''

# Redireciona o admin para a home
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

# Página com o formulário
@app.route("/fale_conosco")
def fale_conosco():
    return '''
        <h1>Fale Conosco</h1>
        <form method="post" action="/obrigado">
            <label for="mensagem">Mensagem:</label><br>
            <input type="text" id="mensagem" name="mensagem" placeholder="Digite sua mensagem aqui"><br><br>
            <input type="submit" value="Enviar">
        </form>
        <p><a href="/">Voltar à Página Inicial</a></p>
    '''

# Página de resposta após o envio
@app.route("/obrigado", methods=["POST"])
def obrigado():
    mensagem = request.form["mensagem"]
    return f'''
        <h1>Obrigado pela sua mensagem!</h1>
        <p>Você escreveu: <strong>{mensagem}</strong></p>
        <p><a href="/">Voltar à Página Inicial</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True)




    
                    
                
           