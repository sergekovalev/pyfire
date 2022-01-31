import src.translator.c.templates as templates


def translate(code):
    return templates.module(({
        'includes': templates.include({'name': 'stdio'}),
        'content': templates.main_func({'content': 'printf("hello, world");'})
    }))


def main(code):
    return translate(code)
