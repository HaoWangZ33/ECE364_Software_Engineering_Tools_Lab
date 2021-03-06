#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-10-02 20:16:20 -0400 (Sun, 02 Oct 2016) $
#$Revision: 94281 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab06/regexTasks.py $
#$Id: regexTasks.py 94281 2016-10-03 00:16:20Z ee364a07 $

import re

def getWords(sentence, letter):
    result = []
    if letter.islower():
        lettero = letter.upper()
    else:
        lettero = letter.lower()
    expr = r"^["+letter+"|"+lettero+"][\w.]+"
    tmp = re.findall(expr, sentence)
    result = result + tmp
    expr = r" ["+letter+"|"+lettero+"][\w.]+"
    tmp = re.findall(expr, sentence)
    for i in range(len(tmp)):
        tmp[i] = tmp[i][1:]
    result = result + tmp
    expr = r"[\w.]+["+letter+"|"+lettero+"] "
    tmp = re.findall(expr, sentence)
    for i in range(len(tmp)):
        tmp[i] = tmp[i][:-1]
    result = result + tmp
    expr = r"[\w.]+["+letter+"|"+lettero+"]$"
    tmp = re.findall(expr, sentence)
    result = result + tmp
    for item in result:
        if (item[0] == letter or item[0] == lettero) and (item[-1] == letter or item[-1] == lettero):
            result.remove(item)
    return result

def extractFloats(s):
    expr = r"[-|+]?[\d.]+\.[\d.]+"
    result = re.findall(expr, s)
    return result

def getUrlParts(url):
    expr = r"/[\w.]+"
    result = re.findall(expr, url)
    for i in range(len(result)):
        result[i] = result[i][1:]
    result = tuple(result)
    return result

def getQueryParameters(url):
    result = []
    expr = r"[\w|\_|\-|\.]+=[\w|\_|\-|\.]+"
    tmp = re.findall(expr, url)
    for item in tmp:
        expr = r"[\w|\_|\-|\.]+"
        tmp1 = re.findall(expr, item)
        tmp1 = tuple(tmp1)
        result.append(tmp1)
    return result

def findFunctions(fileName):
    result = []
    with open (fileName, "r") as input:
        content = input.read()
        expr = r"^def[ ]+[\w|\ |\(|\)|\:|\,]+$"
        tmp = re.findall(expr, content, re.MULTILINE)
    for func in tmp:
        expr = r"def[ ]+[\w]+"
        name = re.findall(expr, func)
        name = name[0]
        expr = r"[ ][\w]+"
        name = re.findall(expr, name)
        name = name[0]
        name = name[1:]
        expr = r"\([\w|\,\ ]+\)"
        argu = re.findall(expr, func)
        argu = argu[0]
        expr = r"[\w]+"
        argu = re.findall(expr, argu)
        tmp_tup = (name, argu)
        result.append(tmp_tup)
    return result

if __name__ == "__main__":
    result = getWords("The TART program runs on Tuesday and Thursday, but it does not start until next week.", "t")
    print(result)

    result = extractFloats("The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each.")
    print(result)
    result = extractFloats("The signal fluctuates between -0.3452 and +12.6509 volts. Try to keep it at 6 volts.")
    print(result)

    result = getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall")
    print(result)

    result = getQueryParameters("http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here")
    print(result)

    result = findFunctions("regexTasks.py")
    print(result)