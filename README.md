# Estructuras_Datos
Actividades para Estructuras de Datos y Análisis de Algoritmos


El principal beneficio de NumPy
El principal beneficio de NumPy es que permite una generación y manejo de datos extremadamente rápido. NumPy tiene su propia estructura de datos incorporada llamado arreglo que es similar a la lista normal de Python, pero puede almacenar y operar con datos de manera mucho más eficiente.

¿ Que aprenderemos sobre NumPy ?
Los practicantes avanzados de Python pasarán mucho más tiempo trabajando con pandas que trabajando con NumPy. AUn así, dado que pandas se basa en NumPy, es importante comprender los aspectos más importantes de la biblioteca NumPy.


----> Arreglos de NumPy

Los arreglos de NumPy son creados llamando al método array() de la librería de NumPy. Dentro del método, deberías pasar una lista.

A continuación, se muestra un ejemplo de un arreglo de NumPy básico. Ten en cuenta que mientras ejecuto la instrucción import numpy as np al comienzo de este bloque de código, se excluirá de los otros bloques de código en esta sección por razones de brevedad.

import numpy as np

sample_list = [1, 2, 3]

np.array(sample_list)
La última línea de ese bloque de código dará como resultado una salida que se ve así.

array([1,2,3])
El contenedor array() indica que esta ya no es una lista normal de Python. En cambio, es un arreglo de NumPy.

Los dos tipos diferentes de arreglos de NumPy
Hay dos tipos diferentes de arreglos de NumPy: vectores y matrices.

Los vectores son arreglos de NumPy uni-dimensionales y se ve así:

my_vector = np.array(['este', 'es', 'un', 'vector'])
Las matrices son arreglo bi-dimensionales y son creadas pasando una lista de lista dentro del método np.array(). Un ejemplo es el siguiente.

my_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

np.array(my_matrix)
También puedes expandir los arreglos de NumPy para trabajar con matrices de tres, cuatro, cinco, seis o más dimensiones, pero son raras y están en gran parte fuera del alcance de este curso (después de todo, este es un curso sobre programación Python, no álgebra lineal).

Arreglos de NumPy: Métodos Incorporados
Los arreglos de NumPy vienen con un número de métodos incorporados útiles. Dedicaremos el resto de esta sección analizando estos métodos en detalle.

Cómo obtener un rango de números en Python utilizando Numpy
NumPy tiene un método útil llamado arange que toma dos números y devuelve un arreglo de números enteros que son mayores o iguales a (>=) el primer número y menores que (<) el segundo número.

Un ejemplo del método arange es el siguiente.

np.arange(0,5)

#Devuevle array([0, 1, 2, 3, 4])

Un ejemplo de uso de la tercera variable en el método arange se encuentra a continuación.

np.arange(1,11,2)

#Returns array([1, 3, 5, 7, 9])
Cómo generar Unos y Ceros en Python usando NumPy
Mientras programas, de vez en cuando necesitará crear arreglos de unos o ceros. NumPy tiene métodos incorporados que te permiten hacer ambas cosas.

Podemos crear arreglos de ceros utilizando el método zeros de NumPy. Le pasas el número de enteros que quisieras crear como el argumento de la función. Un ejemplo es el siguiente.

np.zeros(4)

#Devuelve array([0, 0, 0, 0])
También puedes hacer algo similar utilizando matrices tridimensionales. Por ejemplo, np.zeros(5, 5) crea un arreglo de 5x5 que contiene todos ceros.

Podemos crear arreglos de unos usando un método similar llamado ones. Un ejemplo es el que sigue.

np.ones(5)

#Returns array([1, 1, 1, 1, 1])
Cómo dividir uniformemente un rango de números en Python usando NumPy
Hay muchas situaciones en las que tienes un rango de números y te gustaría dividir por igual ese rango de números en intervalos. El método linspace de NumPy está diseñado para resolver este problema. linspace tiene tres argumentos:

El inicio del intervalo
El fin del intervalo
El número de subintervalos en los que deseas que se divida el intervalo
Un ejemplo del método linspace es el siguiente.

np.linspace(0, 1, 10)

