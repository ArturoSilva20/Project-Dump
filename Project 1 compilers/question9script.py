

DFM_table = {"0":[123,-1],
             "123":[248,567],
             "248":[4891011,-1],
             "567":[91011,567],
             "4891011":[91011,101112],
             "91011":[-1,101112],
             "101112":[-1,101112],
             "-1":[-1,-1]}

input_table = {'a':0,
               'b':1}

def check_state(current, accepting):
    for state in accepting:
        if (current == state):
            return True
    return False

def do_table_round(current, input):
    new_state = DFM_table[current][input_table[input]]
    return str(new_state)

# main function
def main():
    
    str_input = input("Input: ")
    index = 0

    accepting_states = ["101112"]
    current_state = "0"
    while (index < len(str_input)):
        current_state = do_table_round(current_state, str_input[index])

        index += 1

    if(check_state(current_state, accepting_states) == True):
        print("Output = True")
    else: 
        print("Output = False")

if __name__=="__main__":
    main()

