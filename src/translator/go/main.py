import src.parser.tokens as TOKENS

from src.translator.go.builders.module_builder import build as build_module
from src.translator.go.builders.func_builder import build as build_func
from src.translator.go.builders.expr_builder import build as build_expr


def translate(code):
    if code['type'] == TOKENS.MODULE:
        return build_module(translate, code)
    elif code['type'] == TOKENS.FUNCTION_DECLARATION:
        return build_func(translate, code)
    elif code['type'] == TOKENS.EXPRESSION:
        return build_expr(translate, code)
    
    return ''


def main(code):
    return translate(code)
