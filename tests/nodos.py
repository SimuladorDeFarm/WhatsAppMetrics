# Definir la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"


# Definir el nodo de la lista doblemente enlazada
class Nodo:
    def __init__(self, persona):
        self.persona = persona  # El valor del nodo es un objeto de la clase Persona
        self.prev = None        # Puntero al nodo anterior
        self.next = None        # Puntero al nodo siguiente


# Definir la lista doblemente enlazada
class ListaDobleEnlazada:
    def __init__(self):
        self.head = None  # Referencia al primer nodo de la lista
        self.tail = None  # Referencia al último nodo de la lista

    # Insertar un nodo al final de la lista
    def insertar_al_final(self, persona):
        nuevo_nodo = Nodo(persona)
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo  # Enlazar el último nodo actual con el nuevo
            nuevo_nodo.prev = self.tail  # El nuevo nodo apunta de vuelta al anterior
            self.tail = nuevo_nodo       # El nuevo nodo se convierte en el último nodo

    # Recorrer la lista de inicio a fin e imprimir cada persona
    def imprimir_lista(self):
        actual = self.head
        while actual:
            print(actual.persona)  # Imprimir la persona contenida en cada nodo
            actual = actual.next

    # Recorrer la lista de fin a inicio e imprimir cada persona
    def imprimir_reverso(self):
        actual = self.tail
        while actual:
            print(actual.persona)
            actual = actual.prev


# Crear instancias de Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)
persona3 = Persona("Pedro", 40)

# Crear la lista doblemente enlazada llamada 'personas'
personas = ListaDobleEnlazada()

# Insertar las personas en la lista doblemente enlazada
personas.insertar_al_final(persona1)
personas.insertar_al_final(persona2)
personas.insertar_al_final(persona3)

# Imprimir la lista en orden
print("Lista en orden:")
personas.imprimir_lista()

# Imprimir la lista en orden inverso
print("\nLista en reverso:")
personas.imprimir_reverso()
