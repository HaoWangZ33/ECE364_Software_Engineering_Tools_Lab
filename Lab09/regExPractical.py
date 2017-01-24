#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-11-01 11:14:06 -0400 (Tue, 01 Nov 2016) $
#$Revision: 95211 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab09/regExPractical.py $
#$Id: regExPractical.py 95211 2016-11-01 15:14:06Z ee364a07 $

import re

def getFloatData(sensorID):
    with open ("sensors.xml", "r") as input:
        all_line = input.read()
        expr = r"<sensors>(.*?)</sensors>"
        new = re.findall(expr, all_line, re.DOTALL)
        expr = r"<[\w]*>(.*?)<[/\w]*>"
        sensors = re.findall(expr, new[0], re.DOTALL)
        #print(sensors)

def getScientificData(sensorID):
    pass

def getOptions(commandline):
    result = []
    expr = r"-[a-z].*"
    new = re.findall(expr, commandline, re.DOTALL)
    newstr = new[0].split("-")
    while ("" in newstr):
        newstr.remove("")
    for item in newstr:
        newitem = item.split(" ")
        while ("" in newitem):
            newitem.remove("")
        if (len(newitem) == 2):
            result.append((newitem[0], newitem[1]))
    result.sort()
    return result

if __name__ == "__main__":
    result = getFloatData("4IP")
    #print(result)

    result = getOptions("myScript.bash -v  -i 2   -p /local/bin/somefolder")
    print(result)


