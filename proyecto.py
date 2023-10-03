import time #Libreria para agregar delay a las respuestas
import random #Libreria para generar numeros aleatorios
bandera = 0 #Variable de unico valor para tronar el programa en cualquier momento
class cultivos:
    def __init__(self,siembra,regar,cantidad, dinero):
        self.siembra = siembra #Cantidad de semillas que se utilizaran
        self.regar = regar #Regar los cultivos
        self.cantidad = cantidad #Semillas que se tienen en el inventario
        self.dinero = dinero #Cantidad de dinero obtenido por plantar

class trigo(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos.__init__(self, siembra, regar, cantidad, dinero)
        self.tiempo = tiempo #Tiempo para cosechar los cultivos

    def plantarTrigo(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5 #Se le regalan 25 semillas y cada plantacion cuesta 5, por lo tanto lo dividimos por 5 para encontrar cuantas plantaciones seran
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5 #La cantidad de plantaciones las multiplicamos por el valor de cada plantacion (5) y asi obtenemos las semillas gastadas
            restante = self.cantidad - gastado
            print(f'Haz utilizado {gastado} semillas y te quedan {restante}')
            self.dinero = self.dinero+15
            print(f'Has obtenido: {self.dinero} creditos!')
            print(f'Tus creditos actuales son: {self.dinero}')

    def crecimientoTrigo(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        self.tiempo = 60
        print("Tus cultivos estaran listos en:")
        while self.tiempo > 0:
            minutos = self.tiempo // 60
            segundos = self.tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            self.tiempo -= 1
        self.dinero = self.dinero+(self.siembra*5)
        print('Tus cultivos se cosecharon exitosamente!')
        print(f'Has obtenido: {self.dinero} creditos!')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def regarTrigo(self):
        self.tiempo = 30
        while self.tiempo > 0:
            time.sleep(1)
            self.tiempo-=1
            print(f'Quedan {self.tiempo} segundos para terminar de regar tus cultivos!', end='\r')
        self.dinero = self.dinero+5
        print(f'Felicitaciones has obtenido: {self.dinero}')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def dar25_semillas(self):
        if self.dinero >= 30:
            self.cantidad = self.cantidad + 25
            self.dinero = self.dinero - 30
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar50_semillas(self):
        if self.dinero >= 60:
            self.cantidad = self.cantidad + 50
            self.dinero = self.dinero - 60
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar75_semillas(self):
        if self.dinero >= 90:
            self.cantidad = self.cantidad + 75
            self.dinero = self.dinero - 90
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
    def dar100_semillas(self):
        if self.dinero >= 120:
            self.cantidad = self.cantidad + 100
            self.dinero = self.dinero - 120
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")

class tomate(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos.__init__(self, siembra, regar, cantidad, dinero)
        self.tiempo = tiempo
    
    def plantarTomate(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5
            restante = self.cantidad - gastado
            print(f'Haz utilizado {gastado} semillas y te quedan {restante}')
            self.dinero = self.dinero+10
            print(f'Has obtenido: {self.dinero} creditos!')
            print(f'Tus creditos actuales son: {self.dinero}')

    def crecimientoTomate(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        self.tiempo = 45
        print("Tus cultivos estaran listos en:")
        while self.tiempo > 0:
            minutos = self.tiempo // 60
            segundos = self.tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            self.tiempo -= 1
        self.dinero = self.dinero+(self.siembra*5)
        print('Tus cultivos se cosecharon exitosamente!')
        print(f'Has obtenido: {self.dinero} creditos!')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def regarTomate(self):
        self.tiempo = 25
        while self.tiempo > 0:
            time.sleep(1)
            self.tiempo-=1
            print(f'Quedan {self.tiempo} segundos para terminar de regar tus cultivos!', end='\r')
        self.dinero = self.dinero+5
        print(f'Felicitaciones has obtenido: {self.dinero}')
        print(f'Tus creditos actuales son: {self.dinero}')

    def dar25_semillas(self):
        if self.dinero >= 30:
            self.cantidad = self.cantidad + 25
            self.dinero = self.dinero - 30
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar50_semillas(self):
        if self.dinero >= 60:
            self.cantidad = self.cantidad + 50
            self.dinero = self.dinero - 60
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar75_semillas(self):
        if self.dinero >= 90:
            self.cantidad = self.cantidad + 75
            self.dinero = self.dinero - 90
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
    def dar100_semillas(self):
        if self.dinero >= 120:
            self.cantidad = self.cantidad + 100
            self.dinero = self.dinero - 120
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")

class cebolla(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos.__init__(self, siembra, regar, cantidad, dinero)
        self.tiempo = tiempo

    def plantarCebolla(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5
            restante = self.cantidad - gastado
            print(f'Haz utilizado {gastado} semillas y te quedan {restante}')
            self.dinero = self.dinero+8
            print(f'Has obtenido: {self.dinero} creditos!')
            print(f'Tus creditos actuales son: {self.dinero}')

    def crecimientoCebolla(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        self.tiempo = 50
        print("Tus cultivos estaran listos en:")
        while self.tiempo > 0:
            minutos = self.tiempo // 60
            segundos = self.tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            self.tiempo -= 1
        self.dinero = self.dinero+(self.siembra*5)
        print('Tus cultivos se cosecharon exitosamente!')
        print(f'Has obtenido: {self.dinero} creditos!')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def regarCebolla(self):
        self.tiempo = 35
        while self.tiempo > 0:
            time.sleep(1)
            self.tiempo-=1
            print(f'Quedan {self.tiempo} segundos para terminar de regar tus cultivos!', end='\r')
        self.dinero = self.dinero+5
        print(f'Felicitaciones has obtenido: {self.dinero}')
        print(f'Tus creditos actuales son: {self.dinero}')   
    
    def dar25_semillas(self):
        if self.dinero >= 30:
            self.cantidad = self.cantidad + 25
            self.dinero = self.dinero - 30
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar50_semillas(self):
        if self.dinero >= 60:
            self.cantidad = self.cantidad + 50
            self.dinero = self.dinero - 60
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar75_semillas(self):
        if self.dinero >= 90:
            self.cantidad = self.cantidad + 75
            self.dinero = self.dinero - 90
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
    def dar100_semillas(self):
        if self.dinero >= 120:
            self.cantidad = self.cantidad + 100
            self.dinero = self.dinero - 120
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")

class zanahoria(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        super().__init__(siembra, regar, cantidad, dinero) 
        self.tiempo = tiempo
    
    def plantarZanahoria(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5
            restante = self.cantidad - gastado
            print(f'Haz utilizado {gastado} semillas y te quedan {restante}')
            self.dinero = self.dinero+3
            print(f'Has obtenido: {self.dinero} creditos!')
            print(f'Tus creditos actuales son: {self.dinero}')

    def crecimientoZanahoria(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        self.tiempo = 35
        print("Tus cultivos estaran listos en:")
        while self.tiempo > 0:
            minutos = self.tiempo // 60
            segundos = self.tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            self.tiempo -= 1
        self.dinero = self.dinero+(self.siembra*5)
        print('Tus cultivos se cosecharon exitosamente!')
        print(f'Has obtenido: {self.dinero} creditos!')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def regarZanahoria(self):
        self.tiempo = 15
        while self.tiempo > 0:
            time.sleep(1)
            self.tiempo-=1
            print(f'Quedan {self.tiempo} segundos para terminar de regar tus cultivos!', end='\r')
        self.dinero = self.dinero+5
        print(f'Felicitaciones has obtenido: {self.dinero}')
        print(f'Tus creditos actuales son: {self.dinero}')

    def dar25_semillas(self):
        if self.dinero >= 30:
            self.cantidad = self.cantidad + 25
            self.dinero = self.dinero - 30
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar50_semillas(self):
        if self.dinero >= 60:
            self.cantidad = self.cantidad + 50
            self.dinero = self.dinero - 60
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar75_semillas(self):
        if self.dinero >= 90:
            self.cantidad = self.cantidad + 75
            self.dinero = self.dinero - 90
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
    def dar100_semillas(self):
        if self.dinero >= 120:
            self.cantidad = self.cantidad + 100
            self.dinero = self.dinero - 120
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
class maiz(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        super().__init__(siembra, regar, cantidad, dinero)
        self.tiempo = tiempo
    
    def plantarMaiz(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5
            restante = self.cantidad - gastado
            print(f'Haz utilizado {gastado} semillas y te quedan {restante}')
            self.dinero = self.dinero+6
            print(f'Has obtenido: {self.dinero} creditos!')
            print(f'Tus creditos actuales son: {self.dinero}')

    def crecimientoMaiz(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        self.tiempo = 20
        print("Tus cultivos estaran listos en:")
        while self.tiempo > 0:
            minutos = self.tiempo // 60
            segundos = self.tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            self.tiempo -= 1
        self.dinero = self.dinero+(self.siembra*5)
        print('Tus cultivos se cosecharon exitosamente!')
        print(f'Has obtenido: {self.dinero} creditos!')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def regarMaiz(self):
        self.tiempo = 10
        while self.tiempo > 0:
            time.sleep(1)
            self.tiempo-=1
            print(f'Quedan {self.tiempo} segundos para terminar de regar tus cultivos!', end='\r')
        self.dinero = self.dinero+5
        print(f'Felicitaciones has obtenido: {self.dinero}')
        print(f'Tus creditos actuales son: {self.dinero}')

    def dar25_semillas(self):
        if self.dinero >= 30:
            self.cantidad = self.cantidad + 25
            self.dinero = self.dinero - 30
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar50_semillas(self):
        if self.dinero >= 60:
            self.cantidad = self.cantidad + 50
            self.dinero = self.dinero - 60
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar75_semillas(self):
        if self.dinero >= 90:
            self.cantidad = self.cantidad + 75
            self.dinero = self.dinero - 90
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
    def dar100_semillas(self):
        if self.dinero >= 120:
            self.cantidad = self.cantidad + 100
            self.dinero = self.dinero - 120
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")

class puerro(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        super().__init__(siembra, regar, cantidad, dinero)
        self.tiempo = tiempo
    
    def plantarPuerro(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5
            restante = self.cantidad - gastado
            print(f'Haz utilizado {gastado} semillas y te quedan {restante}')
            self.dinero = self.dinero+1
            print(f'Has obtenido: {self.dinero} creditos!')
            print(f'Tus creditos actuales son: {self.dinero}')

    def crecimientoPuerro(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        self.tiempo = 15
        print("Tus cultivos estaran listos en:")
        while self.tiempo > 0:
            minutos = self.tiempo // 60
            segundos = self.tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            self.tiempo -= 1
        self.dinero = self.dinero+(self.siembra*5)
        print('Tus cultivos se cosecharon exitosamente!')
        print(f'Has obtenido: {self.dinero} creditos!')
        print(f'Tus creditos actuales son: {self.dinero}')
    
    def regarPuerro(self):
        self.tiempo = 5
        while self.tiempo > 0:
            time.sleep(1)
            self.tiempo-=1
            print(f'Quedan {self.tiempo} segundos para terminar de regar tus cultivos!', end='\r')
        self.dinero = self.dinero+1
        print(f'Felicitaciones has obtenido: {self.dinero}')
        print(f'Tus creditos actuales son: {self.dinero}')

    def dar25_semillas(self):
        if self.dinero >= 30:
            self.cantidad = self.cantidad + 25
            self.dinero = self.dinero - 30
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar50_semillas(self):
        if self.dinero >= 60:
            self.cantidad = self.cantidad + 50
            self.dinero = self.dinero - 60
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes!")

    def dar75_semillas(self):
        if self.dinero >= 90:
            self.cantidad = self.cantidad + 75
            self.dinero = self.dinero - 90
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")
    
    def dar100_semillas(self):
        if self.dinero >= 120:
            self.cantidad = self.cantidad + 100
            self.dinero = self.dinero - 120
            print(f'Tienes {self.cantidad} semillas y {self.dinero} creditos')
        else:
            print("Creditos insuficientes")

import random

class Animal:
    def __init__(self, nombre, salud_max, hambre_max, felicidad_max):
        self.nombre = nombre #Variable para el nombre del animal
        self.salud = salud_max #Variable para la salud del animal
        self.hambre = hambre_max #Variable para el hambre del animal
        self.felicidad = felicidad_max #Variable para la felicidad del animal
        self.total_recursos_producidos = 0 #La cantidad de recursos producidos por los animales
        self.nombre_usuario = None #Variable que guarda el nombre del usuario

    def alimentar(self): #Al alimentar al animal, se incrementa la salud de este
        self.hambre -= 10
        if self.hambre < 0:
            self.hambre = 0
        if self.salud < 90:
            self.salud += 10

    def acariciar(self): #Si se acaricia aumenta su felicidad
        self.felicidad += 10
        if self.felicidad > 100:
            self.felicidad = 100

        if self.salud < 100:
            self.salud += 10

    def limpieza_y_cuidados(self): #Si se le da limpieza y cuidados mejora la salud del animal
        self.salud += 10
        if self.salud > 100:
            self.salud = 100

    def enfermar(self): #Si el animal se enferma, su salud disminuye el valor
        if self.salud < 50:
            self.salud -= 20
        else:
            self.salud -= 10

    def morir(self): #El animal muere cuando no tenga felicidad, salud y mucha hambre
        return self.salud <= 0 or self.hambre >= 100 or self.felicidad <= 0

    def pasar_dia(self): #Cada que pasan los dias la salud se mejora en 10, si esta salud es menor a 50 esta enfermo
        self.hambre += 10
        if self.salud < 50:
            print(f"{self.nombre} está enferm@.")
            self.enfermar()
        else:
            self.salud -= 10
            self.felicidad -= 10

        if self.morir():
            self.salud = 0

    def comprar_animal(self, numero): #Para comprar un animal primero se verifica que este tenga un nombre, sino lo soliticamos
        if self.nombre_usuario is None:
            nombre_usuario = input(f"Ingrese un nombre para {self.nombre} #{numero}: ")
            self.nombre_usuario = nombre_usuario
        self.nombre = f"{self.nombre} #{numero}"

    def producir(self): #Los recursos producidos son aleatorios utilizando la libreria random
        recursos = random.randint(1, 10)
        self.total_recursos_producidos += recursos  
        return recursos
    

class Vaca(Animal): #El primer animal que hereda de la clase Animal es la vaca, otorgandole un valor a la salud, hambre y felicidad
    def __init__(self, numero):
        super().__init__("Vaca", salud_max=100, hambre_max=50, felicidad_max=100)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(6, 10)

class Oveja(Animal): #EL segunddo animal que hereda de la clase Animal es la Oveja, otorgandole valores distintos y un poco mas bajos que la vaca
    def __init__(self, numero):
        super().__init__("Oveja", salud_max=80, hambre_max=40, felicidad_max=90)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(3, 7)

class Gallina(Animal): #Y el ultimo animal que hereda de la clase Animal es la Gallina, este tiene los valores mas bajos
    def __init__(self, numero):
        super().__init__("Gallina", salud_max=60, hambre_max=30, felicidad_max=80)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(1, 5)

class Granja: #Luego se crea la clase principal granda creando 4 variables
    def __init__(self):
        self.jugador = Jugador() #La variable jugador obtiene todos los valores de la clase Jugador
        self.dinero = 0 #El dinero obtenido por cuidar a los animales
        self.creditos = 0 #Los creditos para poder utilizarlos en la tienda
        self.total_recursos_producidos = 0  #El total de recursos producidos y recolectados

    def simular_dia(self): #Este es el inicio del juego, simulando un dia en la granja con los animales
        print("\nComienza un nuevo día en la granja!")
        self.jugador.cuidar_animales(self)
        for animal in self.jugador.animales:
            recursos = animal.producir()
            animal.total_recursos_producidos += recursos  #Aleatoriamente se genera un mensaje en el que nos dice que uno de nuestro animales ha generado recursos
            print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha producido {recursos} recursos.")

        for animal in self.jugador.animales:
            animal.pasar_dia()
            if animal.morir(): #En caso de que un animal haya muerto se le muestra una advertencia que el animal murio junto con la razon por la cual murio
                print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha muerto - ¡Cuida bien a los demás! >:( ")
                self.jugador.animales.remove(animal)
            elif animal.felicidad <= 0:
                print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) está deprimido - ¡Acarícialo para evitar que muera por depresión!")

        if not self.jugador.animales: #El juego termina cuando los animales del usuario mueren por falta de comida, salud o felicidad
            print('--------------------------------------------------')
            print("¡Todos tus animales han muerto! - Fin del juego :(")
            print('--------------------------------------------------')
            exit()

    def tienda(self):
        while True: #La tienda ofrece variedad de cosas para hacer con nuestros creditos, o mostrar el avance que llevamos en el juego
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

    def mostrar_recursos_producidos(self): #Metodo para mostrar la cantidad de recursos producidos y el nombre de este animal
        print("\n--- Recursos producidos por cada animal ---")
        for animal in self.jugador.animales:
            print(f"{animal.nombre} ({animal.nombre_usuario if animal.nombre_usuario else 'Sin nombre'}) ha producido {animal.total_recursos_producidos} recursos")
        print(f"Total de recursos producidos: {sum(animal.total_recursos_producidos for animal in self.jugador.animales)}")

    def vender_recursos(self): #Se pueden vender los recursos que los animales producen para obtener mas creditos en el juego, ejemplo: Leche, lana y huevos
        total_venta = 0
        for animal in self.jugador.animales:
            recursos = animal.total_recursos_producidos 
            if isinstance(animal, Vaca): #El metodo isinstance verifica que el objeto "animal" sea de tipo "Vaca" obteniendo como valor "True" y poder hacer la venta de los recursos
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

    def comprar_animales(self): #Ofrecemos la opcion de poder comprar mas animales y asi expandir nuestra granja y generar mas recursos
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


    def vender_animales(self): #Al igual que podemos vender nuestros animales para obtener mas creditos y especificarnos en otros animales
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
    def __init__(self): #A la variable animales le asignamos los 3 animales que le damos al usuario
        self.animales = [Vaca(1), Oveja(1), Gallina(1)]

    def mostrar_menu(self, animal): #En el menu se muestra el nombre del animal mas ciertas acciones que se pueden realizar con este
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
            for idx, animal in enumerate(self.animales, start=1): #Aqui realizamos un listado de los animales que tenemos en nuestra granja seguido de todos sus atributos
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

trigo1 = trigo(0, 0, 25, 0, 0)
tomate1 = tomate(0, 0, 25, 0, 0)
cebolla1 = cebolla(0, 0, 25, 0, 0)
zanahoria1 = zanahoria(0, 0, 25, 0, 0)
maiz1 = maiz(0, 0, 25, 0, 0)
puerro1 = puerro(0, 0, 25, 0, 0)
while bandera == 0:
    print("1. Cultivar")
    print("2. Cuidar animales")
    print("3. Salir")
    opcion = input("¿Que desea hacer?")
    match opcion: 
        case '1':
            while True:
                print("¿Que desea cultivar?")
                print("1. Trigo")
                print("2. Tomate")
                print("3. Cebolla")
                print("4. Zanahoria")
                print("5. Maiz")
                print("6. Puerro")
                print("7. Tienda")
                print("8. Salir")
                opcion = input("Opcion: ")
                match opcion:
                    case '1':
                            while True:
                                print("1. Plantar")
                                print("2. Cosechar")
                                print("3. Regar")
                                print("4. Regresar al menu de cultivos")
                                opcion = input("¿Que desea hacer?")
                                match opcion:
                                    case '1':
                                        trigo1.plantarTrigo()
                                    case '2':
                                        trigo1.crecimientoTrigo()
                                    case '3':
                                        trigo1.regarTrigo()
                                    case '4':
                                        print("Regresando al menu de cultivos...")
                                        time.sleep(2)
                                        break
                                    case _:
                                        print("No ingreso una opcion valida!")
                    case '2':
                        while True:
                            print("1. Plantar")
                            print("2. Cosechar")
                            print("3. Regar")
                            print("4. Regresar al menu de cultivos")
                            opcion = input("¿Que desea hacer?")
                            match opcion:
                                case '1':
                                    tomate1.plantarTomate()
                                case '2':
                                    tomate1.crecimientoTomate()
                                case '3':
                                    tomate1.regarTomate()
                                case '4':
                                    print("Regresando al menu de cultivos...")
                                    time.sleep(2)
                                    break
                                case _:
                                    print("No ingreso una opcion valida")
                    case '3':
                        while True:
                            print("1. Plantar")
                            print("2. Cosechar")
                            print("3. Regar")
                            print("4. Regresar al menu de cultivos")
                            opcion = input("¿Que desea hacer?")
                            match opcion:
                                case '1':
                                    cebolla1.plantarCebolla()
                                case '2':
                                    cebolla1.crecimientoCebolla()
                                case '3':
                                    cebolla1.regarCebolla()
                                case '4':
                                    print("Regresando al menu de cultivos...")
                                    time.sleep(2)
                                    break
                                case _:
                                    print("No ingreso una opcion valida")
                    case '4':
                        while True:
                            print("1. Plantar")
                            print("2. Cosechar")
                            print("3. Regar")
                            print("4. Regresar al menu de cultivos")
                            opcion = input("¿Que desea hacer?")
                            match opcion:
                                case '1':
                                    zanahoria1.plantarZanahoria()
                                case '2':
                                    zanahoria1.crecimientoZanahoria()
                                case '3':
                                    zanahoria1.regarZanahoria()
                                case '4':
                                    print("Regresando al menu de cultivos...")
                                    time.sleep(2)
                                    break
                                case _:
                                    print("No ingreso una opcion valida")
                    case '5':
                        while True:
                            print("1. Plantar")
                            print("2. Cosechar")
                            print("3. Regar")
                            print("4. Regresar al menu de cultivos")
                            opcion = input("¿Que desea hacer?")
                            match opcion:
                                case '1':
                                    maiz1.plantarMaiz()
                                case '2':
                                    maiz1.crecimientoMaiz()
                                case '3':
                                    maiz1.regarMaiz()
                                case '4':
                                    print("Regresando al menu de cultivos...")
                                    time.sleep(2)
                                    break
                                case _:
                                    print("No ingreso una opcion valida")
                    case '6':
                        while True:
                            print("1. Plantar")
                            print("2. Cosechar")
                            print("3. Regar")
                            print("4. Regresar al menu de cultivos")
                            opcion = input("¿Que desea hacer?")
                            match opcion:
                                case '1':
                                    puerro1.plantarPuerro()
                                case '2':
                                    puerro1.crecimientoPuerro()
                                case '3':
                                    puerro1.regarPuerro()
                                case '4':
                                    print("Regresando al menu de cultivos...")
                                    time.sleep(2)
                                    break
                                case _:
                                    print("No ingreso una opcion valida")
                    case '7':
                        while True:
                            print("BIENVENIDO A LA TIENDA DE CULTIVOS")
                            print("1. Trigo")
                            print("2. Tomate")
                            print("3. Cebolla")
                            print("4. Zanahoria")
                            print("5. Maiz")
                            print("6. Puerro")
                            print("7. Salir de la Tienda")
                            opcion = input("Que verdura desea comprar semillas: ")
                            match opcion:
                                case '1':
                                    while True:
                                        print("1. 25 semillas de Trigo")
                                        print("2. 50 semillas de Trigo")
                                        print("3. 75 semillas de Trigo")
                                        print("4. 100 semillas de Trigo")
                                        print("5. Regresar a la tienda")
                                        opcion = input("¿Que desea comprar?")
                                        match opcion:
                                            case '1':
                                                trigo1.dar25_semillas()
                                            case '2':
                                                trigo1.dar50_semillas
                                            case '3':
                                                trigo1.dar75_semillas()
                                            case '4':
                                                trigo1.dar100_semillas()
                                            case '5':
                                                print("Saliendo de la tienda de trigo...")
                                                time.sleep(2)
                                                break
                                            case _:
                                                print("No ingreso una opcion valida!")
                                case '2':
                                    while True:
                                        print("1. 25 semillas de Tomate")
                                        print("2. 50 semillas de Tomate")
                                        print("3. 75 semillas de Tomate")
                                        print("4. 100 semillas de Tomate")
                                        print("5. Regresar a la tienda")
                                        opcion = input("¿Que desea comprar?")
                                        match opcion:
                                            case '1':
                                                tomate1.dar25_semillas()
                                            case '2':
                                                tomate1.dar50_semillas()
                                            case '3':
                                                tomate1.dar75_semillas()
                                            case '4':
                                                tomate1.dar100_semillas()
                                            case '5':
                                                print("Saliendo de la tienda de tomate...")
                                                time.sleep(2)
                                                break
                                            case _:
                                                print("No ingreso una opcion valida!")
                                case '3':
                                    while True:
                                        print("1. 25 semillas de Cebolla")
                                        print("2. 50 semillas de Cebolla")
                                        print("3. 75 semillas de Cebolla")
                                        print("4. 100 semillas de Cebolla")
                                        print("5. Regresar a la tienda")
                                        opcion = input("¿Que desea comprar?")
                                        match opcion:
                                            case '1':
                                                cebolla1.dar25_semillas()
                                            case '2':
                                                cebolla1.dar50_semillas()
                                            case '3':
                                                cebolla1.dar75_semillas()
                                            case '4':
                                                cebolla1.dar100_semillas()
                                            case '5':
                                                print("Saliendo de la tienda de cebolla...")
                                                time.sleep(2)
                                                break
                                            case _:
                                                print("No ingreso una opcion valida!")
                                case '4':
                                    while True:
                                        print("1. 25 semillas de Zanahoria")
                                        print("2. 50 semillas de Zanahoria")
                                        print("3. 75 semillas de Zanahoria")
                                        print("4. 100 semillas de Zanahoria")
                                        print("5. Regresar a la tienda")
                                        opcion = input("¿Que desea comprar?")
                                        match opcion:
                                            case '1':
                                                zanahoria1.dar25_semillas()
                                            case '2':
                                                zanahoria1.dar50_semillas()
                                            case '3':
                                                zanahoria1.dar75_semillas()
                                            case '4':
                                                zanahoria1.dar100_semillas()
                                            case '5':
                                                print("Saliendo de la tienda de zanahoria...")
                                                time.sleep(2)
                                                break
                                            case _:
                                                print("No ingreso una opcion valida!")
                                case '5':
                                    while True:
                                        print("1. 25 semillas de Maiz")
                                        print("2. 50 semillas de Maiz")
                                        print("3. 75 semillas de Maiz")
                                        print("4. 100 semillas de Maiz")
                                        print("5. Regresar a la tienda")
                                        opcion = input("¿Que desea comprar?")
                                        match opcion:
                                            case '1':
                                                maiz1.dar25_semillas()
                                            case '2':
                                                maiz1.dar50_semillas()
                                            case '3':
                                                maiz1.dar75_semillas()
                                            case '4':
                                                maiz1.dar100_semillas()
                                            case '5':
                                                print("Saliendo de la tienda de maiz...")
                                                time.sleep(2)
                                                break
                                            case _:
                                                print("No ingreso una opcion valida!")
                                case '6':
                                    while True:
                                        print("1. 25 semillas de Puerro")
                                        print("2. 50 semillas de Puerro")
                                        print("3. 75 semillas de Puerro")
                                        print("4. 100 semillas de Puerro")
                                        print("5. Regresar a la tienda")
                                        opcion = input("¿Que desea comprar?")
                                        match opcion:
                                            case '1':
                                                puerro1.dar25_semillas()
                                            case '2':
                                                puerro1.dar50_semillas()
                                            case '3':
                                                puerro1.dar75_semillas()
                                            case '4':
                                                puerro1.dar100_semillas()
                                            case '5':
                                                print("Saliendo de la tienda de puerro...")
                                                time.sleep(2)
                                                break
                                            case _:
                                                print("No ingreso una opcion valida!")
                                case '7':
                                    print("Saliendo de la tienda...")
                                    time.sleep(2)
                                    break
                                case _:
                                    print("No ingreso una opcion valida!")
                    case '8':
                        print("Saliendo de los cultivos...")
                        time.sleep(2)
                        break
                    case _:
                        print("No ingreso una opcion valida!")
        case '2':
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
        case '3':
            print("Saliendo del juego!")
            time.sleep(2)
            bandera = 1
        case _:
            print("No ingreso una opcion valida!")
