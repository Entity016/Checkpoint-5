**#¿Qué es un condicional?**  

**##if**  

Los condicionales son bloques de codigo que permiten tomar decisiones en base a las propias condiciones, de ahi el nombre de  condicional, para analizar y dar respuestas segun los datos que haya.  
Estos se basan en la condicion **True** y **False**
Para ilustrarlo de forma gráfica, muestro al siguente imagen:  

![src = images/SENTIFELSE.jpg](diagrama basico if-else)  

Hay varias formas de analizar los datos, como primera opcion tenemos **if**, que es el condicional por excelencia, que nos permite comprobar diferentes factores, como si los numeros son pares/impares, buscar palabras en una frase o en una lista de nombres, o poner condiciones para activar otras lineas de codigo.  
Un ejemplo de ello:

~~~
number = 4

if number % 2 == 0:
    print('es un numero par')
~~~

**##else**  

Este codigo nos muestra y analiza si el numero que le mostramos es par, pero,  
¿Y si queremos saber si es impar?  
¿Y si el dato no es un numero?  
Entonces ahi es donde entran la condicional **else**.  
Lo que hace el condicional else es decir: "si no se cumple en el 'if', se hace lo siguiente", asi se ve en el sigueinte ejemplo, donde uso la condicional *else* para decir, "si el numero no es par, y por tanto con cumple la condicion del 'if', hacemos los declarado en el 'else'"
Como por ejemplo:

~~~
number = 3

if number % 2 == 0:
    print('es un numero par')
else:
    print('es un numero impar')
~~~  

El output de este codigo seria: es un numero impar

**##elif**  

Luego viene otra condicional, donde, en este caso, podemos añadir haciendo una pequeña variación al codigo, digamos que ahora queremos saber, si es **multiplo de 3, de 5**, y luego, saber **si no es ninguno**, entonces ahi es donde entra la tercera, la condicional **elif**, que es una variable hibrida entre el *if* y *else*, que a terminos practicos viene a ser: " Si no se cumple la condicion en el if anterior, se prueba con el elif siguiente", pero esta condicional no sustituye al else, este siempre se tiene que poner para que en caso de que el *if* ni el *elif*, no haya error.  
Ejemplo de los condicionales con **if**, **elif** y **else**:

~~~
number = 25

if number % 3 == 0:
    print('Este numero es multiplo de 3')
elif number % 5 == 0:
    print('Este numero es multiplo de 5')
else:
    print('Este numero no es multiplo de 3 ni de 5')
~~~

Finalmente el output de este codigo seria: Este numero es multiplo de 5  

**##Sangria**  

Por otra parte, tenemos otras condiciones que afectan. Como por ejemplo la sangria/sangrado, en ingles, 'indentation'. Esto especifica en que bloque estan las ordenes y las condiciones, y la falta, o lo contrario, pueden desencadenar en un error de el codigo.
Por ejemplo, aqui tenemos un codigo con un error:

~~~
number = 3

if number % 3 == 0:
    print('Este numero es multiplo de 3')
    elif number % 5 == 0:
    print('Este numero es multiplo de 5')
else:
    print('Este numero no es multiplo de 3 ni de 5')
~~~

El primer error que veriamos, seria en el *elif*, que esta adelantado, y estria metido en el bloque de ordnenes de la condicion *if*, y por tanto, el codigo seria erroneo.  
Ademas de eso, fijemonos en el ultimo print, este ultimo esta puesto para quien sea que use el codigo, reciba un agradecimiento, pero tambien, al estar adelantado, estaria metido en el bloque de ordenes de el *else*, y el usuario solo recibiria el agradecimiento cuando se cumpliera la condicion *else*.  
El ejemplo de el codigo correcto seria asi:  

~~~
number = 3

if number % 3 == 0:
    print('Este numero es multiplo de 3')
elif number % 5 == 0:
    print('Este numero es multiplo de 5')
else:
    print('Este numero no es multiplo de 3 ni de 5')
print('Gracias por usar el programa')
~~~

Ahora si, se cumpliran las ordenes en el orden correcto, segun las condiciones correctas y no habra errores.  

**##Anidadas**  

