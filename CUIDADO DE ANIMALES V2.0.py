import random

class Animal:
    def __init__(self, nombre, salud_max, hambre_max, felicidad_max):
        self.nombre = nombre
        self.salud = salud_max
        self.hambre = hambre_max
        self.felicidad = felicidad_max
        self.total_recursos_producidos = 0
        self.nombre_usuario = None 

    def alimentar(self):
        self.hambre -= 10
        if self.hambre < 0:
            self.hambre = 0
        if self.salud < 90:
            self.salud += 10

    def acariciar(self):
        self.felicidad += 10
        if self.felicidad > 100:
            self.felicidad = 100

        if self.salud < 100:
            self.salud += 10

    def limpieza_y_cuidados(self):
        self.salud += 10
        if self.salud > 100:
            self.salud = 100

    def enfermar(self):
        if self.salud < 50:
            self.salud -= 20
        else:
            self.salud -= 10

    def morir(self):
        return self.salud <= 0 or self.hambre >= 100 or self.felicidad <= 0

    def pasar_dia(self):
        self.hambre += 10
        if self.salud < 50:
            print(f"{self.nombre} está enferm@.")
            self.enfermar()
        else:
            self.salud -= 10
            self.felicidad -= 10

        if self.morir():
            self.salud = 0

    def comprar_animal(self, numero):
        if self.nombre_usuario is None:
            nombre_usuario = input(f"Ingrese un nombre para {self.nombre} #{numero}: ")
            self.nombre_usuario = nombre_usuario
        self.nombre = f"{self.nombre} #{numero}"

    def producir(self):
        recursos = random.randint(1, 10)
        self.total_recursos_producidos += recursos  
        return recursos
    

class Vaca(Animal):
    def __init__(self, numero):
        super().__init__("Vaca", salud_max=100, hambre_max=50, felicidad_max=100)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(6, 10)

class Oveja(Animal):
    def __init__(self, numero):
        super().__init__("Oveja", salud_max=80, hambre_max=40, felicidad_max=90)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(3, 7)

class Gallina(Animal):
    def __init__(self, numero):
        super().__init__("Gallina", salud_max=60, hambre_max=30, felicidad_max=80)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(1, 5)

class Granja:
    def __init__(self):
        self.jugador = Jugador()
        self.dinero = 0
        self.creditos = 0
        self.total_recursos_producidos = 0 

    def simular_dia(self):
        print("\nComienza un nuevo día en la granja!")
        self.jugador.cuidar_animales(self)
        for animal in self.jugador.animales:
            recursos = animal.producir()
            animal.total_recursos_producidos += recursos  
            print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha producido {recursos} recursos.")

        for animal in self.jugador.animales:
            animal.pasar_dia()
            if animal.morir():
                print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha muerto - ¡Cuida bien a los demás! >:( ")
                self.jugador.animales.remove(animal)
            elif animal.felicidad <= 0:
                print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) está deprimido - ¡Acarícialo para evitar que muera por depresión!")

        if not self.jugador.animales:
            print('--------------------------------------------------')
            print("¡Todos tus animales han muerto! - Fin del juego :(")
            print('--------------------------------------------------')
            exit()

    def tienda(self):
        while True:
            print('-----------------------------------------------')
            print("- Bienvenido a la tienda - ¿Qué deseas hacer? -")
            print('-----------------------------------------------')
            print("1. Mostrar recursos producidos por cada animal")
            print("2. Vender recursos")
            print("3. Mostrar cantidad de créditos")
            print("4. Comprar animales")
            print("5. Vender animales")
            print("6. Volver a la granja")

            opcion_tienda = input("Elige una opción: ")

            if opcion_tienda == "1":
                self.mostrar_recursos_producidos()
            elif opcion_tienda == "2":
                self.vender_recursos()
            elif opcion_tienda == "3":
                self.mostrar_dinero_y_creditos()
            elif opcion_tienda == "4":
                self.comprar_animales()
            elif opcion_tienda == "5":
                self.vender_animales()
            elif opcion_tienda == "6":
                return
            else:
                print("Opción no válida, elige una opción válida.")

    def mostrar_recursos_producidos(self):
        print("\n--- Recursos producidos por cada animal ---")
        for animal in self.jugador.animales:
            print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha producido {animal.total_recursos_producidos} recursos")
        print(f"Total de recursos producidos: {sum(animal.total_recursos_producidos for animal in self.jugador.animales)}")

    def vender_recursos(self):
        total_venta = 0
        for animal in self.jugador.animales:
            recursos = animal.total_recursos_producidos 
            if isinstance(animal, Vaca):
                precio_por_recurso = 30
            elif isinstance(animal, Oveja):
                precio_por_recurso = 20
            elif isinstance(animal, Gallina):
                precio_por_recurso = 10
            else:
                precio_por_recurso = 0

            venta_animal = recursos * precio_por_recurso
            total_venta += venta_animal

            print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha vendido {recursos} recursos por {venta_animal} créditos.")

        self.dinero += total_venta
        self.creditos += total_venta

    def mostrar_dinero_y_creditos(self):
        print(f"Créditos disponibles para comprar animales: {self.creditos} créditos")

    def comprar_animales(self):
        print('-------------------------------------')
        print("- Animales disponibles para comprar -")
        print('-------------------------------------')
        print("1. Vaca - 1800 créditos")
        print("2. Oveja - 1500 créditos")
        print("3. Gallina - 1200 créditos")
        opcion_compra = input("Elige un animal para comprar (1-3) o 0 para salir: ")

        if opcion_compra == "1" and self.creditos >= 1800:
            self.jugador.animales.append(Vaca(len(self.jugador.animales) + 1))
            self.creditos -= 1800
            print("¡Felicidades, has comprado una vaca!")
        elif opcion_compra == "2" and self.creditos >= 1500:
            self.jugador.animales.append(Oveja(len(self.jugador.animales) + 1))
            self.creditos -= 1500
            print("¡Felicidades, has comprado una oveja!")
        elif opcion_compra == "3" and self.creditos >= 1200:
            self.jugador.animales.append(Gallina(len(self.jugador.animales) + 1))
            self.creditos -= 1200
            print("¡Felicidades, has comprado una gallina!")
        elif opcion_compra != "0":
            print("No tienes suficientes créditos para comprar este animal :(")


    def vender_animales(self):
        print("\nAnimales disponibles para vender:")
        for idx, animal in enumerate(self.jugador.animales, start=1):
            print(f"{idx}. {animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'})")

        while True:
            try:
                opcion_vender = int(input("Elige el número del animal que quieres vender (1-3) o 0 para cancelar: "))
                if opcion_vender == 0:
                    return
                elif 1 <= opcion_vender <= len(self.jugador.animales):
                    animal_vendido = self.jugador.animales[opcion_vender - 1]
                    if isinstance(animal_vendido, Vaca):
                        precio_venta = 1400
                    elif isinstance(animal_vendido, Oveja):
                        precio_venta = 1100
                    elif isinstance(animal_vendido, Gallina):
                        precio_venta = 800
                    else:
                        precio_venta = 0

                    venta_animal = precio_venta
                    print(f"Has vendido {animal_vendido.nombre} por {venta_animal} créditos.")
                    self.jugador.animales.remove(animal_vendido)
                    self.creditos += venta_animal
                    return
                else:
                    print("Número de animal no válido, inténtalo de nuevo.")
            except ValueError:
                print("Por favor, introduce un número válido.")          

