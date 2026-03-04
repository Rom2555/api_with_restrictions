# API Объявлений (api_with_restrictions)

REST API для мобильного приложения с объявлениями. Реализовано на Django + Django REST Framework.

## Возможности

- **Создание объявлений** - только для авторизованных пользователей
- **Просмотр объявлений** - без авторизации
- **Фильтрация** по дате создания и статусу
- **Обновление/удаление** - только автор объявления
- **Лимиты запросов**:
  - Неавторизованные: 10 запросов/минута
  - Авторизованные: 20 запросов/минута

## Статусы объявлений

- `OPEN` - объявление открыто
- `CLOSED` - объявление закрыто

## Ограничения

- Максимум 10 открытых объявлений на одного пользователя

## Установка

```bash
# Установка зависимостей
pip install -r requirements.txt

# Создание базы данных PostgreSQL
createdb -U postgres netology_classified_ads

# Применение миграций
python manage.py migrate

# Запуск сервера
python manage.py runserver
```

## API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/advertisements/` | Список объявлений |
| POST | `/api/advertisements/` | Создание объявления |
| GET | `/api/advertisements/{id}/` | Получение объявления |
| PATCH | `/api/advertisements/{id}/` | Обновление объявления |
| DELETE | `/api/advertisements/{id}/` | Удаление объявления |

## Параметры фильтрации

- `created_at_after` - дата создания от (включительно)
- `created_at_before` - дата создания до (включительно)
- `status` - статус объявления (OPEN/CLOSED)
- `creator` - ID создателя

Примеры:
```
/api/advertisements/?status=OPEN
/api/advertisements/?created_at_after=2026-01-01
/api/advertisements/?created_at_before=2026-03-01
```

## Аутентификация

API использует Token Authentication. Для авторизованных запросов добавляйте заголовок:

```
Authorization: Token <ваш_токен>
```

### Получение токена

1. Создайте пользователя через админку Django (`/admin/`)
2. Создайте токен для пользователя в разделе Tokens
3. Используйте токен в заголовках запросов

## Примеры запросов

См. файл [`requests-examples.http`](requests-examples.http)

## Структура проекта

```
api_with_restrictions/
├── advertisements/
│   ├── models.py       # Модели (Advertisement)
│   ├── views.py        # ViewSet с правами доступа
│   ├── serializers.py  # Сериализаторы + валидация
│   ├── filters.py      # Фильтры
│   ├── permissions.py  # Права доступа
│   └── migrations/     # Миграции
├── api_with_restrictions/
│   ├── settings.py     # Настройки Django
│   └── urls.py         # URL маршруты
└── manage.py
```

## Технологии

- Django 3.1+
- Django REST Framework
- django-filter
- PostgreSQL
