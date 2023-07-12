
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

# E' -> R
# T' -> Y
predictive_parsing_table_2 = {
                            'S':{
                                'a':['F', '=', 'E'],
                                'b':['F', '=', 'E'],
                                '(':['F', '=', 'E'],
                            },
                            'E':{
                                'a': ['T', 'R'],
                                'b': ['T', 'R'],
                                '(': ['T', 'R']
                            },
                            'R':{
                                '+': ['+', 'T', 'R'],
                                '-': ['-', 'T', 'R'],
                                ')': ['ε'],
                                '$': ['ε']
                            },
                            'T':{
                                'a': ['F', 'Y'],
                                'b': ['F', 'Y'],
                                '(': ['F', 'Y']
                            },
                            'Y':{
                                '*': ['*', 'F', 'Y'],
                                '/': ['/', 'F', 'Y'],
                                '+': ['ε'],
                                '-': ['ε'],
                                ')': ['ε'],
                                '$': ['ε']

                            },
                            'F':{
                                'a': ['a'],
                                'b': ['b'],
                                '(': ['(', 'E', ')']
                            }
}

def parse_table(table, input_str, start):
    stack = ['$']
    stack.append(start)
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
                print("No Rule found")
                return False
    return True 

def main():
    input_str = input("Input string: ")
    if parse_table(predictive_parsing_table, input_str, 'S'):
        print("Accepted")
    else:
        print("Rejected")

if __name__=="__main__":
    main()