class Jugador:
    def __init__(self):
        self.animales = [Vaca(1), Oveja(1), Gallina(1)]

    def mostrar_menu(self, animal):
        print(f"Acciones disponibles para {animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}):")
        print("1. Alimentar")
        print("2. Acariciar")
        print("3. Limpieza y Cuidados Médicos")
        print("4. Volver")
        print("5. Ir a la tienda")
        eleccion = input("Elige una opción: ")
        return eleccion

    def cuidar_animales(self, granja):
        while True:
            print("\nAnimales en la granja:")
            for idx, animal in enumerate(self.animales, start=1):
                print(f"{idx}. {animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) - Salud: {animal.salud}, Hambre: {animal.hambre}, Felicidad: {animal.felicidad}")

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
                animal.salud += 10
                print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha recibido cuidados médicos y su salud ha aumentado en 10 puntos.")
            elif eleccion == "4":
                continue
            elif eleccion == "5":
                granja.tienda()
            else:
                print("Opción no válida, elige una opción válida.")

            animal.enfermar()
            if animal.morir():
                print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha muerto - ¡Cuida bien a los demás! >:(")
                self.animales.remove(animal)

if __name__ == "__main__":
    print('----------------------------------------------------')
    print("------------- ¡Bienvenido a la Granja! -------------")
    print('----------------------------------------------------')
    opcion_inicio = input("¿Quieres empezar en la granja? (s/n): ").lower()

    if opcion_inicio == 's':
        granja = Granja()

        while True:
            opcion = input("¿Quieres pasar al siguiente día? (s/n para cerrar el programa): ").lower()
            if opcion != 's':
                print('-----------------------------------------------------')
                print("- Gracias por jugar - ¡Ojalá te hayas divertido! :D -")
                print('-----------------------------------------------------')
                granja.mostrar_dinero_y_creditos()
                break

            if granja.jugador.animales[0].nombre_usuario is None:
                for animal in granja.jugador.animales:
                    nombre_usuario = input(f"Ingrese un nombre para {animal.nombre}: ")
                    animal.nombre_usuario = nombre_usuario

            granja.simular_dia()
    else:
        print('-----------------------------------------------------')
        print("- Gracias por jugar - ¡Ojalá te hayas divertido! :D -")
        print('-----------------------------------------------------')
