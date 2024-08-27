# 🎁 Proyecto de Juego de Cajas Sorpresa

## Descripción del Proyecto

Este es un juego de cajas sorpresa implementado en Python utilizando el framework Flask. Los usuarios deben hacer clic en las cajas, introducir la contraseña correcta basada en la pista proporcionada, y si aciertan, la caja se abrirá, revelando un regalo sorpresa. El juego incluye manejo de usuarios, pistas para cada caja, y una interfaz gráfica simple pero efectiva para interactuar con el usuario.

## Características

- **Interfaz Gráfica con HTML/CSS y JavaScript**: El juego presenta una interfaz de usuario interactiva donde las cajas pueden ser seleccionadas para ingresar una contraseña.
- **Autenticación de Usuario**: Los usuarios deben autenticarse para poder jugar.
- **Base de Datos**: Utiliza SQLite para almacenar información sobre usuarios y cajas.
- **Ventanas Modales**: Se utilizan ventanas modales para pedir la contraseña y para mostrar el regalo cuando se acierta la contraseña.
- **Deshabilitación de Cajas Abiertas**: Cuando una caja se abre correctamente, esta se deshabilita para no poder ser seleccionada de nuevo.

## Requisitos Previos

- **Python 3.x**
- **Flask**: Para instalar Flask, ejecuta el siguiente comando:
  ```bash
  pip install Flask
  ```

* **SQLite** : Para la base de datos.


## Estructura del Proyecto

/static
    /img
        - caja_abierta.png
        - caja_cerrada.png
        - regalo1.png
        - regalo2.png
        - regalo3.png
        - regalo4.png
        - regalo5.png
        - regalo6.png
        - regalo7.png
        - regalo8.png
        - regalo9.png
        - regalo10.png
/templates
    - index.html
    - login.html
    - base.html
    - modal.html
app.py
models.py
populate_db.py
index.js
README.md
`<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium">``<div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>``</div></div>``</pre>`

### Archivos Principales

1. **app.py** : El archivo principal de la aplicación Flask. Contiene todas las rutas para manejar las vistas y la lógica de negocio.
2. **models.py** : Contiene los modelos de la base de datos utilizando SQLAlchemy.
3. **populate_db.py** : Script para inicializar y poblar la base de datos con las cajas y pistas.
4. **index.js** : Archivo JavaScript que maneja la interacción de la interfaz de usuario, incluyendo la visualización de ventanas modales y el cambio de imágenes de las cajas.


## Instalación y Configuración

### Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/proyecto-cajas-sorpresa.git
cd proyecto-cajas-sorpresa
```


### Crear Entorno Virtual (Opcional)

Se recomienda utilizar un entorno virtual para manejar las dependencias del proyecto.

```bash
python3 -m venv env
source env/bin/activate   # En Windows, usa: env\Scripts\activate

```

### Instalar Dependencias

```
pip install -r requirements.txt

```


### Inicializar la Base de Datos

1. Asegúrate de haber creado el archivo** **`app.db` en el directorio del proyecto.
2. Corre el script de población de la base de datos:

```
python populate_db.py

```

Este script eliminará los datos antiguos de la tabla de cajas y agregará nuevamente las cajas con sus respectivas contraseñas y pistas.


### Ejecutar la Aplicación

```
`python main.py

```

La aplicación estará disponible en** **`http://127.0.0.1:5000/`.


## Uso de la Aplicación

1. **Inicio de Sesión** : El usuario debe autenticarse para acceder al juego.
2. **Seleccionar Caja** : Haciendo clic en una caja cerrada, se abrirá una ventana modal pidiendo la contraseña.
3. **Introducir Contraseña** : Basado en la pista, el usuario debe introducir la contraseña correcta para abrir la caja.
4. **Revelar Regalo** : Si la contraseña es correcta, la caja se abrirá, mostrando el regalo en una ventana modal. La imagen de la caja cambiará para indicar que ha sido abierta y quedará deshabilitada.

## Funcionalidades Clave

### Ventana Modal de Contraseña

Cuando el usuario selecciona una caja, se abre una ventana modal solicitando la contraseña. La pista de la caja seleccionada se muestra como un placeholder en el campo de entrada de contraseña.

### Cambiar Imagen de Caja al Abrirla

Si la contraseña es correcta, la caja se abrirá, cambiando su imagen a** **`caja_abierta.png` y quedará deshabilitada para evitar nuevas interacciones.

### Ventana Modal de Recompensa

Después de introducir correctamente la contraseña, se mostrará una ventana modal con una imagen de la recompensa, correspondiente a la caja seleccionada.

## Scripts Principales

### `populate_db.py`

Este script se encarga de limpiar y poblar la base de datos con las cajas y sus respectivas pistas y contraseñas. Útil cuando se desea reiniciar el juego desde cero.

### `index.js`

Maneja toda la lógica de frontend, como la apertura de ventanas modales, validación de contraseñas, y cambio de estado de las cajas.

## Personalización

### Añadir Nuevas Cajas

1. Agrega nuevas entradas en el archivo** **`populate_db.py` dentro de la lista** **`cajas`.
2. Asegúrate de incluir una imagen de recompensa correspondiente en la carpeta** **`static/img`.

### Modificar Contraseñas y Pistas

Para cambiar las contraseñas o pistas, puedes editar las entradas en el archivo** **`populate_db.py` y volver a ejecutar el script para actualizar la base de datos.

## Créditos

* **Desarrollador/a** : Álvaro Carrillo Ibáñez
* **Contacto** :  [aljusca@gmail.com]()
