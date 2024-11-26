# zabbix-api-spec
## Get API specification for Zabbix
Полноценной спецификации API у Zabbix нет, но есть примеры на сайте для каждого метода. \
Скрипт *get_api_validation.py* предназначен для выгрузки всех примеров с официального сайта в одно место. \
Скрипт *json_validation.py* необходим для проверки корректности примеров с сайта.
## For your info
1. Для Zabbix 4.0 в 2021 году (тогда и был написан данный скрипт) было обнаружено 14 ошибок в примерах. По большей части это были лишние или недостающие запятые.
2. Для Zabbix 4.0 от 26.11.2024 выявлено 6 ошибок:
- Невалидный json-файл input_example/triggerprototype/get/1.json, ошибка: Expecting ',' delimiter: line 9 column 16 (char 223)
- Невалидный json-файл input_example/trend/get/0.json, ошибка: Illegal trailing comma before end of array: line 11 column 31 (char 292)
- Невалидный json-файл input_example/discoveryrule/create/3.json, ошибка: Illegal trailing comma before end of object: line 28 column 58 (char 921)
- Невалидный json-файл input_example/itemprototype/update/2.json, ошибка: Expecting ',' delimiter: line 13 column 12 (char 340)
- Невалидный json-файл input_example/maintenance/create/0.json, ошибка: Illegal trailing comma before end of object: line 25 column 41 (char 793)