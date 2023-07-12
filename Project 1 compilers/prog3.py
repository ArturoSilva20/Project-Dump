reservedWords={ "cin>>", "for", "int", "while"}

operator={ "+", "-", "*", "/", "++", "--"}

special={">", "=" , ";" , "(" , ")" , ">=" , ","}


def is_reserverd(str_input):
    for word in reservedWords:
        if str_input == word:
            return True
    return False
def is_operator(str_input):
    for word in operator:
        if str_input == word:
            return True
    return False
def is_special(str_input):
    for word in special:
        if str_input == word:
            return True
    return False

def print_type(str_input):
    if is_reserverd(str_input):
        return " reserved"
    elif is_operator(str_input):
        return " operator"
    elif is_special(str_input):
        return " special"
    elif str_input.isnumeric():
        return " number"
    else:
        return " other"


def main():
    input_str = input("enter statement")
    input_str = input_str.split()

    for word in input_str:
        print(word + print_type(word))



if __name__=="__main__":
    main()