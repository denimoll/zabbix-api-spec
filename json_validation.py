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


path_examples = "examples"
for cls in os.listdir(path_examples):
    for act in os.listdir('%s/%s' % (path_examples, cls)):
        path = "%s/%s/%s" % (path_examples, cls, act)
        files = glob.glob("%s/*.json" % path)
        for file in files:
            json_validation(file)