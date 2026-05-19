import argparse
import glob
import json
import os
import sys


def json_validation(file):
    try:
        with open(file, 'r') as f:
            json.load(f)
        return True
    except Exception as e:
        print('Невалидный json-файл %s, ошибка: %s' % (file, e))
        return False


def main():
    parser = argparse.ArgumentParser(description="Validate Zabbix API example JSON files")
    parser.add_argument("--version", default="7.0", help="Zabbix version (e.g. 7.0, 7.2)")
    parser.add_argument("--base-dir", default="versions", help="Base directory")
    args = parser.parse_args()

    path_examples = os.path.join(args.base_dir, args.version, "examples")
    if not os.path.exists(path_examples):
        print("Examples directory not found: %s" % path_examples)
        sys.exit(1)

    total = 0
    errors = 0
    for cls in sorted(os.listdir(path_examples)):
        cls_path = os.path.join(path_examples, cls)
        if not os.path.isdir(cls_path):
            continue
        for act in sorted(os.listdir(cls_path)):
            act_path = os.path.join(cls_path, act)
            if not os.path.isdir(act_path):
                continue
            for file in sorted(glob.glob(os.path.join(act_path, "*.json"))):
                total += 1
                if not json_validation(file):
                    errors += 1

    print("\nИтого: %d файлов, %d ошибок" % (total, errors))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
