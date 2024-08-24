class Producto:
          def __init__(self, nombre, descripcion, precio, stock_inicial):
              self.nombre = nombre
              self.descripcion = descripcion
              self.precio = precio
              self.stock_inicial = stock_inicial
              self.stock_actual = stock_inicial

          def agregar_stock(self, cantidad):
              self.stock_actual += cantidad

          def retirar_stock(self, cantidad):
              if cantidad <= self.stock_actual:
                  self.stock_actual -= cantidad
              else:
                  raise ValueError("Cantidad a retirar excede el stock disponible")

          def calcular_valor_total(self):
              return self.precio * self.stock_actual


class Categoria:
          def __init__(self, nombre, descripcion):
              self.nombre = nombre
              self.descripcion = descripcion
              self.productos = []

          def agregar_producto(self, producto):
              self.productos.append(producto)

          def eliminar_producto(self, producto):
              self.productos.remove(producto)


class Proveedor:
          def __init__(self, nombre, direccion, telefono):
              self.nombre = nombre
              self.direccion = direccion
              self.telefono = telefono
              self.productos_suministrados = []

          def agregar_producto(self, producto):
              self.productos_suministrados.append(producto)

          def eliminar_producto(self, producto):
              self.productos_suministrados.remove(producto)


class Bodega:
          def __init__(self, nombre, ubicacion, capacidad_maxima):
              self.nombre = nombre
              self.ubicacion = ubicacion
              self.capacidad_maxima = capacidad_maxima
              self.productos_almacenados = {}

          def agregar_producto(self, producto, cantidad):
              if producto in self.productos_almacenados:
                  if self.productos_almacenados[producto] + cantidad <= self.capacidad_maxima:
                      self.productos_almacenados[producto] += cantidad
                  else:
                      raise ValueError("No hay espacio disponible en la bodega")
              else:
                  if cantidad <= self.capacidad_maxima:
                      self.productos_almacenados[producto] = cantidad
                  else:
                      raise ValueError("No hay espacio disponible en la bodega")

          def retirar_producto(self, producto, cantidad):
              if producto in self.productos_almacenados:
                  if cantidad <= self.productos_almacenados[producto]:
                      self.productos_almacenados[producto] -= cantidad
                      if self.productos_almacenados[producto] == 0:
                          del self.productos_almacenados[producto]
                  else:
                      raise ValueError("Cantidad a retirar excede el stock disponible en la bodega")
              else:
                  raise ValueError("El producto no se encuentra en la bodega")

          def consultar_disponibilidad(self, producto):
              return self.productos_almacenados.get(producto, 0) > 0
