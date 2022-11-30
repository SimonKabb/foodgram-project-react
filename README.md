# Foodgram
![workflow foodgram-project-react](https://github.com/SimonKabb/foodgram-project-react/actions/workflows/main.yml/badge.svg)

## Foodgram - социальная сеть для любителей рецептов
Позволяет пользователям публиковать рецепты с изображениями, добавлять рецепты в избранное и список покупок, подписыватся на других пользователей и скачивать список продуктов.

### Проект доступен по адресу:
http://51.250.105.140/
admin@admin.com
admin
### Стек технологий:

Python
Django REST framework
Docker
PostgreSQL

### Запуск проекта на сервере:
Сервер работает с Docker и docker-compose

- Клонирование репозитория:
```
git clone https://github.com/TheXtreme30/foodgram-project-react.git
```
- Выполните команды
```
cd foodgram-project-react/backend/
docker-compose up -d
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --no-input
```
-Создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

________________________________________
Backend-разработчик: Семен Капустников.
