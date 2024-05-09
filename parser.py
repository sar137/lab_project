import re
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


class Parser:
    def __init__(self, input_tokens):
        self.input_tokens = input_tokens
        self.current_token = None
        self.index = 0

    def parse(self):
        self.advance()
        return self.expression()

    def advance(self):
        if self.index < len(self.input_tokens):
            self.current_token = self.input_tokens[self.index]
            self.index += 1
        else:
            self.current_token = None

    def match(self, token_type):
        if self.current_token and self.current_token[0] == token_type:
            self.advance()
        else:
            raise SyntaxError("Unexpected token: {}".format(self.current_token))

    def expression(self):
        term_value = self.term()
        while self.current_token and self.current_token[0] == 'Op' and self.current_token[1] in ('+', '-'):
            operator = self.current_token[1]
            self.match('Op')
            term_value = ('BinaryOp', operator, term_value, self.term())
        return term_value

    def term(self):
        factor_value = self.factor()
        while self.current_token and self.current_token[0] == 'Op' and self.current_token[1] in ('*', '/'):
            operator = self.current_token[1]
            self.match('Op')
            factor_value = ('BinaryOp', operator, factor_value, self.factor())
        return factor_value

    def factor(self):
        primary_value = self.primary()
        if self.current_token and self.current_token[0] == 'ExpOp' and self.current_token[1] == '^':
            self.match('ExpOp')
            return ('Exponentiation', primary_value, self.factor())
        return primary_value

    def primary(self):
        if self.current_token and self.current_token[0] == 'Variable':
            var_name = self.current_token[1]
            self.match('Variable')
            return ('Variable', var_name)
        elif self.current_token and self.current_token[0] == 'Number':
            number_value = float(self.current_token[1])
            self.match('Number')
            return ('Number', number_value)
        elif self.current_token and self.current_token[0] == 'LeftParen':
            self.match('LeftParen')
            expr_value = self.expression()
            self.match('RightParen')
            return expr_value
        else:
            raise SyntaxError("Unexpected token: {}".format(self.current_token))


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
