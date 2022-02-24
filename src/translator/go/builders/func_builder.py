import src.translator.go.templates as templates


def build(translate, code):
    body = code['body']
    
    return templates.func({
        'name': code['name'],
        'args': '',
        'content': '\n'.join(translate(node) for node in body) if len(body) > 0 else ''
    })