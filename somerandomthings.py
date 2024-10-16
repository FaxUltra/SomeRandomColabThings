# -*- coding: utf-8 -*-
"""SomeRandomThings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T1WxLNb8mcoofyTfxVncCKL7gU_0S0fF
"""

print("Hola!")

"""# Diccionarios y variables

Aca, vamos a crear un diccionario y vamos a ir añadiendo y quitando datos
"""

database={"else","is","if"}
print(database)
database.add("lol")
print(database)
database.remove("is")
if database == {"else","lol","if"}:
  print("database is: ",database)

"""Aca, estamos creando una red neuronal que genera palabras aleatorias"""

#Inicio de codigo
import random

# Definimos un vocabulario básico
vocabulary = ["the", "a", "an", "cat", "dog", "house", "run", "jump", "eat", "sleep", "happy", "sad"]

# Función para generar una palabra aleatoria
def generate_random_word(vocab):
  return random.choice(vocab)


# Ejemplo de uso
for _ in range(10):
  random_word = generate_random_word(vocabulary)
  print(random_word)
#Fin de codigo

"""Esto es un programa simple que obtiene un **"secreto"**, que es una variable oculta que creas desde *Google Colab*"""

from google.colab import userdata
userdata.get('KeyWord')
print(userdata.get('KeyWord'))

"""# Numeros aleatorios

Aqui, creamos una variable que tira un numero aleatorio y la mostramos
"""

import random
aleatory = random.randint(1,100)
print(aleatory)

"""Aca creamos un esquema con la frequencia de diferentes numeros random. Me llama la atencion como todos caen cerca de 200"""

import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

x = 200 + np.random.randn(10000)
fig, ax = plt.subplots(1, 1)
ax.hist(x, 100)

plt.title("Rnd DTA (Modified by 200)")
plt.xlabel("Value")
plt.ylabel("Frequency")

"""En este esquema, el valor no esta modificado por 200, pero el valor sigue estando cerca de 0"""

import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

x = np.random.randn(9999999)
fig, ax = plt.subplots(1, 1)
ax.hist(x, 100)

plt.title("Rnd DTA (Not modified by 200)")
plt.xlabel("Value")
plt.ylabel("Frequency")

"""Una curiosidad es que mientras mas numeros generados, mas homogeneo es el esquema"""