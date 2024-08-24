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