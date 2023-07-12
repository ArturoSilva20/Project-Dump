
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

LR_parse_table = {
                0:{
                    'i': 'S5',
                    '(': 'S4',
                    'E': 1,
                    'T': 2,
                    'F': 3
                },
                1:{
                    '+': 'S6',
                    '-': 'S7',
                    '$': 'acc'
                },
                2:{
                    '+': 'R3',
                    '-': 'R3',
                    '*': 'S8',
                    '/': 'S9',
                    ')': 'R3',
                    '$': 'R3'
                },
                3:{
                    '+': 'R6',
                    '-': 'R6',
                    '*': 'R6',
                    '/': 'R6',
                    ')': 'R6',
                    '$': 'R6'
                },
                4:{
                    'i': 'S5',
                    '(': 'S4',
                    'E': 10,
                    'T': 2,
                    'F': 3
                },
                5:{
                    '+': 'R8',
                    '-': 'R8',
                    '*': 'R8',
                    '/': 'R8',
                    ')': 'R8',
                    '$': 'R8'
                },
                6:{
                    'i': 'S5',
                    '(': 'S4',
                    'T': 11,
                    'F': 3
                },
                7:{
                    'i': 'S5',
                    '(': 'S4',
                    'T': 12,
                    'F': 3
                },
                8:{
                    'i': 'S5',
                    '(': 'S4',
                    'F': 13
                },
                9:{
                    'i': 'S5',
                    '(': 'S4',
                    'F': 14
                },
                10:{
                    '+': 'S6',
                    '-': 'S7',
                    ')': 'S15'
                },
                11:{
                    '+': 'R1',
                    '-': 'R1',
                    '*': 'S8',
                    '/': 'S9',
                    ')': 'R1',
                    '$': 'R1'
                },
                12:{
                    '+': 'R2',
                    '-': 'R2',
                    '*': 'S8',
                    '/': 'S9',
                    ')': 'R2',
                    '$': 'R2'
                },
                13:{
                    '+': 'R4',
                    '-': 'R4',
                    '*': 'R4',
                    '/': 'R4',
                    ')': 'R4',
                    '$': 'R4'
                },
                14:{
                    '+': 'R5',
                    '-': 'R5',
                    '*': 'R5',
                    '/': 'R5',
                    ')': 'R5',
                    '$': 'R5'
                },
                15:{
                    '+': 'R7',
                    '-': 'R7',
                    '*': 'R7',
                    '/': 'R7',
                    ')': 'R7',
                    '$': 'R7'
                }
}

Productions = {
                1: ,
                2,
                3,
                4,
                5,
                6,
                7,
                8
}

def LR_parse_table(table, input_str):
    if input_str[-1] != '$':
        input_str.append('$')

    i = 0
    stack = [0]
    try:
        Table_entry = table[stack[-1]][input_str[i]]
    except KeyError:
        print("incorrect table entry")
        return False
    if Table_entry[0] == 'S':
        stack.append(input_str[i])
        i += 1
        stack.append(Table_entry[1])
    elif Table_entry[0]== 'R':
        pass

    while(Table_entry != 'acc'):
        pass
    pass


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