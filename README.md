# API Test Automation Framework

Тестовое задание для автоматизации API, проект соответствует требованиям технического задания

Тестируемая среда: (https://jsonplaceholder.typicode.com/)

## Структура проекта

*  **api\client.py** — HTTP API-клиент для взаимодействия с API, логика запросов и ретраев(цикл)

*  **assertions\checks.py** — assert проверки status code'ов, схем относительно словаря, логика.

*  **models\schema.py** — схемы данных (да, мог использовать pydantic, но mock-API, очень простое - проще было написать свой словарь относительно схемой)

*  **tests\test_posts.py** — GET, POST, PUT, PATCH, DELETE запросы 

*  **tests\test_users.py** - проверки эндпоинтов работы с пользователями

*  **config.py** — конфигурация фреймворка через переменные окружения.

*  **conftest.py** — фикстуры, клиент инит.

*  **pytest.ini** — настройки флоу тест кейсов, маркеры сценариев, формат логгирования.


## Покрытие:

1. Получение списка пользователей ('GET /users' , 'test_get_users')

2. Получение пользователя по ID ('GET /users/{id}', 'test_get_user_by_id')

3. Несуществующий пользователь ('GET /users/9999' , 'test_get_missing_user')

4. Получение списка постов ('GET /posts' , 'test_get_posts')

5. Создание поста ('POST /posts' , `test_create_post')

6. Полное обновление поста ('PUT /posts/{id}' , 'test_update_post')

7. Частичное обновление поста ('PATCH /posts/{id}' , 'test_patch_post')

8. Удаление поста ('DELETE /posts/{id}' , 'test_delete_post')

9. Комментарии конкретного поста ('GET /posts/{id}/comments' , 'test_get_post_comments')

10. Некорректный payload ('POST /posts' , 'test_create_post_with_invalid_payload')



## Требования проекта

* **Python 3.14.5** (требование 3.11+)
* Зависимости из "requirements.txt" (**pytest==8.2.0, requests==2.31.0, pytest-html==4.1.1**)


## Настройка окружения

**Переменные окружения:**

* **"BASE_URL"** — адрес эндпоинта API (в нашем случае - `https://jsonplaceholder.typicode.com`)
* **"REQUEST_TIMEOUT"** — таймаут ожидания ответа в секундах (по умолчанию: "5")(в случае превышения сценарий фейлится)
* **"RETRY_COUNT"** — количество повторных попыток при сбоях (по умолчанию: "1")

## Запуск тестов

**Запуск всех сценариев(full):**

pytest -m full

**Запуск Smoke:**

pytest -m smoke

**Запуск негативных сценариев:**

pytest -m negative

**Запуск тестов с генерацией HTML-отчета** (отчет будет сохранен в report.html`):

pytest -m full --html=report.html --self-contained-html

## Комментарии
Проект масштабируется, разделен на разные слои(API layer / assertions / test logic)
