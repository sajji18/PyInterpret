def arithmetic_operation(self):
    # initially current token is none, so get hold of first char and token
    self.current_token = self.get_next_token()

    # Expecting the first(leftmost) char to be an integer
    left = self.current_token
    self.eat(left.type)
    
    # Middle char is expected to be an operator
    op = self.current_token
    self.eat(op.type)
        
    # Right char is again expected to be integer
    right = self.current_token
    self.eat(right.type)
    
    if op.type == 'PLUS':
        result = left.value + right.value
        return result
        
    elif op.type == 'MINUS':
        result = left.value - right.value
        return result
    
    self.error()
    
def arithmetic_operation(self):
    # initially current token is none, so get hold of first char and token
    # self.current_token = self.get_next_token()
    
    numbers = []
    plus_operator = True
    number_string = ''
    
    # input -> '33 + 45'
    for char in self.text:
        self.current_token = self.get_next_token()
        
        if self.current_token.type == 'WHITESPACE':
            continue
        
        if self.current_token.type == 'INTEGER':
            number_string += str(self.current_token.value)
        
        if(self.current_token.type != 'INTEGER'):
            numbers.append(int(number_string))
            number_string = ''
            if(self.current_token.type == 'MINUS'):
                plus_operator = False
            
        self.eat(self.current_token.type)
    
    # Append the last number after the loop
    numbers.append(int(number_string))
        
    if plus_operator == False:
        return numbers[0] - numbers[1]
    else:
        return numbers[0] + numbers[1]
    
# Attempting operation function

def operation(self):
    str, flag, result, is_add_operator = '', 0, 0, False
    
    for char in self.text:
        if char == '+':
            is_add_operator = False
            break
        elif char == '-':
            is_add_operator = True
            break
        
    while self.current_token.type != 'EOF':
        self.current_token = self.get_next_token()
        
        if self.current_token.type == 'WHITESPACE':
            if flag == 0:
                pass
            elif flag == 1:
                result += int(str)
        
        elif self.current_token.type == 'INTEGER':
            flag = 1
            str += '{self.current_token.value}'
        
        elif self.current_token.type == 'PLUS' and is_add_operator == True:
            is_add_operator = False
            result += int(str)
            str = ''
            
        elif self.current_token.type == 'MINUS' and is_add_operator == False:
            is_add_operator = True
            result -= int(str)
            str = '' 