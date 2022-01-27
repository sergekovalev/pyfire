from src.lib.helpers import tokenize
from src.translator.go.patterns import MODULE, MAIN_FUNC, FUNC, IMPORT


def module(tokens={}):
    return f'{tokenize(MODULE, tokens).strip()}\n'


def main_func(tokens={}):
    return f'{tokenize(MAIN_FUNC, tokens).strip()}\n'


def func(tokens={}):
    return f'{tokenize(FUNC, tokens).strip()}\n'


def import_module(tokens={}):
    if len(tokens.imports) >= 1:
        return f'{tokenize(IMPORT.MULTIPLE, tokens).strip()}\n'
    else:
        return f'{tokenize(IMPORT.SIGLE, tokens).strip()}\n'
