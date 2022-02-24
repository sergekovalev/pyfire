import src.translator.go.templates as templates


def build(translate, code):
    body = code['body']
    
    expr = f'{code["var_name"]} := {body[0]["value"]}'
    
    return expr