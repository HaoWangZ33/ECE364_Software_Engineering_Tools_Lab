#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-10-25 11:04:10 -0400 (Tue, 25 Oct 2016) $
#$Revision: 95002 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab08/moduleTasks.py $
#$Id: moduleTasks.py 95002 2016-10-25 15:04:10Z ee364a07 $

import string

def isIdValid(pin):
    letters = string.ascii_letters
    digits = string.digits
    all_char = list(letters)
    all_char = all_char + (list(digits))
    all_char.append('_')
    in_char = list(pin)
    for item in in_char:
        if item not in all_char:
            return False
    return True

def parseAssignment(assignment):
    try:
        if assignment[0] == "." and assignment[-1] == ")":
            assign = assignment[1:]
            assign = assign.split('(')
            assign[1] = assign[1][:-1]
            if isIdValid(assign[0]) and isIdValid(assign[1]):
                return (assign[0], assign[1])
            else:
                raise ValueError(assignment)
        else:
            raise ValueError(assignment)
    except ValueError as e:
         raise ValueError(e)



def parseLine(line):
    newline = line.split(" ")
    while ("" in newline):
        newline.remove("")
    comp = newline[0]
    instance = newline[1]
    assign_list = ""
    for item in newline[2:]:
        assign_list = assign_list + item
    if isIdValid(comp) and isIdValid(instance) and assign_list != ("()" or ""):
        assign_list = assign_list[1:-1]
        assign_list = assign_list.split(",")
        tup1 = []
        try:
            for item in assign_list:
                result = parseAssignment(item)
                tup1.append(result)
        except ValueError as e:
            raise ValueError(e)
        else:
            tup1 = tuple(tup1)
            return (comp, instance, tup1)
    else:
        raise ValueError(line)


if __name__ == "__main__":
    print(isIdValid("asdfA12_.safdf"))
    print(parseAssignment(".A(packet_data0)"))
    print(parseLine("NAND2X1    U17    ( .A(serial_in), .B(n3), .Y(n10) )"))