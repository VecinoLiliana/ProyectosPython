class Personaje:
    # Atributos de la clase
    #nombre = "Default"
    #fuerza = 0
    #inteligencia = 0
    #defensa = 0
    #vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        #Inventario vacío
        self.inventario = {'vida': 0, 'fuerza': 0, 'inteligencia': 0}

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print (self.nombre, "ha muerto")

    def dañar(self, enemigo):
        return max(0,self.fuerza - enemigo.defensa)
    
    def atacar (self, enemigo):
        daño = self.dañar(enemigo)
        if hasattr(enemigo,"escudo") and enemigo.escudo > 0:
            if daño < enemigo.vida_escudo:
                enemigo.vida_escudo -= daño
            elif daño >= enemigo.vida_escudo:
                enemigo.vida = max(0,enemigo.vida - daño + enemigo.vida_escudo)
                enemigo.escudo = 0
                enemigo.vida_escudo = 0
        else:
            enemigo.vida = max(0,enemigo.vida - daño)
        print (self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print ("Vida de", enemigo.nombre, "es", enemigo.vida)

    def agregar_pocima(self, pocima, cantidad):
        if pocima in self.inventario:
            self.inventario[pocima] += cantidad
            print(f"Se agregó {pocima} pociones de {pocima}. Inventario: {self.inventario}")
        else:
            print(f"Pócima no existente: {pocima}")

    def usar_pocima(self, pocima):
        if pocima in self.inventario and self.inventario[pocima] > 0:
            self.inventario[pocima] -= 1  

            if pocima == "Vida":
                puntos_curados = 20  
                self.vida += puntos_curados
                print(f"{self.nombre} ha usado una pócima de vida. +{puntos_curados} HP. Vida actual: {self.vida}")

            elif pocima == "Fuerza":
                incremento = self.fuerza * 0.5
                self.fuerza += incremento
                print(f"{self.nombre} ha usado una pócima de fuerza. Fuerza aumentada en un 50%. Fuerza actual: {self.fuerza:.2f}")

            elif pocima == "Inteligencia":
                incremento = self.inteligencia * 0.5
                self.inteligencia += incremento
                print(f"{self.nombre} ha usado una pócima de inteligencia. Inteligencia aumentada en un 50%. Inteligencia actual: {self.inteligencia:.2f}")

        else:
            print(f"{self.nombre} no tiene pociones de {pocima} disponibles.")

class Guerrero(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada,escudo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo
        self.vida_escudo = defensa * escudo

    #Sobreescribir impresión de datos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)

    #Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #Escoger navaja
    def escoger_navaja (self):
        opcion = int (input ("Escoge la navaja de la muerte:\n (1)Navaja suiza.... 10 \n (2)Navaja pioja.... 03\n >>>>>>>>>>>"))
        if (opcion == 1):
            self.espada = 10
        elif (opcion == 2):
            self.espada = 6
        else:
            print ("Valor inválido, intente de nuevo")
            #Vuelva a ejecutar el método escoger_navaja
            self.escoger_navaja()

        
class Mago(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #Sobreescribir impresión de datos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:", self.libro)

    #Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    #Escoger libro
    def escoger_libro (self):
        opcion = int (input ("Escoge el libro de la sabiduría:\n (1)El principito.... 10 \n (2)Crepúsculo.... 03\n >>>>>>>>>>>"))
        if (opcion == 1):
            self.libro = 10
        elif (opcion == 2):
            self.libro = 6
        else:
            print ("Valor inválido, intente de nuevo")
            #Vuelva a ejecutar el método escoger_navaja
            self.escoger_libro()

#crear todo los objetos
persona = Personaje("Angel Suárez", 20,15,10,100)
arturoSuarez = Guerrero( "Arturo Suárez", 20, 15, 10, 100,5,2)
gandalf = Mago("Gandalf",20, 15, 10, 100, 5)

#atributos antes de la tragedia
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()

#ataques sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)

#Atributos despues de la tragedia 
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()

#Uso de posima
persona.usar_pocima("Vida")
arturoSuarez.usar_pocima("Fuerza")
gandalf.usar_pocima("Inteligencia")


#arturoSuarez.escoger_navaja()
#print("El valor de espada es:", arturoSuarez.espada)

# Variable del constructor
# mi_personaje = Personaje ("EstebanDido", 100, 50, 45, 100)
# mi_enemigo = Personaje ("Angel", 70, 100, 40, 100)
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar (mi_enemigo)

#mi_personaje.morir()
# mi_personaje.imprimir_atributos()
# mi_personaje.subir_nivel(15,5,10)
# print ("Valores actualizados")
# mi_personaje.imprimir_atributos()
# print (mi_personaje.esta_vivo())

# # Modificando valores de dos atributos
# Mi_personaje.nombre = "EstebanDido"
# Mi_personaje.fuerza = 300
# Mi_personaje.inteligencia = -2
# Mi_personaje.defensa = 30
# Mi_personaje.vida = 2

# print("El nombre de mi personaje es: ",Mi_personaje.nombre)
# print("La fuerza de mi personaje es: ",Mi_personaje.fuerza)
# print("La inteligencia de mi personaje es: ",Mi_personaje.inteligencia)
# print("La defensa de mi personaje es: ",Mi_personaje.defensa)
# print("La vida de mi personaje es: ",Mi_personaje.vida)