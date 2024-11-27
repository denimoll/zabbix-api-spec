# zabbix-api-spec
## Get API specification for Zabbix
Полноценной спецификации API у Zabbix нет, но есть примеры на сайте для каждого метода. \ \
Скрипт *get_api_validation.py* предназначен для выгрузки всех примеров с официального сайта в одно место (директория *examples*). \
Скрипт *json_validation.py* необходим для проверки корректности примеров с сайта. \
Скрипт *create_common_jsons.py* создает общий json в рамках одного метода из примеров (директория *specification*).
## Zabbix 4.0
1. Для Zabbix 4.0 в 2021 году (тогда и был написан данный скрипт) было обнаружено 14 ошибок в примерах. По большей части это были лишние или недостающие запятые.
2. Для Zabbix 4.0 от 26.11.2024 выявлено 6 ошибок:
- Невалидный json-файл examples/triggerprototype/get/1.json, ошибка: Expecting ',' delimiter: line 9 column 16 (char 223)
- Невалидный json-файл examples/trend/get/0.json, ошибка: Illegal trailing comma before end of array: line 11 column 31 (char 292)
- Невалидный json-файл examples/discoveryrule/create/3.json, ошибка: Illegal trailing comma before end of object: line 28 column 58 (char 921)
- Невалидный json-файл examples/itemprototype/update/2.json, ошибка: Expecting ',' delimiter: line 13 column 12 (char 340)
- Невалидный json-файл examples/maintenance/create/0.json, ошибка: Illegal trailing comma before end of object: line 25 column 41 (char 793)
3. Для метода user.checkauthentication нестандартный адрес в документации (https://www.zabbix.com/documentation/4.0/en/manual/api/reference/user/user.checkauthentication), поэтому автоматически через скрипт пример не был скопирован. Стандартный путь: "class/action", например, "alert/get", а здесь "class/class.action". Пример добавлен вручную.
## Zabbix 5.0
1. Добавлены новые классы auditlog, autoregistration, task, а также несколько новых примеров для старых методов.
2. По сравнению с предыдущей версией выявлено уже 4 ошибки, но всё тех же:
- *(повтор)* Невалидный json-файл examples/trend/get/0.json, ошибка: Illegal trailing comma before end of array: line 11 column 31 (char 292)
- *(повтор)* Невалидный json-файл examples/discoveryrule/create/4.json, ошибка: Illegal trailing comma before end of object: line 28 column 58 (char 921)
- *(повтор)* Невалидный json-файл examples/itemprototype/update/2.json, ошибка: Expecting ',' delimiter: line 13 column 12 (char 340)
- *(повтор)* Невалидный json-файл examples/maintenance/create/0.json, ошибка: Illegal trailing comma before end of object: line 25 column 41 (char 793)
3. *(повтор)* Для метода user.checkauthentication нестандартный адрес в документации.
4. Для метода task.create (https://www.zabbix.com/documentation/5.0/en/manual/api/reference/task/create) не было создано примеров через скрипт, т.к. на сайте приводятся примеры до версии 5.0.5 и после версии 5.0.5. Примеры для версий после 5.0.5 добавлены вручную.
