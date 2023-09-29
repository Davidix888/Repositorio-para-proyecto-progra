#Clases para determinar animales:
import time
import random
bandera = 0
class cultivos:
    def _init_(self,siembra,regar,cantidad, dinero):
        self.siembra = siembra #Cantidad de semillas que se utilizaran
        self.regar = regar #Regar los cultivos
        self.cantidad = cantidad #Semillas que se tienen en el inventario
        self.dinero = dinero #Cantidad de dinero obtenido por plantar

class trigo(cultivos):
    def _init_(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos._init_(self, siembra, regar, cantidad, dinero)
        self.tiempo = tiempo #Tiempo para cosechar los cultivos

    def plantarTrigo(self): #Funcion para plantar y las semillas que quedan
        print(f'Usted tiene: {self.cantidad}')
        self.siembra = int(input("Ingrese la cantidad de trigo a plantar: "))
        res = self.cantidad/5
        if self.siembra > res:
            print("Semillas insuficientes!")
        else:
            gastado = self.siembra*5
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
    def _init_(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos._init_(self, siembra, regar, cantidad, dinero)
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
    def _init_(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos._init_(self, siembra, regar, cantidad, dinero)
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
    def _init_(self, siembra, regar, cantidad, dinero, tiempo):
        super()._init_(siembra, regar, cantidad, dinero) 
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
    def _init_(self, siembra, regar, cantidad, dinero, tiempo):
        super()._init_(siembra, regar, cantidad, dinero)
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
    def _init_(self, siembra, regar, cantidad, dinero, tiempo):
        super()._init_(siembra, regar, cantidad, dinero)
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

class Animal:
    def _init_(self, nombre, salud_max, hambre_max, felicidad_max):
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
    def _init_(self):
        super()._init_("Vaca", salud_max=100, hambre_max=50, felicidad_max=100)

    def producir(self):
        return random.randint(5, 10)

class Oveja(Animal):
    def _init_(self):
        super()._init_("Oveja", salud_max=80, hambre_max=40, felicidad_max=90)

    def producir(self):
        return random.randint(1, 5)

class Gallina(Animal):
    def _init_(self):
        super()._init_("Gallina", salud_max=60, hambre_max=30, felicidad_max=80)

    def producir(self):
        return random.randint(2, 4)

class Granja:
    def _init_(self):
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
    def _init_(self):
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

trigo1 = trigo(0, 0, 25, 0, 0)
tomate1 = tomate(0, 0, 25, 0, 0)
cebolla1 = cebolla(0, 0, 25, 0, 0)
zanahoria1 = zanahoria(0, 0, 25, 0, 0)
maiz1 = maiz(0, 0, 25, 0, 0)
puerro1 = puerro(0, 0, 25, 0, 0)
granja1 = Granja()
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
            while True:
                opcion = input("¿Quieres pasar al dia siguiente? (s/n)").lower()
                if opcion == 'n':
                    print("Gracias por jugar. ¡Hasta luego!")
                    break
                
                granja1.simular_dia()
                
        case '3':
            print("Saliendo del juego!")
            time.sleep(2)
            bandera = 1
        case _:
            print("No ingreso una opcion valida!")
