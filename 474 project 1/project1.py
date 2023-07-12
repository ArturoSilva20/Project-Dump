"""Problem: Given a simple instruction and a block of n instructions (n < 11), identify which instructions in
the block can be executed in parallel to the simple instruction
"""


def i_inputs(in_str):
    """#gets instruction string and returns a string of input variables"""
    out_str = []
    elements = in_str.split(' ')
    for element in elements:
        if element.isalpha():
            out_str.append(element)
    out_str.pop(0)
    return out_str

def i_output(in_str):
    """#returns output"""
    output = in_str[0]
    return output

def is_parallel(instruction1, instruction2):
    """#returns true if both instructions can be parallel"""
    inputs1 = i_inputs(instruction1)
    output2 = i_output(instruction2)
    for input_x in inputs1:
        if input_x in output2:
            return False

    inputs2 = i_inputs(instruction2)
    output1 = i_output(instruction1)
    for input_x in inputs2:
        if input_x in output1:
            return False
    return True

def alg_calculate(instruction, block):
    """returns which instruction in the block can be parallel to the given instruction 
        block is list on instructions. instructions are strings with elements eparated by space"""
    output = []
    for instruction_x in block:
        if is_parallel(instruction, instruction_x):
            output.append(instruction_x)

    return output

def alg_verify(block):
    """returns the pair of instructions that can be executed in parallel"""
    output = []
    for i in range(0,len(block)):
        for j in range(0,len(block)):
            if (i != j):
                if is_parallel(block[i], block[j]):
                    if ((not(block[i] in output)) and (not(block[j] in output))):
                        output.append(block[i])
                        output.append(block[j])
    return output


def main():
    """main function for testing algorithms"""
    input_instruction = "d = b + ( c - d / e )"
    input_block = ["b = b * c", "c = c - a", "a = a + b * c"]

    output = alg_calculate(input_instruction, input_block)

    print(output)

    input_block2 = ["b = b * c", "d = c – a", "a = a + b * c"]
    output2 = alg_verify(input_block2)
    print(output2)

    input_block3 = ["a = a * b * c", "c = c – a", "a = a + b * c"]
    output3 = alg_verify(input_block3)
    print(output3)

if __name__ == "__main__":
    main()
