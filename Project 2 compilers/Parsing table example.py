# Parsing table
table = {
    ('E', 'a'): ['T', 'Q'],
    ('E', '('): ['T', 'Q'],
    ('Q', '+'): ['+', 'T', 'Q'],
    ('Q', '-'): ['-', 'T', 'Q'],
    ('Q', ')'): ['ε'],
    ('Q', '$'): ['ε'],
    ('T', 'a'): ['F', 'R'],
    ('T', '('): ['F', 'R'],
    ('R', '+'): ['ε'],
    ('R', '-'): ['ε'],
    ('R', '*'): ['*', 'F', 'R'],
    ('R', '/'): ['/', 'F', 'R'],
    ('R', ')'): ['ε'],
    ('R', '$'): ['ε'],
    ('F', 'a'): ['a'],
    ('F', '('): ['(', 'E', ')']
}

# Stack
stack = ['$']

# User input
input_str = input('Enter the input string: ')

# Parsing function
def parse(input_str):
    # Initialize stack with start symbol
    stack.append('E')
    # Initialize input string index
    i = 0
    # Process the stack until it is empty
    while len(stack) > 0:
        # Get the top element of the stack
        top = stack[-1]
        # If the top matches the current input character, consume the input
        if top == input_str[i]:
            print(f"Stack: {stack}  Input: {input_str[i:]}  Action: match {top}")
            stack.pop()
            i += 1
        # If the top is a terminal but doesn't match the input, report an error
        elif top in ('a', '+', '-', '*', '/', '(', ')', '$'):
            print(f"Stack: {stack}  Input: {input_str[i:]}  Action: error")
            return False
        # If the top is a non-terminal, use a production rule to replace it
        else:
            try:
                # Look up production rule in parsing table
                production = table[(top, input_str[i])]
                print(f"Stack: {stack}  Input: {input_str[i:]}  Action: {top} -> {''.join(production)}")
                # Replace the non-terminal with symbols from the production rule
                stack.pop()
                for symbol in reversed(production):
                    if symbol != 'ε':
                        stack.append(symbol)
            except KeyError:
                # If no production rule is found, report an error
                print(f"Stack: {stack}  Input: {input_str[i:]}  Action: error")
                return False
    # If the stack is empty, the input string is accepted
    return True

# Call the parsing function with the input string and end-of-string symbol
if parse(input_str + '$'):
    print("Accepted")
else:
    print("Rejected")