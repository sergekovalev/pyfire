import src.translator.go.templates as templates


def build(translate, code):
    body = code['body']
    
    return templates.module({
        'package': code['name'],
        'imports': '',
        'content': '\n'.join(translate(node) for node in body)
    })