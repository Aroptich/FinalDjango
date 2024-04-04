![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/django-3670A0?style=for-the-badge&logo=django&logoColor=6aa84f)

# FinalDjango  

## Запуск приложения

> Загрузка проекта
```bash
git clone https://github.com/Aroptich/FinalDjango.git
cd FinalDjango
```
## Установка Django_SECRET_KEY
[DJANGO SECRET KEY GENERATOR](https://djecrety.ir/)
```bash
echo SECRET_KEY='your SECRET_KEY' > .env
```


## Установка зависимостей

> Установка библиотеки __poetry__
```bash
pip install poetry
```
> Установка всех зависимостей приложения
```bash
poetry install
```
> Активирование вертуальной среды
```bash
poetry shell
```
> Установка миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

> Запуск сервера
```bash
python manage.py runserver
```
Открыть приложение в браузере по адресу [localhost:8000](http://127.0.0.1:8000/api/schema/swagger-ui/)