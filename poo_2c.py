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
        return self.fuerza - enemigo.defensa
    
    def atacar (self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print (self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print ("Vida de", enemigo.nombre, "es", enemigo.vida)

# Variable del constructor
mi_personaje = Personaje ("EstebanDido", 100, 50, 45, 100)
mi_enemigo = Personaje ("Angel", 70, 100, 40, 100)
mi_personaje.imprimir_atributos()
mi_personaje.atacar (mi_enemigo)

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