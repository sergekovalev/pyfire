def translate(code):
    return code


def main(code):
    try:
        return translate(code)
    except Exception:
        print(Exception)
        exit()
