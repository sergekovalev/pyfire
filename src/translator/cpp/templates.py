from src.lib.helpers import tokenize
from src.translator.cpp.patterns import MODULE, INCLUDE, NAMESPACE, INCLUDE_H, MAIN_FUNC, FUNC


def module(tokens={}):
    return f'{tokenize(MODULE, tokens).strip()}\n'


def include(tokens={}):
    return f'{tokenize(INCLUDE, tokens).strip()}\n'


def namespace(tokens={}):
    return f'{tokenize(NAMESPACE, tokens).strip()}\n'


def include_h(tokens={}):
    return f'{tokenize(INCLUDE_H, tokens).strip()}\n'


def main_func(tokens={}):
    return f'{tokenize(MAIN_FUNC, tokens).strip()}\n'


def func(tokens={}):
    return f'{tokenize(FUNC, tokens).strip()}\n'
