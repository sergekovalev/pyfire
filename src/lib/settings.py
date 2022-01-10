import json
from setuptools import setup, find_packages
import argparse

setup(name='pyfire', version='1.0', packages=find_packages())


def init(root_dir):
    global CONFIG
    global ROOT_DIR

    ROOT_DIR = root_dir

    with open('./config.json', 'r') as file:
        CONFIG = json.loads(file.read())

    parser = argparse.ArgumentParser()

    parser.add_argument('file', metavar='F', type=str, help='file name')
    
    return parser.parse_args()