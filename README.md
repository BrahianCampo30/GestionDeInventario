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

## Instalación y Ejecución

Para instalar y ejecutar el proyecto, sigue los siguientes pasos:

## **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/sistema-gestion-inventario.git

## **Navega al directorio del proyecto:**

Copiar código
cd sistema-gestion-inventario

## **Crear un entorno virtual:**

En sistemas Unix/macOS:

Copiar código
python3 -m venv venv
En Windows:

Copiar código
python -m venv venv
**Activar el entorno virtual:**

En sistemas Unix/macOS:

Copiar código
source venv/bin/activate
En Windows:

Copiar código
.\venv\Scripts\activate
## Instalar dependencias:

Si tienes un archivo requirements.txt, instala las dependencias con el siguiente comando:

Copiar código
pip install -r requirements.txt
Ejecución del Proyecto:

Una vez que hayas activado el entorno virtual y hayas instalado todas las dependencias necesarias, puedes ejecutar el proyecto de la siguiente manera:

Copiar código
python main.py
Asegúrate de que el archivo que estás ejecutando contenga el código para instanciar y utilizar las clases del sistema de gestión de inventario.

**Uso del Proyecto**
El sistema de gestión de inventario permite registrar productos, categorías, proveedores y bodegas, así como gestionar el stock y realizar consultas sobre la disponibilidad de productos. Primero, se crean categorías para organizar los productos, como "Electrónica" para agrupar dispositivos. Luego, se registran productos con atributos como nombre, descripción, precio y stock inicial, y se asocian a categorías. Los productos también se pueden asignar a proveedores que los suministran, añadiendo detalles como nombre, dirección y teléfono del proveedor. Posteriormente, los productos se almacenan en bodegas, verificando la capacidad disponible. Finalmente, el sistema permite consultar la disponibilidad de productos en una bodega específica y generar reportes de stock por categoría, proveedor o bodega, facilitando la gestión integral del inventario.

