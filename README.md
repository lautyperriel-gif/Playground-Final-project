# Playground Final Project 

## Pasos
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Rutas: `/` (home), `/about/`, `/pages/`, `/accounts/signup/`, `/accounts/login/`, `/accounts/profile/`, `/messenger/`
No subir `db.sqlite3` ni `media/`.
