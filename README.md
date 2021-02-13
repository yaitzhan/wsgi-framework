## Простой WSGI-фреймворк


### Описание работы фреймворка:

1) возможность отвечать на get запросы пользователя (код ответа + html страница)
2) для разных url - адресов отвечать разными страницами
3) page controller - возможность без изменения фреймворка добавить view для обработки нового адреса
4) front controller - возможность без изменения фреймворка вносить изменения в обработку всех запросов
5) рендеринг страниц через шаблонизатор jinja2
6) middleware для отслеживания зашел ли пользователь с мобильного устройства

### Установка

    python -m venv venv
    source venv/bin/activate (lin) или venv/Scripts/activate (win)
    git clone https://github.com/yaitzhan/wsgi-framework
    cd wsgi-framework
    python setup.py install

### Использование

Пример использования в данном [проекте](https://github.com/yaitzhan/wsgi-framework-usage-example)

### TODO

* [ ] ф-ционал автогенерации структуры проекта при вызове команды из консоли
