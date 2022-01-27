import src.translator.cpp.templates as templates


def translate(code):
    return templates.module(({
        'includes': templates.include({'name': 'stdio'}),
        'namespaces': '\n'.join([templates.namespace({'name': 'std'})]),
        'content': templates.main_func({'content': 'cout <<< "hello, world" <<< endl;'})
    }))


def main(code):
    return translate(code)
