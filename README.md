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

### 1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/gestion-inventario.git

```
### 2. Navega al directorio del proyecto:
```bash
cd sistema-gestion-inventario
```
### 3. Crear un entorno virtual:
En Windows:
```bash

python -m venv venv
```
En macOS/Linux:
```
python3 -m venv venv
```
### 4. Activar el entorno virtual:
En Windows:
```bash

.\venv\Scripts\activate
```
En macOS/Linux:
```bash

source venv/bin/activate
```
### 5. Instalar dependencias:
Si tienes un archivo requirements.txt, instala las dependencias con el siguiente comando:

```bash

pip install -r requirements.txt
```
### 6. Ejecución del Proyecto:
Una vez que hayas activado el entorno virtual y hayas instalado todas las dependencias necesarias, puedes ejecutar el proyecto de la siguiente manera:

```bash
python main.py
```
Asegúrate de que el archivo main.py contenga el código para instanciar y utilizar las clases del sistema de gestión de inventario.

### 7. Uso del Proyecto
El sistema de gestión de inventario permite registrar productos, categorías, proveedores y bodegas, así como gestionar el stock y realizar consultas sobre la disponibilidad de productos.

