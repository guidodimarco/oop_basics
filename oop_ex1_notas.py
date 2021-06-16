class Nota:
    def __init__(self, titulo, activa, id_nota=0):
        self.id_nota = id_nota
        self.titulo = titulo
        self.activa = activa

    def __str__(self):
        return "Id: {a} / Titulo: {b} / Activa: {c}"\
            .format(a=self.id_nota, b=self.titulo, c=self.activa)

class ListadoNotas:
    def __init__(self):
        self.listado = []

    def agregar_nota(self, nota):
        self.listado.append(nota)

    def editar_nota(self, id_nota, nota):
        contador = 0
        for x in self.listado:
            if id_nota == x.id_nota:
                self.listado[contador].titulo = nota.titulo
            contador += 1

    def borrar_nota(self, id_nota):
        contador = 0
        for x in self.listado:
            if id_nota == x.id_nota:
                self.listado[contador].activa = False #Instancia de nota contenida dentro del array de self.listado
            contador += 1

    def get_notas(self):
        contador = 0
        for x in self.listado:
            if self.listado[contador].activa is True:
                print(x)
            contador += 1

###

if __name__ == '__main__':
    # Creamos instancia de ListadoNotas
    listadoNotas = ListadoNotas()

    # Creamos instancias de Nota
    nota1 = Nota("Ingredientes", True, 1)
    nota2 = Nota("Peliculas favoritas", True, 2)

    # Usamos el método de instancia de Nota
    listadoNotas.agregar_nota(nota1)
    listadoNotas.agregar_nota(nota2)

    print()
    # Imprimimos el atributo listado del objeto listadoNotas
    print("listadoNotas.get_notas() ->")
    listadoNotas.get_notas()

    print()
    print("listadoNotas.get_notas() despues de editar nota 2 ->")
    nota_editada_1 = Nota("Peliculas para ver", True, 2)
    listadoNotas.editar_nota(2, nota_editada_1)
    listadoNotas.get_notas()

    print()
    print("listadoNotas.get_notas() despues de borrar nota 1 ->")
    listadoNotas.borrar_nota(1)
    listadoNotas.get_notas()
