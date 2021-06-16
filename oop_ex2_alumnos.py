class Alumno:
    def __init__(self, num_legajo, nombre, notas=[]):
        self.num_legajo = num_legajo
        self.nombre = nombre
        self.notas = notas

    def __str__(self):
        return "Nro de legajo: {num_legajo} / Nombre: {nombre} / Notas: {notas}"\
            .format(num_legajo=self.num_legajo, nombre=self.nombre, notas=self.notas)

    def agregar_nota(self, nota):
        if isinstance(nota, int):
            self.notas.append(nota)
        else:
            print("Argumento ingresado no es de tipo numerico")

    def agregar_muchas_notas(self, array_notas):
        for x in array_notas:
            self.notas.append(x)

    def sacar_promedio(self, notas):
        contador = 0
        suma = 0
        for x in notas:
            suma += x
            contador += 1
        promedio = suma / contador
        print ("Promedio:", promedio, "=", suma, "/", contador)

###

if __name__ == '__main__':

    # Creamos instancias de Nota
    alumno1 = Alumno(1, "Juan", [])
    alumno2 = Alumno(2, "Diego", [])

    # Creamos arrays de notas
    notas1 = [7,4]
    notas2 = [10,9,8,8]

    # Usamos los métodos agregar_nota y agregar_muchas_notas
    alumno1.agregar_muchas_notas(notas1)
    alumno2.agregar_muchas_notas(notas2)
    alumno1.agregar_nota(10)
    alumno2.agregar_nota(4)

    print("Alumnos:")
    # Imprimimos las instancias de Alumno
    print(alumno1)
    print(alumno2)

    print("\n")
    print("Promedios:")
    # Usamos el método sacar_promedio
    alumno1.sacar_promedio(alumno1.notas)
    alumno2.sacar_promedio(alumno2.notas)
