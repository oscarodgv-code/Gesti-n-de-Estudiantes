# Clase que representa a un estudiante
class Estudiante:

    # Constructor
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    # Método para mostrar la información
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Matrícula:", self.matricula)

    # Método para actualizar la edad
    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad


# Programa principal

# Crear objetos
estudiante1 = Estudiante("oscar guajardo", 20, "A001")
estudiante2 = Estudiante("daniel guajardo", 22, "A002")

print("=== Información Inicial ===\n")

estudiante1.mostrar_informacion()

print()

estudiante2.mostrar_informacion()

print("\nActualizando la edad de oscar guajardo...\n")

estudiante1.actualizar_edad(21)

estudiante1.mostrar_informacion()