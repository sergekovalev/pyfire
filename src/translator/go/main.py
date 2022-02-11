import src.translator.go.templates as templates
import src.parser.tokens as TOKENS


def build_module(code):
    body = code['body']
    
    return templates.module({
        'package': code['name'],
        'imports': '',
        'content': '\n'.join(translate(node) for node in body)
    })


def build_func_declaration(code):
    body = code['body']
    
    return templates.func({
        'name': code['name'],
        'args': '',
        'content': '\n'.join(translate(node) for node in body) if len(body) > 0 else ''
    })


def translate(code):
    if code['type'] == TOKENS.MODULE:
        return build_module(code)
    elif code['type'] == TOKENS.FUNCTION_DECLARATION:
        return build_func_declaration(code)
    
    return ''


def main(code):
    return translate(code)
