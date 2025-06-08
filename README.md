# Chemistry portal

Этот документ содержит инструкции по настройке и запуску проекта на Django с использованием базы данных SQLite.

## Установка

## 1. Создайте виртуальное окружение и активируйте его:

bash
### Windows

python -m venv venv
venv\Scripts\activate

### Linux/macOS

python3 -m venv venv
source venv/bin/activate

2. Установите poetry и зависимости:

pip install poetry && poetry install

3. Примените миграции:

python back/manage.py migrate

4. Запустите сервер разработки:

python manage.py runserver

5. В файле .env добавьте значения для **FOLDER_ID** и **OAUTH_TOKEN**

6. Откройте браузер и перейдите по адресу:

    http://127.0.0.1:8000/

## Роли
| Роль    | Логин   | Пароль         |
|---------|---------|----------------|
| Учитель | teach   | teachteach     |
| Ученик  | student | studentstudent |
