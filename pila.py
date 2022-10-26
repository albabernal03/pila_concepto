class nodoPila(object): # establecemos dentro un objeto el 

    info, sig = None, None   # El info es el dato que se almacena en el nodo que hace referencia al tipo de dato que se va a almacenar en la pila y el sig es el puntero que apunta al siguiente nodo de la pila; el nodo es el elemento que se va a almacenar en la pila. Los establecemos ambos con None para que no apunten a nada. 

class Pila(object):
    def __init__(self):
        self.cima= None #  
        self.tamanio= 0 # El tamanio es el tamaño de la pila, en este caso es 0 porque no hay nada en la pila.

    def apilar(pila, dato): # El dato es el elemento que se va a almacenar en la pila.  La pila es la pila que se va a utilizar.
        nodo = nodoPila() # Creamos un nodo de la clase nodoPila que es el que va a almacenar el dato.
        nodo.info = dato # El nodo.info  sirve para guardar el tipo de dato que se va a almacenar en la pila. usamos .info porque es el atributo que se establecio en la clase nodoPila.
        nodo.sig = pila.cima # El nodo.sig es el puntero que apunta al siguiente nodo de la pila, en este caso apunta a la cima de la pila que es el ultimo elemento que se apilo.  Usamos el pila. para que sepa que es un atributo de la clase pila.
        pila.cima = nodo # El nodo.cima es el puntero que apunta a la cima de la pila, en este caso apunta al nodo que se acaba de crear. Usamos el nodo. para que sepa que es un atributo de la clase nodoPila.
        pila.tamanio += 1 # El pila.tamanio es el tamaño de la pila, en este caso se le suma 1 porque se acaba de apilar un elemento en la pila. Usamos el pila. para que sepa que es un atributo de la clase pila.


    def desapilar(pila): # La pila es la pila que se va a utilizar.
        x= pila.cima.info # El x es el elemento que se va a desapilar, en este caso es el elemento que esta en la cima de la pila. Usamos el pila. para que sepa que es un atributo de la clase pila  y el info ya que sirve para guardarlo
        pila.cima = pila.cima.sig # El pila.cima es el puntero que apunta a la cima de la pila, en este caso apunta al siguiente elemento de la pila.  esto lo definimos para que el siguiente elemento de la pila sea el nuevo elemento de la cima de la pila. Usamos el pila. para que sepa que es un atributo de la clase pila.
        pila.tamanio -= 1 # El pila.tamanio es el tamaño de la pila, en este caso se le resta 1 porque se acaba de desapilar un elemento en la pila. Usamos el pila. para que sepa que es un atributo de la clase pila.
        return x # El return x nos devuelve el elemento que se desapilo de la pila.

    def pilaVacia(pila): # La pila es la pila que se va a utilizar.
        return pila.cima == None # El pila.cima es el puntero que apunta a la cima de la pila, en este caso nos devuelve si la cima de la pila es igual a None, es decir, si la pila esta vacia. Usamos el pila. para que sepa que es un atributo de la clase pila.
    
    def en_cima(pila):
        if pila.cima is not None:
            return pila.cima.info # el .info es para que nos devuelva el dato que esta en la cima de la pila
        else:
            return None
    
    def tamanio_pila(pila):
        return pila.tamanio
    
    def barrido(pila):
        paux= Pila()
        while not pila.pilaVacia():
            paux.apilar(pila.desapilar())
        while not paux.pilaVacia():
            print(paux.en_cima())
            pila.apilar(paux.desapilar())

   

# caso se tiene una pila de números enteros y se desea dividirla en dos pilas, una con los números pares y otra con los impares: pedir 10 numeros


pila = Pila() 
pares = Pila()
impares = Pila()

for i in range(10):
    pila.apilar(int(input("Ingrese un numero: ")))

while not pila.pilaVacia():
    if pila.en_cima() % 2 == 0: # decimos que si el numero que esta en la cima de la pila es par, lo apile en la pila de pares # pongpo pila. para que sepa que es un atributo de la clase pila
        pares.apilar(pila.desapilar()) # apilamos el numero que esta en la cima de la pila en la pila de pares y lo desapilamos de la pila original
    else:
        impares.apilar(pila.desapilar()) #esto de usar impares.apilar(pila.desapilar()) es para que no se pierda el numero que esta en la cima de la pila original y se apile en la pila de impares y lo desapilamos de la pila original, es decir pila.desapilar() lo metemos dentro de los parentesis de impares.apilar() para que no se pierda el numero que esta en la cima de la pila original
print("Pila de pares: ")


while not pares.pilaVacia(): 
    print(pares.desapilar())

print("Pila de impares: ")

while not impares.pilaVacia():
    print(impares.desapilar())






