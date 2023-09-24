#Clases para determinar animales:
import time
class cultivos:
    def __init__(self,siembra,regar,cosechar,cantidad):
        self.siembra = siembra #Cantidad de semillas que se utilizaran
        self.regar = regar #Regar los cultivos
        self.cosechar = cosechar #Para obtener los cultivos
        self.cantidad = cantidad #Semillas que se tienen en el inventario

class trigo(cultivos):
    def __init__(self, siembra, regar, cosechar, cantidad, tiempo):
        super().__init__(siembra, regar, cosechar, cantidad)
        self.tiempo = tiempo #Tiempo para cosechar los cultivos

    def plantar(self): #Funcion para plantar y las semillas que quedan
        cantidad = self.cantidad
        siembra = self.siembra
        restante = cantidad - siembra
        print(f'Haz utilizado {self.siembra} semillas y te quedan {restante}')

    def crecimiento(self): #Contadora hacia atras para saber cuando estaran listos los cultivos
        import time #import time para hacer el conteo hacia atras utilizando sleep que una pausa de 1 seg
        tiempo = self.tiempo
        regar = self.regar

        print("Tus cultivos estaran listos en:")

        while tiempo > 0:
            minutos = tiempo // 60
            segundos = tiempo % 60
            print(f"Tiempo restante: {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1) 
            tiempo -= 1
        
        print('Tus cultivos estan listos para ser recogidos')
            
    def cosechar(self): #Para obtener la cosecha
        cosechar = self.cosechar
        print(f'Has cosechado {cosechar} unidades de trigo')
        
def datos_para_trigo():
    print('Recuerda que si estas iniciando comienzas con 50 semillas')
    siembra = int(input('Ingresa la cantidad de semillas que utilizaras:'))
    cosecha = siembra
    trigo1 = trigo(siembra,60,cosecha,50,120)
    trigo1.plantar()
    trigo1.crecimiento()
    trigo1.cosechar()
    

def datos_para_tomate():
    print('Recuerda que si estas iniciando comienzas con 50')
    siembra = int(input('Ingresa la cantidad de semillas que utilizaras: '))
    cosecha = siembra
    tomate1 = trigo(siembra,60,cosecha,50,180)
    tomate1.plantar()
    tomate1.crecimiento()
    tomate1.cosechar()

def datos_para_cebolla():
    print ('Recuerda que si estas iniciando comienzas con 50')
    siembra = int(input('Ingresa la cantidad de semillas que utilizaras: '))
    cosecha = siembra
    cebolla1 = trigo(siembra,60,cosecha,50,240)
    cebolla1.plantar()
    cebolla1.crecimiento()
    cebolla1.cosechar()

def datos_para_zanahoria():
    print ('Recuerda que si estas iniciando comienzas con 50')
    siembra = int(input('Ingresa la cantidad de semillas que utilizaras: '))
    cosecha = siembra
    zanahoria = trigo(siembra,60,cosecha,50,60)
    zanahoria.plantar()
    zanahoria.crecimiento()
    zanahoria.cosechar()

def datos_para_maiz():
    print ('Recuerda que si estas iniciando comienzas con 50')
    siembra = int(input('Ingresa la cantidad de semillas que utilizaras: '))
    cosecha = siembra
    maiz= trigo(siembra,60,cosecha,50,160 )
    

print('Menu para plantas')
print('1. Plantar trigo')
print('2. Plantar tomate')
print('3. Plantar cebollas')
print('4. Plantar Zanahoria')
opcion = int(input('Ingrese la opcion que desea: '))
match opcion:
    case 1:
        datos_para_trigo()
    case 2:
        datos_para_tomate()
    case 3:
        datos_para_cebolla()
    case 4:
        datos_para_zanahoria()
    
    

