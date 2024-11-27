import json
import glob
import os


def recurs_merge(dictionary1, dictionary2):
    for key in dictionary1.keys():
        if dictionary2.get(key):
            if isinstance((dictionary1.get(key)), dict) and isinstance((dictionary2.get(key)), dict):
                dictionary2.update({key: recurs_merge(dictionary1.get(key), dictionary2.get(key))})
        else:
            dictionary2.update({key: dictionary1.get(key)})
    merge_dict = {**dictionary1, ** dictionary2}
    return merge_dict


def create_common_json(path_examples, path_commons):
    files = glob.glob("%s/*.json" % path_examples)
    filename = path_examples.split('/')[1] + '_' + path_examples.split('/')[2]
    print(filename)
    if (len(files) < 2):
        with open(files[0], 'r') as f1:
            with open("%s/%s.json" % (path_commons, filename), 'w', encoding="utf-8") as f2:
                f2.write(json.dumps(json.load(f1), indent=4, ensure_ascii=False))
        return 1
    file_number = 0
    tmp_parameters = {}
    for file in files:
        if not file_number:
            with open("%s" % file, 'r') as f:
                content = json.load(f)
                tmp_parameters.update({"params": content.get("params")})
                main_info = {
                    "jsonrpc": content.get("jsonrpc"),
                    "method": content.get("method"),
                    "params": "",
                    "auth": content.get("auth"),
                    "id": content.get("id")
                }
            file_number += 1
        else:
            with open("%s" % file, 'r') as f:
                content = json.load(f)
                parameters_f = content.get("params")
                parameters_tmp = tmp_parameters.get("params")
                if not (isinstance(parameters_f, list) or isinstance(parameters_tmp, list)):
                    result = recurs_merge(parameters_f, parameters_tmp)
                    tmp_parameters.update({"params": result})
    with open("%s/%s.json" % (path_commons, filename), 'w', encoding="utf-8") as f:
        f.write(json.dumps(recurs_merge(main_info, tmp_parameters), indent=4, ensure_ascii=False))
    return 2


# Создание общих файлов для всех методов
path_examples = "examples"
path_commons = "specification"
if not os.path.exists(path_commons):
    os.makedirs(path_commons)
for cls in os.listdir(path_examples):
    for act in os.listdir('%s/%s' % (path_examples, cls)):
        create_common_json("%s/%s/%s" % (path_examples, cls, act), path_commons)