Ahora que hemos hablado de la sangria, hablaremos de un ultimo tema, algo mas complejo que las condicionales comunes, que son las condicionales anidadas. En este caso, ocurrira que habra o nos tocara programas una condicional dentro de otra, y para ello pondremos el ejemplo para explicarlo de forma gráfica:

~~~
def mezclacolores(a, b):
    if a == 'rojo':
        if a == 'rojo' and b == 'azul':
            return 'morado'
        elif a == 'rojo' and b == 'amarillo':
            return 'naranja'
    elif b == 'azul':
        if a == 'azul' and b == 'amarillo':
            return 'verde'
        elif a == 'azul' and b == 'rojo':
            return 'morado'
    else:
        return 'color no definido'
~~~

El ejemplo tomara el primer color, y en caso de que la primera condicion sea verdad, pasara a la primera condicion interna, y asi hasta que encuentre una condicion que se cumpla, o todas sean falsas y llegue al *else*

**#¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?**

Los bucles nos permiten modificar el flujo del programa, y por ejemplo nos permiten repetir una porcion de codigo tantas veces como sea necesario, 
Los dos principales tipos de bucle son **for** y **while**.  

**##While**  

Por una parte, tenemos el bucle **while**, que se basa en la afirmacion **True** o **False**:  
-True: sigue con el bucle.  
-False: Termina el bucle
Por esto mismo, a menos que queramos un bucle infinito, debemos añadir un contador o un valor asignado al *False*, para que el bucle pare llegado a ese valor, que puede ser un contador, o el final de una lista.
En el ejemplo, haremos que un rango de numeros se multiplique por dos cada uno:

**!!!!BUCLE INFINITO NO EJECUTAR!!!!!**
~~~
num = 0
while num <= 10:
    print(num*2)
~~~
**!!!!BUCLE INFINITO NO EJECUTAR!!!!!**  

Pero esto seria un bucle infinito, y si lo ejecutamos, solo nos mostraria una fila interminable de 0, porque nunca alncazaria el 10 que le hemos puesto, es un codigo sin sentido aparente, pero digamos que la necesitamos de esta manera, necesitamos que lo haga, digamos, 5 veces, entonces necesitariamos un contador, y le diremos que salte, a la vuelta 5 del bucle:

~~~
num = 0
contador = 0
while contador <= 5:
    print(num*2)
    contador += 1
~~~

Y asi, aunque la multiplicacion muestre 5 ceros, pero parara justo en el quinto 0. Aun asi, tambien puede pasar, como en el anterior codigo, que queriamos llegar al 10, entonces tendriamos que dar la orden de cortar el codigo ahi, pero poniendo un valor que de verdad pueda llegar al 10, y ademas haciendo que con cada iteración, o bucle, se vaya sumando a lo ya multiplicado.

~~~
num = 1
while num <= 10:
    print(num)
    num *= 2
~~~
Si se ejecuta, veremos que solo llega al 8, porque el siguiente '*2', lo llevaria al 16, entonces ahi se corta el bucle.

En los bucles **while** tambien tenemos las condicionales *if/else*, las cuales se podran anidar dentro de el bucle para tener mas posibilidades, pero digamos que queremos descartar un valor del codigo anterior

~~~
num = 1

while num <= 10:
    if num == 4:
        num *= 2  
        continue  
    else:
        print(num)

    num *= 2  
~~~

En este codigo, le hemos dicho lo mismo que en el anterior, pero le hemos avisado, que cuando el valor de 'num' sea 4, debera continuar, pero no le hemos dicho que haga 'print', por lo que no lo mostrara y pasara al siguiente valor.


**##for**  

Los '**for** loops', a diferencia de los **while**, ya se sabe cuantas veces se repetira el bucle, por lo que no sera necesario ponerle un limite.
Por ejemplo:

~~~
for num in range(0, 5)
    print(num)
~~~

Esta lista nos devolvera 0 1 2 3 4, sin el 5 porque los range paran justo en el valor indicado, si hubieramos querido el 5, tenddriamos que ajustar el rango  (0,6)
Tambien se puede hacer con 'strings', donde si por ejemplo, hicieramos:

