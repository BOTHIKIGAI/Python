""" 
¿Para que es la herencia?
-------------------------------------------------------------------------------
Dado que una clase hija hereda los atributos y métodos de la padre, nos puede
ser muy util cuando tengamos clases que se parecen entre si pero tienen ciertas
particularidades. En este caso en vez de definir un monton de clases que se
parecen entre si pero tienen ciertas particularidades. En este caso en vez de
definir un monton de clases para cada animal, podemos tomar los elementos comunes
y crear una clase Animal de la que hereden el resto, respetando por tanto la
filosofia DRY. Realizar estas abstracciones y buscar el denominador común para
definir una clase de la que hereden las demás, es una tarea de lo más compleja
en el mundo de la programación.

Para saber mas: El principio DRY (Don't Repeat Yourself) es muy aplicada en el
mundo de la programación y consiste en no repetir código de manera innecesaria.
Cuanto más codigo duplicado exista, más dificil de modificar y mas facil será
crear inconsistencias. Las clases y la herencia a no repetir codigo.
"""

""" 
Extendiendo y modificando métodos
Continuemos con nuestro ejemplo de perros y animales. Vamos a definir una clase
padre Animal que tendra todos los atributos y metodos genericos que los animales
pueden tener. Esta tarea de buscar el denominador comun es muy importante en
programación. Veamos los atributos:

- Tenemos la especie ya que todos los animales pertenecen a una.
- Y la edad, ya que todo vivo nace, crece, se reproduce y muere.

Y los metodos o funcionales:
- Tendremos el metodo de hablar, que cada animal implementara de una forma.
Los perros ladran, las abejas zumban y los caballos relinchan.
- Un método moverse. Unos animales lo haran caminando, otros volando.
- Y por ultimo un metodo describeme que seran comun.

Definamos la clase padre, con una serie de atributos comunes para todos los
animales como hemos indicado.
"""

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie;
        self.edad = edad;
    
    # Metodo generico pero con implementación particular
    def hablar(self):
        # Metodo vacio
        pass;
    
    # Metodo generico pero con implementación particular
    def moverse(self):
        pass;
    
    # Metodo generico con la misma implementación
    def describirme(self):
        print("Soy un animal del tipo ", type(self).__name__);
        
        
"""
Tenemos ya por lo tanto una clase generica Animal, que generaliza las
caracteristicas y funcionalidades que todo animal puede tener. Ahora creamos una
clase vacia, para ver como los métodos y atributos son heredados por defecto.
"""

class Perro(Animal): # Perro hereda de animal
    pass;

perro1 = Perro('Mamifero', 10);
perro1.describirme();

""" 
Con tan solo un par de lineas de codigo, hemos creado una clase que tiene todo
el contenido que la clase padre tiene, pero aqui viene lo que es verdad intere-
sante. Vamos a crear varios animales concretos y sobreescribir algunos de los
metodos que habian sido definidos en la clase Animal, como el hablar o el mover-
se, ya que cada animal se comporta de una manera distinta.

Podemos incluso crear nuevos métodos que se añadiran a los ya heredados, como en
el caso de la Abeja con picar().
"""

class Perro(Animal):
    def hablar(self):
        print("Gua");
    def moverse(self):
        print("Caminando en 4 patas");
        
class Vaca(Animal):
    def hablar(self):
        print("Muuu!");
    def moverse(self):
        print("Caminando en 4 patas");

class Abeja(Animal):
    def hablar(self):
        print("Bzzz!");
    def moverse(self):
        print("Volando");
    # nuevo metodo
    def picar(self):
        print("Picar!");
        
""" 
Por lo tanto ya podemos crear nuestros objetos de esos animales y hacer uso de
sus métodos que podrian clasificarse en tres:

- Heredades directamente de la clase padre: describirme()
- Heredados de la clase padre pero modificados: hablar() y moverse()
- Creados en la clase hija por lo tanto no existentes en la clase padre: picar()
"""

mi_perro = Perro('mamifero', 10);
mi_vaca = Vaca('mamifero', 23);
mi_abeja = Abeja('insecto', 1);

mi_perro.hablar();
mi_vaca.hablar();

mi_vaca.describirme();
mi_abeja.describirme();

mi_abeja.picar();