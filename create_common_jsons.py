import argparse
import glob
import json
import os


def recurs_merge(dict1, dict2):
    result = dict(dict2)
    for key, val in dict1.items():
        if key in result and isinstance(val, dict) and isinstance(result[key], dict):
            result[key] = recurs_merge(val, result[key])
        elif key not in result:
            result[key] = val
    return result


def create_common_json(path_examples, path_commons):
    all_files = sorted(glob.glob(os.path.join(path_examples, "*.json")))
    if not all_files:
        print("No JSON files in %s, skipping" % path_examples)
        return 0

    parts = path_examples.replace("\\", "/").rstrip("/").split("/")
    # parts[-2] = class, parts[-1] = action
    filename = parts[-2] + "_" + parts[-1]
    print(filename)

    # Skip invalid JSON files
    files = []
    for f_path in all_files:
        try:
            with open(f_path, 'r', encoding="utf-8") as f:
                json.load(f)
            files.append(f_path)
        except json.JSONDecodeError as e:
            print("  Skipping invalid file %s: %s" % (f_path, e))

    if not files:
        print("  No valid JSON files in %s, skipping" % path_examples)
        return 0

    with open(files[0], 'r', encoding="utf-8") as f:
        first = json.load(f)

    if len(files) == 1:
        out = first
    else:
        # Build main_info from first file keys, excluding 'auth' (deprecated in 7.0+)
        main_info = {k: v for k, v in first.items() if k != "params"}
        tmp_params = first.get("params")

        for file in files[1:]:
            with open(file, 'r', encoding="utf-8") as f:
                content = json.load(f)
            params_f = content.get("params")
            if not isinstance(tmp_params, list) and not isinstance(params_f, list):
                tmp_params = recurs_merge(params_f, tmp_params)

        out = recurs_merge(main_info, {"params": tmp_params})

    out_path = os.path.join(path_commons, filename + ".json")
    with open(out_path, 'w', encoding="utf-8") as f:
        f.write(json.dumps(out, indent=4, ensure_ascii=False))
    return len(files)


def main():
    parser = argparse.ArgumentParser(description="Merge Zabbix API examples into combined specification JSONs")
    parser.add_argument("--version", default="7.0", help="Zabbix version (e.g. 7.0, 7.2)")
    parser.add_argument("--base-dir", default="versions", help="Base directory")
    args = parser.parse_args()

    path_examples = os.path.join(args.base_dir, args.version, "examples")
    path_commons = os.path.join(args.base_dir, args.version, "specification")

    if not os.path.exists(path_examples):
        print("Examples directory not found: %s" % path_examples)
        return

    os.makedirs(path_commons, exist_ok=True)

    for cls in sorted(os.listdir(path_examples)):
        cls_path = os.path.join(path_examples, cls)
        if not os.path.isdir(cls_path):
            continue
        for act in sorted(os.listdir(cls_path)):
            act_path = os.path.join(cls_path, act)
            if not os.path.isdir(act_path):
                continue
            create_common_json(act_path, path_commons)


if __name__ == "__main__":
    main()