~~~
palabra = 'python'
for letra in palabra:
    print(letra)
~~~

Esta condicional los devolvera las letras individuales, es decir p y t h o n.

Otras funciones que podemos utilizar serian los rangos, donde podriamos desde hacer 'print' a solo una parte de la palabra o saltarnoslas

~~~
palabra = "python"
for i in palabra[1:4]:
    print(i)
~~~

Este codigo nos devolvera y t h, porque empezara en el index 1, y acabara justo en el index 3

~~~
palabra = "python"
for i in palabra[::3]:
    print(i)
~~~

Por otro lado, esta condicional nos mostrara p h


Tambien se pueden hacer operaciones, a un numero, o a un conjunto, incluso a cada uno individualmente
Por ejemplo, digamos que tenemos una lista de numeros aleatorios, y queremos multiplicarlos por dos:

~~~
numeros = [39, 56, 78, 3, 109]

for num in range(len(numeros)):
    numeros[num] *=2

print(numeros)
~~~

En este codigo, podemos ver la lista de numeros, le asignamos a una variable, y luego asignamos un nombre a cada elemento, normalmente es el singular de la variable o una forma abreviada, en este caso numeros => num.  
Luego le asignamos el valor range(len(x)), el cual indica que la el bucle se debe repetir tantas veces como elementos haya en la variable. Asi que en este caso, coge cada elemento, lo multiplica por dos, y lo devuelve en su sitio.
Tambien podriamos cojerlos todos, y pedirle que le quite a cada uno 5, o le sume 10.

**##Break y Continue**

**Break** sirve para, justo despues de cumplir una condicion, cerrar el bucle, por ejemplo, si estariamos iterando en una palabra y solo queremos llegar hasta una letra, le ordenariamos que al llegar a esa letra saliera del bucle. El el siguiente ejemplo veremos su funcionamiento:

~~~
def buscador(palabra):
    for letra in palabra:
        print(letra)  # Imprime la letra actual
        if letra == 't':
            print('T encontrada')
            break  # Salimos del bucle cuando encontramos la 't'
    else:
        print('No se encontró t')

buscador('python')
~~~

Podemos ver como en este ejemplo, si lo ejecutamos, nos mostrara como empieza el bucle sobre la palabra 'python', pero como le hemos ordenado parar justo al llegar a la T, ahi al roto el bucle.  

Pero, que pasaria si queremos que se salte esa 'T', pues usamos **continue**

**Continue**, sirve para, en base a una condicion, hace que el bucle siga, pero con una condicion particular, y es que se salta el codigo restante por iterar, y pasa a la siguiente iteracion. Podemos verlo en el siguiente ejemplo:

~~~
x = 5
while x >= 0:
    if x == 2:
        x -= 1  
        continue
    print(x)
    x -= 1
~~~

En este ejemplo podemos ver, si lo ejecutamos, como el bucle va restando al 'x', pero cuando llega al 2, hace la resta pero se lo salta, pasando directamente al 1.

**#¿Qué es una lista por comprensión en Python?**  

En un resumen muy simple, las ~**listas de comprension** nos permiten crear listas con una sola linea de codigo, es decir, funcionalidades que llevarian procesos mas largos, por ejemplo, digamos que queremos hacer una lista de los 3 primeros numeros, todos ello elevados al cubo(**3), el proceso con listas de comprension seria tal que asi:  

~~~
lista = [num**3 for num in range(3)]
print(lista)
~~~

esto nos devolveria [0, 1, 8], que corresponderian al index:  
- 0=0 => 0**3=0
- 1=1 => 1**3=1
- 2=2 => 2**3=8  
Y con ello, nos devuelve la lista, que en cambio nos costaria varias lineas de codigo crear si las **listas de comprension** no existieran. En el proximo ejemplo crearemos la misma lista sin usar esta funcionalidad:

~~~
lista = []
for num in range(3):
    lista.append(lista**3)
print(lista)
~~~

El proceso es sencillo, se crea una lista vacia, luego se declara la condicional *for* en un rango de 3, y dentro de ella se da la orden de que cada numero hay que añadirlo elevandolo al cubo. Pero lo que con una linea hemos hecho, aqui son 3.

