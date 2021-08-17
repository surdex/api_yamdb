# Учебный проект API сервиса YaMDb

Проект собирает отзывы пользователей о фильмах, книгах, музыке и др., которым можно присваивать жанр.
Список категорий и жанров может расширять только админ. Реализовано комментирование отзывов.
Проект написан для закрепления написания и работы с API сервисов.

Используются Python 3.7, Django и DRF, JWT-токены для аутентификации.
Формат передачи данных API - JSON. У неаутентифицированных пользователей
доступ к API только на чтение.

## Как запустить проект:

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры API запросов:

### Получение JWT-токена в обмен на email и confirmation_code - http://127.0.0.1:8000/api/v1/auth/token/

POST request:

```
{
  "email": "string",
  "confirmation_code": "string"
}
```

Response:

```
{
  "token": "string"
}
```


### Отправление confirmation_code на переданный email - http://127.0.0.1:8000/api/v1/auth/email/

POST request:

```
{
  "email": "string"
}
```

Response:

```
{
  "email": "string"
}
```


### Получить список всех отзывов/Создать новый - http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

GET Response:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

POST Request:

```
{
  "text": "string",
  "score": 1
}
```

POST Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


### Получить/обновить/удалить отзыв по id http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

PATCH request:

```
{
  "text": "string",
  "score": 1
}
```

GET/PUT Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

### Комментарии к отзывам

GET/PUT - http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

GET Response:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

POST Request:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

POST Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```

По id комментария GET/PATCH/DELETE -
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

PATCH Request:

```
{
  "text": "string"
}
```

Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
