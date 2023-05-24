# Как запустить код из репозитория
Сперва необходимо выкачать код из репозитория командой:
`git clone https://github.com/MReader-boop/stepik_module3_lesson6_step10.git`

Затем установить зависимости из файла `requirements.txt`.

## Установка зависимостей в виртуальное окружение
В папке с кодом создать виртуальное окружение командой в терминале:
`python -m venv <directory>`, где directory - название папки (угловые скобки вводить не надо), в которой будет находиться виртуальное окружение.

Затем активировать окружение командой:
`source <directory>/bin/activate`

После чего, установить зависимости командой:
`pip install -r requirements.txt`

## Установка зависимостей глобально
Обратите внимание, что данная команда установит все зависимости не в обособленное окружение, а как глобальный пакет для Python. Выполнить команду:
`pip install -r requirements.txt`

## Запуск кода
Выполнить команду:
`pytest --language=<language> --browser=<browser> test_items.py`, где
browser - Браузер, в котором будут выполняться тесты. На выбор:
Chrome
Firefox
language - Язык тестового браузера. На выбор:
en
ru
es
fr
