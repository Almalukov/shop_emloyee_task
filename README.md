# shop_emloyee_task

Это пример инструкции README для запуска Django-приложения "shop_emloyee_task" в Docker-контейнере.

## Требования

Для запуска этого приложения в Docker-контейнере, у вас должны быть установлены:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (для легкой настройки контейнеров)

## Запуск приложения

1. Клонируйте репозиторий на свой компьютер:
   ```git clone https://github.com/ваш_репозиторий/shop_emloyee_task-django.git```

2.Перейдите в каталог проекта:
  ```cd myshop-django```

3.Скопируйте файл .env в .env и настройте переменные окружения, если это необходимо:
  ```cp .env .env```
  Редактируйте файл .env и укажите нужные значения переменных окружения

4.Соберите Docker-образ и запустите контейнер:
 ```docker-compose up --build```
 Это команда соберет Docker-образ и запустит контейнеры Django приложения и базы данных.

5.Откройте браузер и перейдите по адресу http://localhost:8008/ для доступа к вашему приложению.

6.Чтобы остановить контейнеры Docker, выполните следующую команду:
 ```docker-compose down```

Дополнительные настройки
При необходимости вы можете настроить дополнительные параметры в файле docker-compose.yml, такие как порты, переменные окружения и другие опции.

Вы можете управлять миграциями и другими командами Django, запустив их внутри контейнера Docker. Например:

```docker-compose exec web python manage.py migrate```
Замените migrate на другие команды Django, которые вам нужны.
    
