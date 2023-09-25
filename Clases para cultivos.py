#Clases para determinar animales:
import time
bandera = 0
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

class tomate(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos.__init__(siembra, regar, cantidad, dinero)
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

class cebolla(cultivos):
    def __init__(self, siembra, regar, cantidad, dinero, tiempo):
        cultivos().__init__(siembra, regar, cantidad, dinero)
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

trigo1 = trigo(0, 0, 25, 0, 0)
tomate1 = tomate(0, 0, 25, 0, 0)
cebolla1 = cebolla(0, 0, 25, 0, 0)
zanahoria1 = zanahoria(0, 0, 25, 0, 0)
maiz1 = maiz(0, 0, 25, 0, 0)
puerro1 = puerro(0, 0, 25, 0, 0)
while bandera == 0:
    print("1. Trigo")
    print("2. Tomate")
    print("3. Cebolla")
    print("4. Zanahoria")
    print("5. Maiz")
    print("6. Puerro")
    print("7. Informacion")
    print("8. Tienda")
    print("9. Salir")
    opcion = input("¿Que desea hacer?")
    match opcion: 
        case '1':
            print("1. Plantar")
            print("2. Cosechar")
            print("3. Regar")
            opcion = input("¿Que desea hacer?")
            match opcion:
                case '1':
                    trigo1.plantarTrigo()
                case '2':
                    trigo1.crecimientoTrigo()
                case '3':
                    trigo1.regarTrigo()
        case '2':
            print("1. Plantar")
            print("2. Cosechar")
            print("3. Regar")
            opcion = input("¿Que desea hacer?")
            match opcion:
                case '1':
                    tomate1.plantarTomate()
                case '2':
                    tomate1.crecimientoTomate()
                case '3':
                    tomate1.regarTomate()
        case '3':
            print("1. Plantar")
            print("2. Cosechar")
            print("3. Regar")
            opcion = input("¿Que desea hacer?")
            match opcion:
                case '1':
                    cebolla1.plantarCebolla()
                case '2':
                    cebolla1.crecimientoCebolla()
                case '3':
                    cebolla1.regarCebolla()
        case '4':
            print("1. Plantar")
            print("2. Cosechar")
            print("3. Regar")
            opcion = input("¿Que desea hacer?")
            match opcion:
                case '1':
                    zanahoria1.plantarZanahoria()
                case '2':
                    zanahoria1.crecimientoZanahoria()
                case '3':
                    zanahoria1.regarZanahoria()
        case '5':
            print("1. Plantar")
            print("2. Cosechar")
            print("3. Regar")
            opcion = input("¿Que desea hacer?")
            match opcion:
                case '1':
                    maiz1.plantarMaiz()
                case '2':
                    maiz1.crecimientoMaiz()
                case '3':
                    maiz1.regarMaiz()
        case '6':
            print("1. Plantar")
            print("2. Cosechar")
            print("3. Regar")
            opcion = input("¿Que desea hacer?")
            match opcion:
                case '1':
                    puerro1.plantarPuerro()
                case '2':
                    puerro1.crecimientoPuerro()
                case '3':
                    puerro1.regarPuerro()
        case '9':
            print("Saliendo del juego!")
            time.sleep(2)
            bandera = 1
        case _:
            print("No ingreso una opcion valida!")
