### Привет) Представляю мой проект по имопрту оборотной ведомости из excel в базу данных 'excel_import'

Цель проекта - на основании оборотной ведомости, данной в формате xls, споектировать базу данных, 
настроить процедуру иморта дынных из excel таблицы в нужные таблицы в базе данных. Также необходимо было обернуть данную функциональность в web-интерфейс.

>В качестве субд была выбрана sqlite3
>Язык програмирования - Python3
>Web-framework - Django4
>Дополнительные зависимости находятся в файле requirement.txt

Исходные данные: 'ОСВ для тренинга.xls'

Предварительная работа с исходными данными: файл ОСВ для тренинга.xls был переименован в balance.xls | сконвертироан в balance.xlsx()

Проектирование базы дынных:
---
>1)Были выделеены слудующие информационные обьекты:

* Счет
* Банк 
* Класс 

>2) Были созданы соответствующие таблицы 

* account
* bank
* class

>3)На основании столбцов таблицы данной оборотной ведомости были определены следующие столбцы таблиц бд

* для account - in_active=входящие активы, in_passive=входящие пассивы ,debet=дебет, credit=кредит,
out_active=исходящие активы, out_passive=исходящие пассивы, class_id(внешний ключ ссылается на таблице class), 
bank_id(внешний ключ ссылаается на таблицу bank)
* для bank - in_active=входящие активы, in_passive=входящие пассивы ,debet=дебет, credit=кредит,
out_active=исходящие активы, out_passive=исходящие пассивы, class_id(внешний ключ ссылается на таблице class)
* для class - in_active=входящие активы, in_passive=входящие пассивы ,debet=дебет, credit=кредит,
out_active=исходящие активы, out_passive=исходящие пассивы


Процедура импорта:
---
+ Для извлечения данных из таблицы Excel был использован модуль openpyxl
+ Данные построчно извлекаются в list, затем первый элемент проверятся с помощью регулярных выражений(4 цифры - счет, 2 цифры - банк)
+ Данные записываются в соответствующую таблицу sqlite3
+ При запуске сервера иморт производится при нажатии на кнопку import.
+ Для просмотра содержания получившейся базы данных используется ресурс: https://inloop.github.io/sqlite-viewer

![Альтернативный текст](/путь/screenshots/bank.jpg)
https://sun9-75.userapi.com/impg/gCENO5iBfirMAf3pD0d1dHbOlZZMuIaaTbNXvw/WXr9QrUEKJc.jpg?size=1096x737&quality=96&sign=687a43a0764394388dd2157d1b43cd6f&type=album