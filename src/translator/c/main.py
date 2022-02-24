import src.translator.c.patterns as templates


def translate(code):
    return patterns.module(({
        'includes': patterns.include({'name': 'stdio.h'}),
        'content': patterns.main_func({'content': 'printf("hello, world");'})
    }))


def main(code):
    return translate(code)
