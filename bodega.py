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