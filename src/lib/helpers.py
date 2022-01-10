import settings
import os


def import_module(path):
    with open(path, 'r') as f:
        file = f.read()
    
    if file[file.length - 1] != '\n':
        file += '\n'
    
    return file


def log(path='', folder='', content=''):
    if folder:
        os.mkdir(f'{settings.ROOT_DIR}/__dist__/{folder}')
    
    with open(f'{settings.ROOT_DIR}/__dist__/{folder + "/"}{path}') as f:
        f.write(content)


def tokenize(text, tokens):
    # Object.keys(tokens).forEach(key= > text = text.replace(new RegExp(`{{?${key} ?}}`, 'gi'), tokens[key]));
    
    return text


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