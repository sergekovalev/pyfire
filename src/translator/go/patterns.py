MODULE = '''
{{ includes }}

{{ content }}
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