Dentro de las **listas de comprension** tenemo la posibilidad de hacer una lista de valor contante, como por ejemplo, una lista que muestre 3 unos:

~~~
unos = [1 for i in range(3)]
print(unos)
~~~

**#Funciones en listas de comprension**  

Por otro lado, tambien tenemos la posibilidad de **llamar a funciones** dentro de las **listas de comprension**

~~~
def eleva_tres(num):
    return num ** 3

lista = [eleva_tres(i) for i in range(5)]
print(lista)
~~~

En este caso hemos declarado la funcion, y luego la hemos llamado dentro de la lista, el resultado seria [0, 1, 8, 27, 64]  

**##Condicionales en listas de comprension**  

Al igual que hemos demostrado con las funciones, tambien podemos usar **condicionales** dentro de las **listasde comprension**, lo que nos serviria por ejemplo si queremos hacer una lista solo con ciertos elementos de otra lista.   
Vamos a poner un ejemplo, filtrando una lista en base a un criterio:

~~~
lista = ['azul', 'arena', 'verde', 'amigo', 'reina']
lista_filtrada = [palabra for palabra in lista if palabra.startswith('a')]

print(lista_filtrada)
~~~

Una vez hecho esto, lo que nos mostraria seria: ['azul', 'arena', 'amigo']; habiendo solo seleccionado y hecho una lista independiente con las palabras que empiezan por 'a', de ahi el '.startswith()'

**##Sets en listas de comprension**  

Los **sets** tienen varias condiciones, entre ellas, que no permiten duplicados y son inmutables, pero quitando esas caracteristicas, son muy similares, lo unico que cambiaria es que los set estan envueltos por parentesis **()**, entonces habria que cambiarlos por **{}**.
Un ejemplo de ello seria:  

~~~
numeros = {1, 2, 3, 4, 5}

numeros_cuadrado = [num**2 for num in range(1, 11)]
print(numeros_)

cuadrado_pares = [num**2 for num in range(1, 11) if num % 2 == 0]
print(cuadrado_pares)
~~~

Aqui vemos como hemos creado el set, pero con {}, y luego tenemos dos  de comprension, la primera nos devolvera [1, 4, 9, 16, 25], mientras que en la segunda, en la que hemos usado la condicional *if*, nos devolvera solo los numeros pare elevados al cuadrado [4, 16].

**##Diccionarios en listas de comprension**  

Los **diccionarios** en las listas de comprension son muy similares a los sets, pero lo que cambia aqui es que tenemos **key: value**, pero con funciones en una sola linea, podemos, convertir dos listas o dos sets, en un diccionario, por ejemplo:  

~~~
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pablo', 23, 'Bizkaia']

dicc = {x:y for x,y in zip(lista1, lista2)}
~~~

Aqui vemos como hemos cogido la dos listas y les hemos asignado a uno los key, y en otro los value, y le ordenamos ponerlos en un diccionario, repetando el orden, asignando al primer elemento de la primera lista *key*, y al primer elemento de las segunda lista *value*. asi que lo que nos devolveria seria:  

~~~
print(dicc)

dicc = {'nombre': 'Pablo', 
        'edad': 23, 
        'región': 'Bizkaia'}
~~~

En conclusion, las listas de comprension y sus variantes tienen mucha utilidad, practicidad y funcionalidad para poder resumi funciones y operaciones mas largas y complejas a una sola linea, pero esto no significa que las haga faciles, para saber hacer una linea de comprension, hay que saber como hacer de la forma compleja tambien, para saber comprimirlo correctamente en una linea.

**#¿Qué es un argumento en Python?**  

Los argumentos o en la nomenclatura dentro de pythons : *args*; de forma muy superficial y resumida, son los datos que necesita una funcion para poder trabajar, y hay de distintos tipos:  

**##Argumentos Posicionales**  

Como el provio nombre indica, estos argumentos funcionan basandose en su posicion. es decir, que si tenemos *(a, b)* la funcion dara por hecho que *a* es el primer valor y *b* es el segundo. Por esto mismo es el tipo de argumento mas basico e intuitivo. He aqui un ejemplo:

