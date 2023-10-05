# Проект FastAPI для отправки электронной почты

## Описание проекта

Этот проект использует FastAPI для создания RESTful API, которое позволяет отправлять электронные письма.

## Зависимости

- Python 3.11
- FastAPI
- Pydantic
- uvicorn
- unittest

## Установка и запуск с Docker

Для сборки и запуска контейнера выполните:

```bash
docker-compose up --build
```

## Создайте файл '.env' в корневой директории со следующими переменными:

```bash
SMTP_EMAIL=your_smtp_email
SMTP_PASSWORD=your_smtp_password
SMTP_SERVER=your_smtp_server
SMTP_PORT=your_smtp_port
```

## API Endpoints

- POST `/send_email/`: Отправить электронное письмо

## Пример тела запроса

```json
{
  "to": "recipient@example.com",
  "subject": "Your Subject",
  "message": "Your message here"
}
```

## Тестирование

Тесты написаны с использованием библиотеки unittest. Для запуска тестов выполните:

```bash
python -m unittest
```
