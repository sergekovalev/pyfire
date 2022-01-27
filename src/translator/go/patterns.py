MODULE = '''
package {{ package }}
{{ imports }}
{{ content }}
'''

IMPORT = {
    'SIGLE': '''
import {{ import }}
''',
    'MULTIPLE': '''
import (
  {{ imports }}
)
'''
}

MAIN_FUNC = '''
func main() {
  {{ content }}
}
'''

FUNC = '''
func {{ name }}({{ args }}) {
  {{ content }}
}
'''