~~~
def resta(a, b):
    resta = a - b
    return resta
print(resta(10, 5))
~~~

La anterior funcion, con los **argumentos posicionales** entregados en el 'print', muestra un 5, y no hay que olvidar poner 'return' en estas funciones, ya que luego si no, en vez de 5, mostrara 'none' al no devolver ningun valor la funcion.  
Algo importante a destacar es que una funcion no podra tomar mas argumentos de los definidos en el caso de los **posicionales**, ya que daria error al no saber que hacer con esos valores.


**##Argumentos por nombre**  

En este tipo de argumentos se utiliza el nombre para asignarles un valor, y a diferencia de los *argumentos posicionales*, el orden da igual. En el siguiente ejemplo lo mostraremos de manera grafica:  

~~~
def resta(a, b):
    resta = a - b
    return resta
print(resta(b = 10, a = 5))
~~~

Como se puede ver, hemos utilizado los **argumentos por nombre para invertir el sentido de la operacion, por lo que el resultado que mostraria seria -5. Aqui tampoco se podria pasar un valor 'c', por ejemplo, porque tambien provocaria un error al no estar definido el valor en la funcion.

**##Argumentos por defecto**  

Estos tipos de argumento se les asgina un valor en la misma funcion, que es el valor por defecto que se utilizara a menos que se le otorgue un valor nuevo. Este tipo de argumentos se utiliza mucho en funciones en las que se contempla la posibilidad de quedar vacias, y los **argumentos por defecto** evitarian que la funcion provocara un error. Aqui mostramos un ejemplo de una funcion con un valores por defecto:

~~~
def resta(a, b, c = 0):
    resta = a - b - c
    return resta
print(resta(10, 5))
~~~

Por una parte tendriamos los valores por defecto, que en este caso, al tener un valor por defecto, no es necesario aportarle un valor 'c', nos mostrara un valor 5, pero, si le aplicamos otro valor al argumento 'c':

~~~
def resta(a, b, c = 0):
    resta = a - b - c
    return resta
print(resta(10, 5, 2))
~~~

Aqui el valor por defecto lo sustituiria el 2, por lo que nos mostraria un resultado de 3.

**##Argumentos de longitud variable**  

Esta clase de argumentos permite tener in numero indeterminado de argumentos, que tienen que estar vinculados a la variable que se establece como argumento. Para explicar esto, digamos que queremos una funcion que sume listas de numeros:

~~~
def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

numeros = [1, 2, 3, 4, 5]
print(suma(numeros))
~~~

A esta funcion le entregamos una lista de numeros, y dentro de la funcion le asignamos una variable vacia, que es en la que nos devolvera la suma ya hecha, entonces con la condicional *for* le asignamos la suma a cada elemento de la lista, y no muestra 15.  
La lista que le asignamos podria haber sido diferente, y tener, o 5 elementos, o 10, o 100, de ahi el nombre **argumentos de longitud variable**

**##args y kwargs**  

Con **args** abreviatura de **arguments**, podemos definir funciones curyo numero de argumentos es variable, es decir, funciones que se adaptan a numero de argumentos con los que son llamados.  
Lo mostraremos un ejemplo:  

~~~
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(suma(1, 3, 4, 2))
~~~

Este codigo nos mostraria un 10, y tenemos 4 argumentos, en cambio, si ponemos 2 argumentos, como en el siguiente ejemplo, usamos dos argumentos:  

~~~
print(suma(1, 1))
~~~

Este nos dara 2, pero tiene dos argumentos, por ello podemos observar que las funciones con argumentos *args*. Eso si, el uso de args es completamente arbitrario, por lo que podria llamarse con cualquier nomenclatura, pero debido a las convencion entre los usuarios de Python, pero lo que si debe tener si o si como requisito es el asterisco (*)args.  
Notese que con los argumentos de *args hemos utilizado una tupla, para que pueda ser iterado. Ademas, el ejemplo se podria simplificar mucho mas:  

~~~
def sum(*args):
    return sum(args)
print(suma(5, 5, 3))
~~~

