class Personaje:
    # Atributos de la clase
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

# Variable del constructor
Mi_personaje = Personaje()
# Modificando valores de dos atributos
Mi_personaje.nombre = "EstebanDido"
Mi_personaje.fuerza = 300
Mi_personaje.inteligencia = -2
Mi_personaje.defensa = 30
Mi_personaje.vida = 2

print("El nombre de mi personaje es: ",Mi_personaje.nombre)
print("La fuerza de mi personaje es: ",Mi_personaje.fuerza)
print("La inteligencia de mi personaje es: ",Mi_personaje.inteligencia)
print("La defensa de mi personaje es: ",Mi_personaje.defensa)
print("La vida de mi personaje es: ",Mi_personaje.vida)