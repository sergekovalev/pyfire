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
int main(int argc, char **argv)
{
    {{ content }}
}
'''

VAR_DECLARATION = '''
{{ type }} {{ name }};
'''

FUNC = '''
{{ type }} {{ name }}({{ args }})
{
    {{ content }}
}
'''

STRUCT = '''
struct {{ name }}
{
    {{ content }}
};
'''

STRUCT_WITH_VARIABLES = '''
struct {{ name }}
{
    {{ content }}
} {{ variables }};
'''

STRUCT_FIELD = '''
{{ type }} {{ name }};
'''

IF_CONDITION = '''
if({{ condition }})
{
    {{ content }}
}
'''

FOR_LOOP = '''
for({{ var_type }} {{ var_name }} = {{ from_value }}; {{ var_name }} {{ cmp_op }} {{ to_value }}; {{ var_name }}{{ upd_op }})
{
    {{ content }}
}
'''

WHILE_LOOP = '''
while({{ cmp_var }} {{ cmp_op }} {{ cmp_value }})
{
    {{ content }}
}
'''