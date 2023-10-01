import random

class Animal:
    def __init__(self, nombre, salud_max, hambre_max, felicidad_max):
        self.nombre = nombre
        self.salud = salud_max
        self.hambre = hambre_max
        self.felicidad = felicidad_max

    def alimentar(self):
        if self.hambre >= 10:
            self.hambre -= 10
        else:
            self.hambre = 0
        self.salud += 10


    def acariciar(self):
        self.felicidad += 10

    def limpieza_y_cuidados(self):
        self.salud += 10  

    def enfermar(self):
        self.salud -= 10

    def morir(self):
        return self.salud <= 0 or self.hambre >= 100 or self.felicidad <= 0

    def pasar_dia(self):
        self.hambre += 10
        self.salud -= 10
        self.felicidad -= 10

    def producir(self):
        pass

class Vaca(Animal):
    def __init__(self):
        super().__init__("Vaca", salud_max=100, hambre_max=50, felicidad_max=100)

    def producir(self):
        return random.randint(5, 10)

class Oveja(Animal):
    def __init__(self):
        super().__init__("Oveja", salud_max=80, hambre_max=40, felicidad_max=90)

    def producir(self):
        return random.randint(1, 5)

class Gallina(Animal):
    def __init__(self):
        super().__init__("Gallina", salud_max=60, hambre_max=30, felicidad_max=80)

    def producir(self):
        return random.randint(2, 4)

class Granja:
    def __init__(self):
        self.jugador = Jugador()

    def simular_dia(self):
        print("\nComienza un nuevo día en la granja!")
        self.jugador.cuidar_animales()
        for animal in self.jugador.animales:
            recursos = animal.producir()
            print(f"{animal.nombre} ha producido {recursos} recursos.")

        for animal in self.jugador.animales:
            animal.pasar_dia()
            if animal.morir():
                print(f"{animal.nombre} ha muerto. ¡Cuida bien a los demás!")
                self.jugador.animales.remove(animal)
            elif animal.felicidad <= 0:
                print(f"{animal.nombre} está deprimido. ¡Acarícialo para evitar que muera por depresión!")

        if not self.jugador.animales:
            print("¡Todos tus animales han muerto! Juego terminado.")
            exit()

class Jugador:
    def __init__(self):
        self.animales = [Vaca(), Oveja(), Gallina()]

    def mostrar_menu(self, animal):
        print(f"Acciones disponibles para {animal.nombre}:")
        print("1. Alimentar")
        print("2. Acariciar")
        print("3. Limpieza y Cuidados Médicos")
        print("4. Volver")
        eleccion = input("Elige una opción: ")
        return eleccion

    def cuidar_animales(self):
        while True:
            print("\nAnimales en la granja:")
            for idx, animal in enumerate(self.animales, start=1):
                print(f"{idx}. {animal.nombre} - Salud: {animal.salud}, Hambre: {animal.hambre}, Felicidad: {animal.felicidad}")

            opcion_animal = int(input("\nElige un animal para interactuar (1-3) o 0 para pasar al siguiente día: ")) - 1
            if opcion_animal == -1:
                return

            animal = self.animales[opcion_animal]
            eleccion = self.mostrar_menu(animal)

            if eleccion == "1":
                animal.alimentar()
            elif eleccion == "2":
                animal.acariciar()
            elif eleccion == "3":
                animal.limpieza_y_cuidados()
            elif eleccion == "4":
                continue
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

            animal.enfermar()
            if animal.morir():
                print(f"{animal.nombre} ha muerto. ¡Cuida bien a los demás!")
                self.animales.remove(animal)


if __name__ == "__main__":
    granja = Granja()

    while True:
        opcion = input("¿Quieres pasar al siguiente día? (s/n): ").lower()
        if opcion == 'n':
            print("Gracias por jugar. ¡Hasta luego!")
            break

        granja.simular_dia()
