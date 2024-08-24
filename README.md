# Sistema de Gestión de Inventario

Este proyecto implementa un sistema de gestión de inventario en Python. El sistema permite registrar productos, categorías, proveedores, y bodegas, así como gestionar el stock de productos.

## Características

- **Registro de Entidades:**
  - Registrar productos con atributos como nombre, descripción, precio, stock inicial y categoría.
  - Registrar categorías con nombre y descripción.
  - Registrar proveedores con nombre, dirección, teléfono y la lista de productos suministrados.
  - Registrar bodegas con nombre, ubicación, capacidad máxima y la lista de productos almacenados.

- **Gestión de Stock:**
  - Agregar stock a un producto existente.
  - Retirar stock de un producto existente.
  - Calcular el valor total del stock.

- **Relaciones entre Entidades:**
  - Asociar productos a categorías.
  - Asociar productos a proveedores.
  - Almacenar productos en bodegas, verificando la disponibilidad de espacio.

- **Consultas y Reportes:**
  - Consultar información de productos, categorías, proveedores y bodegas.
  - Generar informes de stock.

## Estructura del Código

### Clases Principales

1. **Producto**
   - Atributos:
     - `nombre`: Nombre del producto.
     - `descripcion`: Descripción del producto.
     - `precio`: Precio del producto.
     - `stockInicial`: Stock inicial del producto.
     - `stockActual`: Stock actual del producto.
   - Métodos:
     - `agregar_stock(cantidad)`: Agrega stock al producto.
     - `retirar_stock(cantidad)`: Retira stock del producto.
     - `calcular_valor_total()`: Calcula el valor total del stock del producto.

2. **Categoria**
   - Atributos:
     - `nombre`: Nombre de la categoría.
     - `descripcion`: Descripción de la categoría.
   - Métodos:
     - `agregar_producto(producto)`: Agrega un producto a la categoría.
     - `eliminar_producto(producto)`: Elimina un producto de la categoría.

3. **Proveedor**
   - Atributos:
     - `nombre`: Nombre del proveedor.
     - `direccion`: Dirección del proveedor.
     - `telefono`: Teléfono del proveedor.
   - Métodos:
     - `agregar_producto(producto)`: Agrega un producto a la lista de productos suministrados.
     - `eliminar_producto(producto)`: Elimina un producto de la lista de productos suministrados.

4. **Bodega**
   - Atributos:
     - `nombre`: Nombre de la bodega.
     - `ubicacion`: Ubicación de la bodega.
     - `capacidad_maxima`: Capacidad máxima de la bodega.
   - Métodos:
     - `agregar_producto(producto, cantidad)`: Agrega un producto a la bodega, verificando el espacio disponible.
     - `retirar_producto(producto, cantidad)`: Retira un producto de la bodega, verificando el stock disponible.
     - `consultar_disponibilidad(producto)`: Consulta la disponibilidad de un producto en la bodega.

## Ejemplo de Uso

```python
# Crear una categoría
categoria = Categoria("Electrónica", "Dispositivos electrónicos y gadgets")

# Crear un producto
producto = Producto("Laptop", "Laptop de 15 pulgadas", 1000.00, 10)

# Agregar el producto a la categoría
categoria.agregar_producto(producto)

# Crear un proveedor
proveedor = Proveedor("Proveedor A", "Calle 123", "123456789")

# Agregar el producto al proveedor
proveedor.agregar_producto(producto)

# Crear una bodega
bodega = Bodega("Bodega Central", "Zona Industrial", 100)

# Almacenar el producto en la bodega
bodega.agregar_producto(producto, 5)

# Consultar la disponibilidad del producto en la bodega
disponible = bodega.consultar_disponibilidad(producto)
print(f"Disponibilidad de {producto.nombre} en la bodega: {'Sí' si disponible else 'No'}")


