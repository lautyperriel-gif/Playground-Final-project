# Playground Final Project

Este proyecto es la **entrega final** del curso.  
Es una aplicación web estilo blog desarrollada en **Python (Django)** con manejo de usuarios, perfiles, páginas y mensajería.

---

## 🚀 Funcionalidades

- **Home** y **About** accesibles desde el menú de navegación.
- **Usuarios**:
  - Registro (signup)
  - Login / Logout
  - Perfil con avatar, bio y datos personales
  - Edición de perfil y cambio de contraseña
- **Páginas (Blog/Pages)**:
  - Crear, listar, buscar, editar y eliminar páginas
  - Uso de ckeditor (texto enriquecido), imágenes y fecha
  - Mensaje de aviso si no existen páginas o no hay resultados en la búsqueda
- **Mensajería interna** entre usuarios registrados
- **Class Based Views (CBV)** con mixins y uso de decoradores
- **Herencia de plantillas** con `base.html` y navegación en todas las vistas

---

## 📂 Instalación y ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lautyperriel-gif/Playground-Final-project.git
   cd Playground-Final-project
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Migraciones y superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

---

## 🔗 Rutas principales

- `/` → Home  
- `/about/` → About  
- `/pages/` → Listado de páginas  
- `/accounts/signup/` → Registro  
- `/accounts/login/` → Login  
- `/accounts/profile/` → Perfil de usuario  
- `/messenger/` → Mensajería  

---

## 📌 Notas importantes

- El archivo `db.sqlite3` y la carpeta `/media/` **no están en el repositorio** (excluidos en `.gitignore`).  
- `requirements.txt` incluye Django, Pillow, django-ckeditor y demás dependencias necesarias.  
- Todos los modelos están registrados en el admin de Django.  

---

## 🎥 Video demostración

Se adjunta un video (máx. 10 min) mostrando:  
1. Navegación por Home y About  
2. Registro, login y logout de usuarios  
3. Creación, edición, búsqueda y borrado de páginas  
4. Perfil de usuario (avatar, bio, edición y cambio de password)  
5. Mensajería entre usuarios  

---

## ⚠️ Nota sobre commits

En el historial de commits puede aparecer el nombre **PascualCoudannes** debido a una configuración global previa de Git en la PC utilizada.  
El desarrollo completo del proyecto corresponde a **Lautaro Perriel**.

---
