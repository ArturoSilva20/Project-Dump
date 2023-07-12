
predictive_parsing_table = {'E': {
                                'a': ['T','Q'],
                                '(': ['T','Q']
                            },
                            'Q': {
                                '+': ['+','T','Q'],
                                '-': ['-','T','Q'],
                                ')': ['ε'],
                                '$': ['ε']
                            },
                            'T': {
                                'a': ['F','R'],
                                '(': ['F','R']
                            },
                            'R': {
                                '+' : ['ε'],
                                '-' : ['ε'],
                                '*' : ['*', 'F', 'R'],
                                '/' : ['/', 'F', 'R'],
                                ')' : ['ε'],
                                '$' : ['ε']
                            },
                            'F': {
                                'a' : ['a'],
                                '(' : ['(', 'E', ')']
                            }
}


def parse_table(table, input_str):
    stack = ['$']
    stack.append('E')
    i = 0
    while(len(stack) > 0):
        if stack[-1] == input_str[i]:
            stack.pop()
            i += 1
        else:
            try:
                production = table[stack[-1]][ input_str[i]]
                stack.pop()
                for symbol in reversed(production):
                    if symbol != 'ε':
                        stack.append(symbol)
            except KeyError:
                # If no production rule is found, report an error
                print(f"Stack: {stack}  Input: {input_str[i:]}  Action: error")
                return False
    return True 

def main():
    input_str = input("Input string: ")
    if parse_table(predictive_parsing_table, input_str + '$'):
        print("Accepted")
    else:
        print("Rejected")

if __name__=="__main__":
    main()