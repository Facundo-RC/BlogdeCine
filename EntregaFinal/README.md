# Butaca 🎬 · Blog de cine

Blog de reseñas de cine desarrollado con Django como entrega final del curso de Python. Los usuarios pueden registrarse, iniciar sesión y publicar posts sobre películas, con imagen, género y puntuación. Cada autor puede editar y eliminar sus propios posts, y cualquier visitante puede leerlos y buscarlos.

## Tecnologías

- Python 3
- Django 5.2
- Pillow (carga de imágenes)
- python-decouple (variables de entorno)
- SQLite (base de datos)
- Bootstrap 5 (estilos, cargado desde CDN)

## Funcionalidades

- **Posts:** listado, detalle, creación, edición y eliminación desde la interfaz web.
- **Datos de la película:** cada post puede indicar la película, el género y una puntuación de 1 a 5 estrellas. Los tres son opcionales.
- **Imágenes:** cada post puede tener una imagen opcional. Si no tiene, se muestra un recuadro en su lugar y la página no se rompe.
- **Usuarios:** registro, inicio y cierre de sesión.
- **Perfil:** página de perfil con avatar, descripción y lista de posts propios. Se puede editar.
- **Rutas protegidas:** crear, editar y eliminar posts, y ver o editar el perfil, requieren sesión iniciada. La protección está en las vistas con `@login_required`. Si un visitante entra a esas rutas, se lo redirige al login.
- **Permisos de autor:** solo el autor de un post puede editarlo o eliminarlo. Otro usuario recibe un error 403.
- **Buscador:** busca posts por título, película o contenido y avisa cuando no hay resultados.
- La barra de navegación cambia según el usuario sea anónimo o esté logueado.

## Instalación

Los comandos se ejecutan en una terminal, dentro de la carpeta del proyecto.

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <carpeta-del-repositorio>
```

### 2. Crear y activar el entorno virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear el archivo `.env`

El proyecto lee la clave secreta desde un archivo `.env`, que no se sube al repositorio. Hay que crearlo copiando el ejemplo:

Windows:

```bash
copy .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

Después, reemplazá el valor de `SECRET_KEY` en `.env` por una clave propia. Se puede generar una con:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

| Variable | Para qué sirve | Valor para desarrollo |
|---|---|---|
| `SECRET_KEY` | Clave secreta de Django | La que generaste |
| `DEBUG` | Modo desarrollo (muestra errores y sirve las imágenes) | `True` |
| `ALLOWED_HOSTS` | Dominios permitidos, separados por coma | `127.0.0.1,localhost` |

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

### 6. Crear un superusuario (opcional)

Solo hace falta para entrar al panel de administración en `/admin/`:

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrí <http://127.0.0.1:8000/> en el navegador.

## Probar el proyecto desde cero

El repositorio no incluye la base de datos (`db.sqlite3`) ni las imágenes subidas (`media/`). Las dos se crean solas al usar el proyecto: la base con `migrate` y la carpeta `media/` al subir la primera imagen.

Para recorrerlo:

1. Entrá como visitante: se ven los posts y el buscador, pero no los botones para crear o editar.
2. Probá abrir <http://127.0.0.1:8000/nuevo/> sin sesión: te redirige al login.
3. Registrate desde **Registrarme**. Quedás logueado automáticamente.
4. Creá un post con imagen, película, género y puntuación, y otro solo con título y contenido.
5. Editá y eliminá uno de tus posts.
6. Editá tu perfil y subí una imagen de perfil.
7. Cerrá sesión, registrá un segundo usuario e intentá editar un post del primero: recibís un error 403.

## Estructura

```
config/      configuración del proyecto (settings, urls)
posts/       app de publicaciones: modelo, vistas, formularios y templates
usuarios/    app de usuarios: registro, login, perfil y avatar
templates/   template base y fragmentos compartidos
static/      estilos propios (css/estilos.css)
```

## Autor

Facundo Robaño · Entrega final del curso de Python
