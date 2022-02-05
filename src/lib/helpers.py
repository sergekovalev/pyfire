from src.lib.settings import Settings
import os
import re


def import_module(path):
    with open(path, 'r') as f:
        file = f.read()
    
    if file[len(file) - 1] != '\n':
        file += '\n'
    
    return file


def log(path='', folder='', content=''):
    if folder:
        new_folder = ''
        for f in folder.split('/'):
            new_folder = f'{new_folder}/{f}'
            os.mkdir(f'{Settings().ROOT_DIR}/__dist__{new_folder}')
    
    with open(f'{Settings().ROOT_DIR}/__dist__/{folder + "/"}{path}', 'w') as f:
        f.write(content)


def cp(infile, outfile):
    with open(infile, 'r') as file_from:
        with open(outfile, 'w') as file_to:
            file_to.write(file_from.read())


def tokenize(text, tokens):
    new_text = text
    
    for k, v in tokens.items():
        new_text = re.sub(f'{{{{ {k} }}}}', v, new_text)
    
    return new_text


class Empty(object):
    def set_attr(self, key, value):
        self.__dict__[key] = value


def objectify(json_data):
    new_obj = Empty()

    for key in json_data.keys():
        value = json_data[key]

        new_obj.set_attr(key, objectify(
            value) if type(value) is dict else value)

    return new_obj


def find_in_list(lst, fn):
    filtered = list(filter(fn, lst))

    return filtered[0] if len(filtered) > 0 else None