def tokenize_input(input_string):
    # Define regex patterns for each token type
    patterns = [
        (r'\+', 'Op'),
        (r'-', 'Op'),
        (r'\*', 'Op'),
        (r'/', 'Op'),
        (r'\^', 'Op'),
        (r'=', 'AssignOp'),
        (r';', 'Semicolon'),
        (r'User\s+In:', 'UserInput'),
        (r'Print:', 'Print'),
        (r'EXIT', 'ExitCommand'),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'Variable'),
        (r'\d+(\.\d*)?', 'Number'),
        (r'\(', 'LeftParen'),
        (r'\)', 'RightParen'),
        (r'\s+', 'Whitespace')
    ]

    tokens = []
    input_string = input_string.strip()
    line_number = 1

    while input_string:
        match = None
        for pattern, token_type in patterns:
            regex_match = re.match(pattern, input_string)
            if regex_match:
                match = (token_type, regex_match.group(0), line_number)
                input_string = input_string[regex_match.end():].strip()
                if token_type == 'UserInput' or token_type == 'Print':
                    line_number += 1
                break
        if not match:
            raise ValueError("Invalid token at line {}: '{}'".format(line_number, input_string))
        if match[1] != 'Whitespace':
            tokens.append(match)

    return tokens


# Example usage:
input_string = input("Enter an expression: ")

try:
    input_tokens = tokenize_input(input_string)
    for token_type, token_value, line_number in input_tokens:
        print("Token Value:", token_value)

    parser = Parser(input_tokens)
    result = parser.parse()
    print("Parse Result:", result)

except ValueError as e:
    print("Error:", e)
