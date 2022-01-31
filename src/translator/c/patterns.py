MODULE = '''
{{ includes }}
{{ content }}
'''

INCLUDE = '''
    #include <{{ name }}>
'''

INCLUDE_H = '''
    #include "{{ name }}.h"
'''

MAIN_FUNC = '''
int main(int argc, char **argv) {
    {{ content }}
}
'''

FUNC = '''
{{ type }} {{ name }}({{ args }}) {
    {{ content }}
}
'''