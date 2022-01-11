from src.parser.python.tokenizer import tokenize

parsed_code = []

concat_pairs = [
    [ord('='), ord('=')],
    [ord('>'), ord('=')],
    [ord('<'), ord('=')],
    [ord('-'), ord('>')]
]


def is_space(char_code):
    return char_code == 10 or char_code == 32


def is_endl(char_code):
    return char_code == 10


def is_sign(char_code):
    return not ((65 <= char_code <= 90) or (97 <= char_code <= 122))


def is_number(char_code):
    return 47 < char_code < 58


def can_concat(char_code, previous_char_code):
    for pair in concat_pairs:
        if pair[0] == previous_char_code and pair[1] == char_code:
            return True
    
    return False


def push(ch, char_code, previous_char_code):
    if ch:
        if can_concat(char_code, previous_char_code):
            parsed_code[-1] += ch
        else:
            parsed_code.append(ch)


def parse(code):
    word = ''
    previous_char_code = None
    lines_count = 0
    
    for ch in code:
        char_code = ord(ch)
        
        if is_sign(char_code) and not is_number(char_code):
            push(word, char_code, previous_char_code)
            word = ''
            
            if not is_space(char_code):
                push(ch, char_code, previous_char_code)
            
            if is_endl(char_code):
                lines_count += 1
                
                if not is_endl(previous_char_code) and char_code != 59:
                    push(';', char_code, previous_char_code)
        else:
            word += ch
        
        previous_char_code = char_code
    
    return {
        'lines': lines_count,
        'code': parsed_code,
        'tokens': tokenize(parsed_code)
    }


def main(code):
    return {
        'start': 0,
        'end': len(code),
        **parse(code)
    }
