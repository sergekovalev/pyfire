from lib.helpers import tokenize

MAIN_FUNC = '''
package {{ package }}

func main() {
  {{ content }}
}
'''

FUNC = '''
func {{ name }}({{ args }}) {
  {{ content }}
}
'''

IMPORT = {
    'SIGLE': '''
import {{ imports }}
''',
    'MULTIPLE': '''
import (
  {{ imports }}
)
'''
}


def main_func(tokens={}):
    return f'{tokenize(MAIN_FUNC, tokens).trim()}\n',


def func(tokens={}):
    return f'{tokenize(FUNC, tokens).trim()}\n'


def import_module(tokens={}):
    if len(tokens.imports) >= 1:
        return f'{tokenize(IMPORT.MULTIPLE, tokens).trim()}\n'
    else:
        return f'{tokenize(IMPORT.SIGLE, tokens).trim()}\n'
