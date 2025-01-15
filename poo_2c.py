class Personaje:
    # Atributos de la clase
    #nombre = "Default"
    #fuerza = 0
    #inteligencia = 0
    #defensa = 0
    #vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida:", self.__vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print (self.__nombre, "ha muerto")

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar (self, enemigo):
        daño = self.dañar(enemigo)
        if daño < 0:
            daño = 0
        if enemigo.__vida - daño < 0:
            enemigo.__vida = 0
        else:
            enemigo.__vida = enemigo.__vida - daño
        print (self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        print ("Vida de", enemigo.__nombre, "es", enemigo.__vida)

    def get__vida(self):
        return self.__vida
    def set_vida(self, vida):
        self.__vida = vida
        if self.__vida <= 0:
            self.morir()

# Variable del constructor
mi_personaje = Personaje ("EstebanDido", 10, 50, 45, 100)
mi_enemigo = Personaje ("Angel", 70, 100, 7000, 100)
print(mi_personaje.get__vida())
# print(mi_personaje.set__vida())
print(mi_personaje.get__vida())
mi_personaje._Personaje__vida = -50
mi_personaje.imprimir_atributos()


#mi_personaje.vida
#mi_personaje.__vida
# mi_personaje.vida = 0
# mi_personaje.imprimir_atributos()

# mi_personaje.imprimir_atributos()
# mi_personaje.atacar (mi_enemigo)

#mi_personaje.morir()
# mi_personaje.imprimir_atributos()
# mi_personaje.subir_nivel(15,5,10)
# print ("Valores actualizados")
# mi_personaje.imprimir_atributos()
# print (mi_personaje.esta_vivo())

# # Modificando valores de dos atributos
# Mi_personaje.__nombre = "EstebanDido"
# Mi_personaje.__fuerza = 300
# Mi_personaje.__inteligencia = -2
# Mi_personaje.__defensa = 30
# Mi_personaje.__vida = 2

# print("El nombre de mi personaje es: ",Mi_personaje.__nombre)
# print("La fuerza de mi personaje es: ",Mi_personaje.__fuerza)
# print("La inteligencia de mi personaje es: ",Mi_personaje.__inteligencia)
# print("La defensa de mi personaje es: ",Mi_personaje.__defensa)
# print("La vida de mi personaje es: ",Mi_personaje.__vida)