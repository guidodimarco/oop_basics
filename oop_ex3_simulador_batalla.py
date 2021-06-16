import random

class Guerrero:
    def __init__(self, nombre, vida, fuerza, defensa, precision, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.precision = precision
        self.velocidad = velocidad

    def __str__(self):
        return "Nombre: {nombre} / Vida: {vida} / Fuerza: {fuerza} / " \
               "Defensa: {defensa} / Precision: {precision} / Velocidad: {velocidad}"\
                .format(nombre=self.nombre, vida=self.vida, fuerza=self.fuerza,
                        defensa=self.defensa, precision=self.precision, velocidad=self.velocidad)

class Combate:
    def __init__(self, guerrero_a, guerrero_b):
        self.guerrero_a = guerrero_a
        self.guerrero_b = guerrero_b

    def iniciar_combate(self, guerrero_a, guerrero_b):
        # El guerrero con mayor velocidad tiene el 1er movimiento
        if guerrero_a.velocidad > guerrero_b.velocidad:
            print("{n} tiene mayor velocidad asi que va primero.".format(n=guerrero_a.nombre))
            combate1.turnos(guerrero_a, guerrero_b)
        else:
            print("{n} tiene mayor velocidad asi que va primero.".format(n=guerrero_b.nombre))
            combate1.turnos(guerrero_b, guerrero_a)

    def turnos(self, guerrero_a, guerrero_b):
        ronda = 0
        while not (guerrero_a.vida <= 0 or guerrero_b.vida <= 0):
            ronda += 1
            print("\nRonda {a}:".format(a=ronda))
            combate1.golpe(guerrero_a, guerrero_b)
            if not (guerrero_a.vida <= 0 or guerrero_b.vida <= 0):
                print()
                combate1.golpe(guerrero_b, guerrero_a)

        print()
        if guerrero_a.vida > 0:
            print("El ganador es {n}.".format(n=guerrero_a.nombre))
        if guerrero_b.vida > 0:
            print("El ganador es {n}.".format(n=guerrero_b.nombre))

    def golpe(self, guerrero_a, guerrero_b):
        # Probabilidad de acierto -> (guerreroA.precision - guerreroB.velocidad) / 100
        hit_probs = (guerrero_a.precision - guerrero_b.velocidad)
        miss_probs = 100 - hit_probs
        hitormiss = (random.choices(["HIT", "MISS"], weights=(hit_probs, miss_probs)))
        print("Chances de {n} de golpear({a}%) o errar({b}%)... {c}!"
              .format(n=guerrero_a.nombre, a=hit_probs, b=miss_probs, c=hitormiss[0]))

        if hitormiss == ['HIT']:
            # Daño del golpe -> max(guerrero_a.fuerza - guerrero_b.defensa + random.randrange(-10, 11), 1)
            print("Vida de {a}: {b}".format(a=guerrero_b.nombre, b=guerrero_b.vida))
            danio = max(guerrero_a.fuerza - guerrero_b.defensa + random.randrange(-10, 11), 1)
            guerrero_b.vida -= danio
            print("-{a} = {b}".format(a=danio, b=guerrero_b.vida))

# Crear instancias de Guerrero
guerrero1 = Guerrero("Rojo", 50, 90, 50, 90, 40)
guerrero2 = Guerrero("Azul", 80, 70, 70, 100, 20)

# Crear instancia de Combate
combate1 = Combate(guerrero1, guerrero2)
# Ejecutar metodo de instancia de Combate
combate1.iniciar_combate(guerrero1, guerrero2)