#Devuelve array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
Cómo crear un arreglo Identidad en Python usando NumPy
Cualquiera que haya estudiado álgebra lineal estará familiarizado con el concepto de un "arregloidentidad", que es un arreglo cuadrada cuyos valores diagonales son todos 1. NumPy tiene una función incorporada que incluye un argumento para construir matrices de identidad. La función es eye.

Algunos ejemplos:

np.eye(1)

#Devuelve un arreglo identidad de 1x1

np.eye(2) 

#Devuelve un arreglo identidad de 2x2

np.eye(50)

#Devuelve un arreglo identidad de 50x50

----> ¿ Cómo crear números aleatorios en Python usando NumPy ?

NumPy tiene varios métodos integrados que te permiten crear matrices de números aleatorios. Cada uno de estos métodos comienza con random. A continuación se muestran algunos ejemplos:

np.random.rand(sample_size)

#Devuelve una muestra de números aleatorios entre 0 y 1.

#El tamaño de la muestra puede ser un número entero (para un arreglo unidimensional) o dos enteros separados por comas (para un arreglo bidimensional).

np.random.randn(sample_size)

#Devuelve una muestra de números aleatorios entre 0 y 1, siguiendo la distribución normal

#El tamaño de la muestra puede ser un número entero (para un arreglo unidimensional) o dos enteros separados por comas (para un arreglo bidimensional).

np.random.randint(low, high, sample_size)

#Devuelve una muestra de números enteros que son mayores o iguales que 'low' y menores que 'high' 
Cómo remodelar arreglos de NumPy

A continuación se muestra un ejemplo:

arr = np.array([0,1,2,3,4,5])

arr.reshape(2,3)
La salida de esta operación es:

array([[0, 1, 2],

       [3, 4, 5]])


Puede determinar su forma utilizando el atributo shape de NumPy. Usando nuestra estructura de la variable arr anterior, a continuación se muestra un ejemplo de cómo llamar al atributo shape:

arr = np.array([0,1,2,3,4,5])

arr.shape

#Devuelve (6,)
arr = arr.reshape(2,3)

arr.shape

#Devuelve (2,3)
También puede combinar el método  reshape con el atributo  shape en una línea como esta:

arr.reshape(2,3).shape

#Devuelve (2,3)
Cómo encontrar el valor máximo y mínimo de un arreglo NumPy
Para concluir esta sección, aprendamos cuatro métodos útiles para identificar los valores máximo y mínimo dentro de un arreglo NumPy. Trabajaremos con este arreglo:

simple_array = [1, 2, 3, 4]
Podemos usar el método max para encontrar el máximo valor de un arreglo de NumPy. A continuación se muestra un ejemplo.

simple_array.max()

#Devuelve 4
Podemos usar también el método argmax para encontrar el índice del máximo valor dentro de un arreglo. Esto es útil cuando deseas encontrar la ubicación del valor máximo pero no necesariametne te interesa su valor en si.

Un ejemplo se observa a continuación.

simple_array.argmax()

#Devuelve 3
En forma similar, podemos usar los métodos min y argmin para encontrar el valor e índice del mínimo valor dentro de un arreglo de NumPy.

simple_array.min()

#Devuelve 1

simple_array.argmin()

#Devuelve 0

---> En esta sección, analizaremos varios atributos y métodos de los arreglos de NumPy.

---> Métodos y Operaciones de NumP
En esta sección, trabajaremos a través de varias operaciones incluidas en la biblioteca NumPy.

Asumiremos que el comando import numpy as np ya ha sido ejecutada.

Arreglo de longitud 4 creada usando np.arange en todos los ejemplos.

arr = np.arange(4)

arr
Los valores del arreglo están debajo.

array([0, 1, 2, 3])
Cómo realizar operaciones aritméticas en Python usando NumPy
NumPy facilita realizar operaciones aritméticas con arreglos. Puedes realizarlas usando el arreglo y un sólo número, o puedes realizarlas entre dos arreglos NumPy.


Suma
Al sumar un sólo número a un arreglo de NumPy, ese número se suma a cada elemento en el arreglo. A continuación se ve un ejemplo:

2 + arr

#Devuelve array([2, 3, 4, 5])
Puedes sumar dos arreglos NumPy usando el operador +. Los arreglos se suman elemento por elemento (lo que significa que los primeros elementos se suman entre si, los segundos elementos se suman se suman entre se, y así sucesivamente).

A continuación se ve un ejemplo.

arr + arr

#Devuelve array([0, 2, 4, 6])
Resta
Como la suma, la resta se realiza elemento por elemento para arreglos de NumPy. Puedes encontrar un ejemplo para el caso de un solo número y para el de otro arreglo NumPy a continuación

arr - 10

#Devuelve array([-10,  -9,  -8,  -7])

arr - arr

#Devuelve array([0, 0, 0, 0])
Multiplicación
La multiplicación también se realiza elemento por elemento tanto para casos de un sólo número como para casos de opraciones entre arreglos de NumPy.

A continuación se ven dos ejemplo.

6 * arr

#Devuelve array([ 0,  6, 12, 18])

arr * arr

#Devuelve array([0, 1, 4, 9])
División

Ejemplo de división de arr por un sólo número se ve a continuación:

arr / 2

#Devuelve array([0. , 0.5, 1. , 1.5])


Un ejemplo de dividir por cero es con un arreglo NumPy que se muestra a continuación.

arr / arr

#Devuelve array([nan,  1.,  1.,  1.])
Aprenderemos cómo tratar los valores nan con más detalle más adelante en este curso.

Operaciones complejas en arreglos de NumPy
Muchas operaciones no se pueden realizar simplemente aplicando la sintaxis normal a un arreglo NumPy. En esta sección, exploraremos varias operaciones matemáticas que tienen métodos incorporados en la biblioteca NumPy.

¿ Cómo calcular raíz cuadrada usando NumPy ?

Calcular la raíz cuadrada de cada elemento en un arreglo usando el método np.sqrt:

np.sqrt(arr)

#Devuelve array([0., 1., 1.41421356, 1.73205081])
A continuación se muestran muchos otros ejemplos (ten en cuenta que no te serán evaluados, pero aún así es útil ver las capacidades de NumPy):

np.exp(arr)

#Devuelve e ^ elemento para cada elemento del arreglo

np.sin(arr)

#Calcula el seno trigonométrico de cada valor en el arreglo

np.cos(arr)

#Calcula el coseno trigonométrico de cada valor en el arreglo

np.log(arr)

#Calcula el logaritmo en base diez de cada valor en el arreglo


----> Indexación y Asignación en NumPy
La indexación y la asignación en arreglos NumPy.

El arreglo que usaré en esta sección

Esta vez se generará utilizando el método np.random.rand. Así es como generé el arreglo:

arr = np.random.rand(5)
Aquí está el arreglo real:

array([0.69292946, 0.9365295 , 0.65682359, 0.72770856, 0.83268616])
Para que este arreglo sea más fácil de ver, redondearé cada elemento a 2 decimales usando el método round de NumPy:

arr = np.round(arr, 2)
Aquí está el nuevo arreglo:

array([0.69, 0.94, 0.66, 0.73, 0.83])
Cómo retornar un elemento específico de un arreglo de NumPy
Podemos seleccionar (y retornar) un elemento específico desde un arreglo NumPy de la misma forma que realiza con una lista normal de Python: usando los corchetes.

Un ejemplo se ve a continuación:

arr[0]

#Devuelve 0.69

Referenciar usando los dos puntos. Por ejemplo:  el índice [2:] selecciona cada elemento desde el índice 2 en adelante. El índice [:3] selecciona cada elemento hasta el índice 3 excluido. El índice [2:4] retorna cada elemento desde el índice 2 al índice 4, excluyendo este último. El criterio de valoración más alto siempre se excluye.

A continuación se muestran algunos ejemplos de indexación mediante el operador de dos puntos.

arr[:]

#Retorna el arreglo completo: array([0.69, 0.94, 0.66, 0.73, 0.83])

arr[1:]

#Devuelve array([0.94, 0.66, 0.73, 0.83])

