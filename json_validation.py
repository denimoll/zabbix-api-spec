import glob
import json
import os


def json_validation(file):
    try:
        with open(file, 'r') as f:
            json.load(f)
        return 1
    except Exception as e:
        print('Невалидный json-файл %s, ошибка: %s' % (file, e))
        return 0


input_dir = "input_example"
for cls in os.listdir(input_dir):
    for act in os.listdir('%s/%s' % (input_dir, cls)):
        path = "%s/%s/%s" % (input_dir, cls, act)
        files = glob.glob("%s/*.json" % path)
        for file in files:
            json_validation(file)