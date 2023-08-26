# QRKot + Spreadsheets

### Приложение для Благотворительного Фонда поддержки котиков. Можно открывать проекты и быть тем, кто их закрывает своими пожертвованиями. Проекты закрываются по принципу FIFO (First In, First Out).
#### Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
#### Так же добавлена возможность сохранять отчет о скорости закрытия проектов. Чем быстрее проект закрыт, тем выше он будет в таблице. PS Для того чтобы работать с Google Cloud Platform, нужен гугл-аккаунт.

## Технологии:

* Python - 3.10
* FastAPI - 0.78.0
* Google Cloude Platform

##### P.S. Остальной стек в requirements.txt

## Для отчета нужно в Google Cloud Platform:
```sh
* Создать проект — связующее звено между нужными Google API и вашим Python-приложением.
* Подключить к проекту два API: Google Sheets API и Google Drive API.
* Создать сервисный аккаунт. Она служит для подключения и управления продуктами
и сервисами Google Cloud Platform из ваших приложений.
* Получить ключ и JSON-файл с данными сервисного аккаунта,
чтобы управлять подключенными API из вашего Python-приложения.
```

#### Для получения JSON:
```sh
* Перейдите на экран Credentials, нажмите на строчку с названием вашего сервисного аккаунта,
чтобы попасть в его настройки. Нажмите Keys – Add Key – Create New Key,
чтобы создать ключ доступа к вашему сервисному аккаунту
* Платформа предложит сохранить файл, в котором будут собраны все необходимые данные
для работы ваших Python-приложений с подключёнными ранее API. Выберите формат JSON и нажмите Create
* На ваш компьютер скачается JSON-файл с информацией о вашем сервисном аккаунте,
его приватный ключ, ID и ссылки для авторизации, а на платформе активируется бессрочный ключ
```
##### PS Переместите JSON-файл в надёжное место и никому не передавайте. Запомните, где вы сохранили этот файл, он вам ещё пригодится.


### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Oskalovlev/cat_charity_fund.git
```

```
cd cat_charity_fund
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Заполните .env со следующим содержанием:
```sh
APP_TITLE=QRKot
DESCRIPTION=Donats или ваше описание

DATABASE_URL=sqlite+aiosqlite:///./fastapi.db

SECRET=secret

# Созадние суперпользователя
FIRST_SUPERUSER_EMAIL=admin@admin.ru
FIRST_SUPERUSER_PASSWORD=admin

# Константы магических чисел
ZERO=0
LENGTH_NAME=100
MIN_ANYSTR_LENGTH=1
MIN_LENGTH_PASS=3
LIFETIME_JWT=36000

# Для отчета
FORMAT="%Y/%m/%d %H:%M:%S" или ваш вариант
ROW_COUNT=15
COLUMN_COUNT=5
ROW=10

# Данные из JSON c Google Cloude Platform
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=

EMAIL=ваша эл.почта
```

### Автор 
#### Оскалов Лев
