#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-10-25 11:04:10 -0400 (Tue, 25 Oct 2016) $
#$Revision: 95002 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab08/hardwareMapper.py $
#$Id: hardwareMapper.py 95002 2016-10-25 15:04:10Z ee364a07 $

import moduleTasks

def mapHardwareLine(line):
    try:
        newline = moduleTasks.parseLine(line)
        print(newline)
    except ValueError:
        return "Error: Bad Line."
    else:
        result = newline[1] + ": " + newline[0] + " PORT MAP("
        for assignment in newline[2]:
            result = result + assignment[0] + "=>" + assignment[1] + ", "
        result = result[:-2] + ");"
        return result


def mapFile(sourceFile, targetFile):
    with open (sourceFile, "r") as input:
        all_line = input.readlines()
    for i in range(len(all_line)):
        all_line[i] = all_line[i][:-1]
        while (all_line[i][0] == " "):
            all_line[i] = all_line[i][1:]
    count = len(all_line)
    count1 = 1
    with open (targetFile, "w") as output:
        for line in all_line:
            newline = mapHardwareLine(line)
            output.write(newline)
            if count1 < count:
                output.write("\n")
            count1 = count1 + 1


if __name__ == "__main__":
    print(mapHardwareLine("OAI22X1 U2 ( .A(n28), .B(n32), .C(n3), .D(n31), .Y(n15) )"))
    mapFile("verilog_test.v", "output.vhdl")