arr[1:4] 

#Devuelve array([0.94, 0.66, 0.73])

Asignación de elementos en arreglos de NumPy
Podemos asignar nuevos valores a un elemento de un arreglo NumPy usando el operador =, al igual que las listas de Python normales. A continuación se muestran algunos ejemplos (ten en cuenta que todo esto es un bloque de código, lo que significa que las asignaciones de elementos se llevan adelante de paso a paso)

array([0.12, 0.94, 0.66, 0.73, 0.83])

arr

#Devuelve array([0.12, 0.94, 0.66, 0.73, 0.83])

arr[:] = 0

arr

#Devuelve array([0., 0., 0., 0., 0.])

arr[2:5] = 0.5

arr

#Devuelve array([0. , 0. , 0.5, 0.5, 0.5])


Referenciación de arreglos en NumPy
NumPy hace uso de un concepto llamado "Referencia de arreglos" (array referencing) que es una fuente común de confusiones para las personas que son nuevas en la librería.

Para entender la referencia de arreglo, primero veamos un ejemplo:


new_array = np.array([6, 7, 8, 9])

second_new_array = new_array[0:2]

second_new_array

#Devuelve array([6, 7])

second_new_array[1] = 4

second_new_array 

#Devuelve array([6, 4]), como se esperaba

new_array 

#Devuelve array([6, 4, 8, 9]) 

#que es DIFERENTE de su valor original de array([6, 7, 8, 9])

#¿Que ha pasado?
Como puedes ver, la modificación de second_new_array cambió también el valor de new_array.

¿Por qué es esto?

Por defecto, NumPy no crea una copia de un arreglo cuando hace referencia a la variable del arreglo original usando el operador de asignación =. En cambio, simplemente apunta la nueva variable a la anterior, lo que permite que la segunda variable realice modificaciones en la variable original, incluso si esta no es tu intención.

Puede utilizar el método copy para copiar explícitamente un arreglo NumPy.

A continuación se muestra un ejemplo de esto.

array_to_copy = np.array([1, 2, 3])

copied_array = array_to_copy.copy()

array_to_copy

#Returns array([1, 2, 3])

copied_array

#Returns array([1, 2, 3])
Como puede ver a continuación, realizar modificaciones al arreglo copiado no altera el original.

copied_array[0] = 9

copied_array

#Devuelve array([9, 2, 3])

array_to_copy

#Devuelve array([1, 2, 3])
Hasta ahora en la sección, solo hemos explorado cómo hacer referencia a arreglos NumPy unidimensionales. Ahora exploraremos la indexación de matrices bidimensionales.

Indexando arreglos NumPy de dos dimensiones
Para comenzar, creemos un arreglo NumPy de dos dimensiones llamado mat:

mat = np.array([[5, 10, 15],[20, 25, 30],[35, 40, 45]])

mat

"""

Devuelve:

array([[ 5, 10, 15],

       [20, 25, 30],

       [35, 40, 45]])

"""
Hay dos formas de indexar un arreglo NumPy de dos dimensiones:

mat[fila, columna]
mat[fila][colulma]

#Primero, vamos a conseguir la primera fila:

mat[0]

#Luego, obtengamos el último elemento de la primera fila:

mat[0][-1]
También puede generar submatrices a partir de un arreglo NumPy bidimensional utilizando esta notación:

mat[1:][:2]

"""

Devuelve:

array([[20, 25, 30],

       [35, 40, 45]])

"""
La referencia de arreglos también se aplica a arreglos bidimensionales en NumPy


---> Selección condicional mediante arreglos de NumPy

Los arreglos NumPy admiten una función llamada conditional selection, que le permite generar un nuevo arreglo de valores booleanos que indican si cada elemento dentro del arreglo satisface una declaración if particular.

arr = np.array([0.69, 0.94, 0.66, 0.73, 0.83])

arr > 0.7

#Devuelve array([False,  True, False,  True,  True])
También puedes generar un nuevo arreglo de valores que satisfagan esta condición pasando la condición entre corchetes 

arr[arr > 0.7]

#Devuelve array([0.94, 0.73, 0.83])

