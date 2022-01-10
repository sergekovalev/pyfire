import json


def init(root_dir):
    global CONFIG
    global ROOT_DIR

    ROOT_DIR = root_dir

    with open('./config.json', 'r') as file:
        CONFIG = json.loads(file.read())