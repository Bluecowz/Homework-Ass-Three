
# open file
file = open("students.txt", 'r')
out = open("out.txt", 'w')

# skip the first two lines becuase of header and empty line
lines = file.readlines()[2:]

out.write("FIRST NAME\tLAST NAME\tID\tHOMEWORK ADVERAGE\tEXAM AVERAGE\tFINAL COURSE ADVERAGE\n\n")


for l in lines:
    values = l.split()

    # get the first name
    first = values[0]
    # get the last name
    last = values[1]
    # get the student id
    sid = values[5]

    # grabbing homework values
    homework = values[8:15]

    # convert strings to nums
    for i in range(0, len(homework)):
        homework[i] = int(homework[i])

    # grabbing test values
    tests = values[-3:]
    
    # do it again
    for i in range(0, len(tests)):
        tests[i] = int(tests[i])

    h_avg = round(sum(homework)/len(homework), 2)
    t_avg = round(sum(tests)/len(tests), 2)
    c_avg = round(h_avg * 0.40 + t_avg * 0.60, 2)
    
    # there is one stupid name that is really long and I want everything to look pretty. Stupid Chancellor 
    one_annoying_name = "\t\t"

    if len(first) >= 10:
        one_annoying_name = "\t"

    out.write(f'{first}{one_annoying_name}{last}\t\t{sid}\t{h_avg}\t\t\t{t_avg}\t\t{c_avg}\n')
    
     

out.close()
file.close()