Asi vemos, como esta funcion mas simplificada hace el mismo trabajo que la anterior, lo que nos mostraria un valor de 13=5+5+3.  

En cambio, con los argumentos (*kwargs), o los **key word arguments**, pero como los *args, este nombre es una convencion entre los ususarios y podrias usar el nombre que quisieras respetando el (**), pero es mejor usar el nombre que se establece por convencion, ya que eso es considerado como buena practica.  
Lo que diferencia a los *kwargs* de los *args*, a parte del doble asterisco o el asterisco simple respectivamente, es que en los *kwargs* es que trabajaremos con un diccionario, y esta caracteristica nos permite dar nombre a los argumentos de entrada. Lo mostraremos en el siguente ejemplo:  

~~~
suma(a=3, 
     b=10, 
     c=3)
~~~

Con este diccionario como valores, con 'a', 'b' y 'c' como *key* y '3', '10' y '3' como *value* de esos *keys*. Ejecutamos la siguiente funcion:

~~~
def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s
    

print(suma(a=3, b=10, c=3))
~~~

Y esto nos mostrara, la immpresion del diccionario que tenemos como argumento, y tambien nos devolvera la suma de los *value*, que mostraremos con el 'print'.  

Una vez entendido el concepto de los *args* y *kwargs*, podemos complicar un poco mas las cosas, mezclando tipos de argumentos en una funcion, eso si, antes de continuar debemos dejar claro que los argumentos de funciones mixtas deben seguir un orden determinado.  
1. Argumentos normales  
2. *args
3. **kwargs  
Estos nos serviran, o bien para completar una funcion, añadiendo a argumentos fijos, un argumento *args* para asegurar que la funcion se pueda adaptar. Otra capacidad que tambien tendrian seria la capacidad de extraer los valores individualmente de una tupla y pasarlos como argumentos, un truco llamado *tuple unpacking*, he aqui un ejemplo:

~~~ 
def unpack_tuple(*args):
    for arg in args:
        print("args =", arg)

args = (1, 2, 3)
unpack_tuple(*args)
~~~

Esta funcion, nos mostrara los valores pertenecientes a args individualmente:  
- args = 1  
- args = 2  
- args = 3  

En conclusion, estos son los argumentos de python, y hay que saber usarlos dependiendo de las condiciones, exigencias, tipos de datos a introducir o zi el numero de argumentos variara, lo importante es usar la buena practica para que el codigo sea lo mejor posible.

**#¿Qué es una función Lambda en Python?**  

Las **funciones lambda** se usan para definir un codigo en una sola linea, normalmente una función, y una cita sacada textualmente de la documentación oficial dice tal que asi:  
>“Python lambdas are only a shorthand notation if you’re too lazy to define a function.”  

Asi que, para explicarlo de una forma grafica, lo demostratremos con, primero una funcion común referente a una resta:

~~~
def resta(x, y):
    r = 0
    r = x - y
    return r
print(resta(9, 5))
~~~

Esta simple funcion nos mostrara 4, pero ahora, podemos hacerlo en una sola linea, con la **funcion lambda**:  

~~~
resta = lambda x, y : x - y
print(resta(9, 5))
~~~

Esta *funcion lambda* nos devolvera el mismo resultado que la funcion convencional, pero es importante saber, que se deben asignar a una variable, si no no serviran.  
Tambien podriamos utilizarla, con valores por defecto, que se haria exactamente igual que en una funcion normal:

~~~
valor_defecto = lambda a, c, b = 0 : a + b + c
~~~

Otra posibilidad disponible tambien seria llamar a los argumentos por el nombre, como en el siguiente ejemplo:

~~~
func_lambda = lambda x, y : x + y
print(func_lambda(y = 9, x = 1))
~~~

El cual nos daria 10, y funcionaria exactamente ccomo si en una funcion convencional llamaramos a los argumentos por su nombre.

Por otra parte, las *funciones lambda*, tambien tienen otras funciones interesantes, como el *tuple unpacking*, como en el siguiente ejemplo:

~~~
lambda_arg = lambda *args : sum(*args)
args = (1, 2, 3)
~~~

Donde teniendo una tupla, podemos extraerle los valores individualmente y pasarlos como argumentos.  

