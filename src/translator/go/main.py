import src.translator.go.templates as templates


def translate(code):
    return templates.main_func({'package': 'main', 'content': 'println("hi")'})


def main(code):
    try:
        return translate(code)
    except Exception:
        print(Exception)
        exit()
