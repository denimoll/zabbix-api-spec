import os

import requests
import urllib3
from lxml import html

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_api_list(url):
    response = requests.get(url, verify=False)
    tree = html.fromstring(response.content)
    api_list_from_tree = tree.xpath("/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[33]/div[2]//a/text()")
    api_list = []
    for method in api_list_from_tree:
        if len(method.split('.')) != 1:
            api_list.append(method)
    return api_list

def get_api_example(url):
    response = requests.get(url, verify=False)
    tree = html.fromstring(response.content)
    print(str(response).find("Request:"))
    return tree.xpath("//p[contains(text(), 'Request:')]/following-sibling::div[1]/pre") # может меняться путь


# Основная часть программы
zabbix_version = "6.0"
url = "https://www.zabbix.com/documentation/%s/en/manual/api/reference" % zabbix_version
path = "examples"
if not os.path.exists(path):
    os.makedirs(path)

for method in get_api_list(url):
    cls = method.split('.')[0]
    act = method.split('.')[1]
    folder = "%s/%s/%s" % (path, cls, act)
    if not os.path.exists(folder):
        os.makedirs(folder)
    path_to_api_doc = "%s/%s/%s" % (url, cls, act)
    for num, example in enumerate(get_api_example(path_to_api_doc)):
        filename = "%s/%s.json" % (folder, num)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(example.text_content())