Relacionado con esto, tambien tenemos la posibilidad, de usando los *kwargs*, de poder introducir valores en forma de *key* y *value*, como en el siguiente ejemplo:

~~~
dicc_lambda = lambda **kwargs : sum(kwargs.values())
print(dicc_lambda(x = 1, y = 2, z = 3))
~~~

En esta *funcion lambda*, le hemos ordenado sumar los *value* del diccionario, lo que nos mostrara como resultado un 6.

En conclusion podemos ver que con la **funcion lambda** podemos crear funciones en una linea, ahorrandonos las multiples lineas de las **convencionales**, pero para ello hay que dominar bien la sintaxis del condigo para que funcione correctamente en los diversos escenarios.

**#¿Qué es un paquete pip?** 

**PIP**, que quiere decir Pip Installs Packages, es una herramineta para instalar, desinstalar y/o actualizar modulos y bibliotecas desde el Python Package Index (PyIP), y para buscar los modules y ver como tenemos que instalarlos, podemos entrar en: https://pypi.org/  

La definicion basica del **paquete pip** seria la siguiente:  
>pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.

Asi que en base a esta definicion, podemos suponer que esta herramienta es muy util, ya que con una sola linea de codigo, como podemos ver un los siguientes ejemplos, podemos instalar paquetes de diversas funciones que nos resultaran utiles a la hora de ordenar los codigos, o procesar el *output* de distintas maneras incluso trabajar de forma remota o crear entornos virtuaales, aqui mostramos el ejemplo para instalar o desinstalar:

~~~
pip install paquete
pip uninstall paquete
~~~

Pero primeramente, para verificar si tenemos pip:

~~~
pip --version
~~~

Tambien tenemos la opcion de instalarlo con el siguiente comando de una linea:

~~~
python -m ensurepip --upgrade
~~~

Una vez instalado, tenemos diversas opciones, como por ejemplo, un paquete para realizar solicitudes http, tendriamos que ejecutar la instalacion del paquete **requests**

~~~
pip install requets
~~~

Pero, y si ademas de este paquete, quisieramos instalar mas de un paquete, como por ejemplo el paquete **numpy**, se podria hacer, poniendo cada paquete separado por un espacio:

~~~
pip install requests numpy
~~~

Despues, tenemos la opcion para que encaso de ser una aplicacion grande con varios modulos y queremos que todo funciones correctamente, podemos crear una bibloteca con todos los paquetes instalados con el siguiente comando:

~~~
pip freeze > requirements.txt
~~~

Y luego, si queremos instalas esas bibliotecas o dependencias, incluso en un entorno de desarrllo nuevo, tendriamos que usar el comando:

~~~
pip install -r requirements.txt
~~~

Luego, tambien tenemos la opcion de buscar actualizaciones y si las hay, actualizar la biblioteca, en caso de que ya estuvieran actualizadas, el sistema avisaria que ya esta en su version mas reciente. El comando de actualizacion es el siguiente:

~~~
pip install --upgrade paquete
~~~

Otra posibilidades que se nos abren al usar esta herramienta es:

1. *Crear y usar entornos virtuales.* 

Creacion  
~~~
python -m venv mi_entorno
~~~

Activacion(siguiendo el directiori de tu ordenador, esto solo es un ejemplo)
Windows
~~~
mi_entorno\Scripts\activate
~~~
Activacion
MacOS y Linux
~~~
source mi_entorno/bin/activate
~~~

Desactivacion
~~~
Deactivate
~~~

2. *Instalacion de paquetes desde fuentes locales o repositirios remotos*  

Desde fuentes locales:
    Como archivo:
    ~~~
    pip install nombre_paquete.whl
    ~~~

    Como directorio:
    ~~~
    pip install -e ./directorio_paquete
    ~~~
Desde repositorios remotos:
    Ejemplo de instalacion desde GitHub:
    ~~~
    pip install git+https://github.com/usuario/repositorio.git
    ~~~

Ademas, tenemos la opcion de la reinstalacion forzosa, y borrando el cache, para instalar la aplicacion desde 0:
~~~
pip install --no-cache-dir paquete
~~~
