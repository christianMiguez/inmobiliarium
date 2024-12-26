# Inmobiliarium

Inmobiliarium is a Django-based web application for managing hawaii and caribbean real estate listings. This project allows users to browse, search, and filter real estate listings. This is the typical CRUD app where superusers can create, read, update, and delete properties.

The first time after you execute django-admin startproyect inmobiliarium, you need to do the following steps:

1. add import os en settings.py
2. create templates, static folder
3. In settings specify static, templates, etc paths:


```
- TIME_ZONE
```

```
- STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

```
- (dirs) TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        (...)
```

4. python3 manage.py startapp inmobiliariumwebsite (or whatever you want to call it)

This inmobiliariumwebsite app will contain the models, views, and templates for the project.

5. en installed_apps add the app

```
- INSTALLED_APPS = [
    'inmobiliariumwebsite',
    (...)
```

6. Create models in models.py

7. Create views in views.py

8. Create urls in urls.py

9. run python3 manage.py makemigrations

10. run python3 manage.py migrate

11. run python3 manage.py createsuperuser. for dev we are using: 
chris
ChrisPass101

12. in admin.py register the models by doing:



