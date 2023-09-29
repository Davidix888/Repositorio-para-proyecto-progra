class Usuario:
    def __init__(self, idUsuario, nombre, email, contrasena, direccion, pago):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena
        self.direccion = direccion
        self.pago = pago

    def registro_usuario(self):
        self.idUsuario = int(input('Ingresa tu ID de usuario: '))
        self.nombre = input('Ingresa tu nombre de usuario: ')
        self.email = input('Ingresa tu direccion de correo electronico: ')
        self.contrasena = input('Ingresa tu contraseña: ')
        pago = input('Ingresa tu metodo de pago (Debes escribir): ')
        if self.pago == 'Credito':
            tarjeta = int(input('Ingresa tu numero de tarjeta: '))
            print('Tu tarjeta ha sido registrada')
        elif self.pago =='Paypal':
            paypal = input('Ingresa tu usuario de paypal')
            print('Tu usuario ha sido registrado')
        elif self.pago == 'efectivo':
            print('Pagaras al recibir tu producto')
        else:
            print('No haz seleccionado ningun metodo')

    def inicio_sesion(self):
        print('Bienvenido al inicio de sesion: ')
        uIngreso = input('Ingrese su nombre: ')
        if uIngreso == self.nombre:
            print('El nombre de usuario esta registrado ')
        else:
            print('Tu nombre de usuario no esta registrado')

        Ucontrsena = input('Ingresa tu contraseña: ')
        if Ucontrsena == self.contrasena:
            print('Tu contraseña es correcta')

# class Producto:
#     def __init__(self, idProducto, nombre_producto, descripcion, precio, stock): 
#         self.idProducto = idProducto
#         self.nombre_producto = nombre_producto
#         self.descripcion = descripcion
#         self.precio = precio
#         self.stock = stock

#     def ingreso_prod(self):
#         idProducto = self.idProducto
#         nombre_producto = self.nombre_productoProducto
#         descripcion = self.descripcion
#         precio = self.precio
#         stock = self.stock


# class Carrito(Producto):
#     def __init__(self, idProducto, nombre_producto, descripcion, precio, stock, idOrden, producto,subtotal,impuestos):
#         super().__init__(idProducto, nombre_producto, descripcion, precio, stock)
#         self.idOrden = idOrden
#         self.producto = producto
#         self.subtotal = subtotal
#         self.impuestos = impuestos

#     def 




def registro_usuario1():
usuario1 = Usuario(idUsuario, )









# def prod():
#     idProducto = int(input('Ingrese el ID del producto: '))        