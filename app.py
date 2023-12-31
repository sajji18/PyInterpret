# An Interpreter with rules:
f'''The only arithmetic operation supported at the moment is addition, subtraction
whitespace characters are allowed anywhere in the input. Ex -> 23  +     434-12 is valid input.'''

# Token types, A token is an object that has a type and a value
INTEGER, WHITESPACE, PLUS, MINUS, EOF = 'INTEGER', 'WHITESPACE', 'PLUS', 'MINUS', 'EOF'

class Token:
    # constructor
    def __init__(self, type, value):
        self.type = type # type -> int, plus, minum, eof
        self.value = value # the value -> int, '+', '-', none
        
    def __str__(self):
        # string representation of class instance
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )
        
    def __repr__(self):
        # representation that can be used to recreate the object
        return self.__str__()
    
    
# We will take text input from the user, and then advance the position one by one to check tokens and perform operation accordingly 
class Interpreter:
    # constructor
    def __init__(self, text):
        self.text = text # text input from user
        self.position = 0 # position of current character in consideration
        
        self.current_token = None # current token corresponding to current character
        self.current_char = self.text[self.position] # current character under consideration
        
    def error(self):
        raise Exception('Error parsing input')
     
    def advance(self):
        self.position += 1 # move pos by 1 and assign current char
        
        if self.position > len(self.text) - 1: # text input ended, character is none
            self.current_char = None
            
        else: # track the character otherwise
            self.current_char = self.text[self.position]
            
    def skip_white_spaces(self):
        if self.position < len(self.text):
            if self.current_char.isspace():
                self.advance()
    
    # Break a sentence into token, one at a time
    def get_next_token(self):
        if self.position > len(self.text) - 1: # If No more input left to convert into token
            return Token(EOF, None)
        
        current_char = self.text[self.position]
        
        if current_char.isdigit(): # if current char is recognized, then store token and advance pos by 1
            token = Token(INTEGER, int(current_char))
            self.advance()
            return token

        elif current_char == '+':
            token = Token(PLUS, current_char)
            self.advance()
            return token
        
        elif current_char == '-':
            token = Token(MINUS, current_char)
            self.advance()
            return token
        
        elif current_char == ' ':
            token = Token(WHITESPACE, current_char)
            self.advance()
            return token
        else:
            self.error()
        
    def eat(self, token_type):
        if self.current_token.type == token_type: # check if current token type == passed token type, get next token
            self.current_token = self.get_next_token() 
            
        else:
            self.error()
    
    # Handles Addition and Subtraction
    def operation(self):
        str_buffer, result, is_add_operator = '', 0, True  # Initialize is_add_operator to True
        
        while self.position < len(self.text):
            char = self.text[self.position]
            self.position += 1
            
            if char == ' ':
                continue
            
            if char.isdigit():
                str_buffer += char
                
                # Handle multi-digit numbers
                while self.position < len(self.text) and self.text[self.position].isdigit():
                    str_buffer += self.text[self.position]
                    self.position += 1
            
            elif char == '+':
                if not is_add_operator:
                    result -= int(str_buffer)
                else:
                    result += int(str_buffer)
                str_buffer = ''
                is_add_operator = True
                
            elif char == '-':
                if not is_add_operator:
                    result -= int(str_buffer)
                else:
                    result += int(str_buffer)
                str_buffer = ''
                is_add_operator = False
                
        # Handle the last number in the sequence
        if str_buffer:
            if is_add_operator:
                result += int(str_buffer)
            else:
                result -= int(str_buffer)
            
        return result
            
    
def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.operation()
        print(result)


if __name__ == '__main__':
    main() 
    