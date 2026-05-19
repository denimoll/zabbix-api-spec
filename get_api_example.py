import argparse
import os

import requests
import urllib3
from lxml import html

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_api_list(url):
    response = requests.get(url, verify=False)
    tree = html.fromstring(response.content)
    # Broad selector: all links whose text matches "class.method" pattern
    all_links = tree.xpath("//a/text()")
    result = []
    for m in all_links:
        m = m.strip()
        parts = m.split('.')
        if len(parts) == 2 and parts[0].isalpha() and parts[1].isalpha():
            result.append(m)
    return result


def get_api_example(url):
    response = requests.get(url, verify=False)
    tree = html.fromstring(response.content)
    # Try both layouts: pre wrapped in div (older docs) and direct pre sibling (7.2+)
    results = tree.xpath("//p/a[contains(text(), 'Request')]/parent::p/following-sibling::div[1]/pre")
    if not results:
        results = tree.xpath("//p/a[contains(text(), 'Request')]/parent::p/following-sibling::pre[1]")
    return results


def main():
    parser = argparse.ArgumentParser(description="Download Zabbix API examples from the official documentation")
    parser.add_argument("--version", default="7.0", help="Zabbix version (e.g. 7.0, 7.2)")
    parser.add_argument("--base-dir", default="versions", help="Base directory for output")
    args = parser.parse_args()

    url = "https://www.zabbix.com/documentation/%s/en/manual/api/reference" % args.version
    path = os.path.join(args.base_dir, args.version, "examples")
    os.makedirs(path, exist_ok=True)

    api_list = get_api_list(url)
    if not api_list:
        print("Warning: no API methods found. The page structure may have changed.")
        return

    for method in api_list:
        cls, act = method.split('.')
        folder = os.path.join(path, cls, act)
        os.makedirs(folder, exist_ok=True)
        path_to_api_doc = "%s/%s/%s" % (url, cls, act)
        examples = get_api_example(path_to_api_doc)
        for num, example in enumerate(examples):
            filename = os.path.join(folder, "%s.json" % num)
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(example.text_content())

    print("Done. Saved to: %s" % path)


if __name__ == "__main__":
    main()
