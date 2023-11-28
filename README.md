Описание
=
Данный проект предназначен для сокращения ссылок

Установка
=

```$ python3 -m pip install requests```
```$ python3 -m pip install argparse```

Настройка окружения
=

Для работы с bitly необходимо установить токен авторизации:

```$ python3 -m pip install python-dotenv```

```from dotenv import load_dotenv, find_dotenv```
```load_dotenv()```

Требования к окружению
=
Python 3.*

Ключ API. В переменную ```token``` надо положить Ключ API из кабинета  ![Как получить Токен](https://dev.bitly.com/)
GENERIC ACCESS TOKEN  - нужный тип токена

Инструкция
=

Если введенная ссылка битлинк, то на выходе будет количество кликов по ней.
Если не битлинк, то программа преобразует ее в битлинк

Примеры запуска скриптов
=

Если указанная ссылка уже сокращена(bitlink):
-

```$ python3 main.py bit.ly/3MUIV8U```

Количество кликов: **0**

![Screenshot](https://drive.google.com/file/d/10cKe_zAHuwjSpoppwgkjp_ruwTpy7TED/view?usp=sharing)

Если не Bitlink:
-

```%  python3 main.py https://www.tk-drive.com/tables```

Битлинк bit.ly/3sUmw4U
