def remove_comment(str_input):
    out_string = []
    
    str_input = str_input.split()
    for word in str_input:
        if word[:2] == '//':
            break
        else:
            out_string.append(word)

    out_string = " ".join(out_string)
    return out_string

def fix_line(str_input):
    str_out = " ".join(str_input.split())

    str_out = remove_comment(str_out)

    str_out = str_out + '\n'
    return str_out



def main():
    inputfile = "file.txt"
    outputfile = "clean.txt"
    outfile = open(outputfile, 'w')
    infile = open(inputfile, 'r')


    for line in infile.readlines():
        if (line[:2] == '//'):
            pass
        elif(line == '\n'):
            pass
        else:
            line = fix_line(line)
            outfile.write(str(line))

    outfile.close()
    infile.close()
    print("finished")

if __name__=="__main__":
    main()
