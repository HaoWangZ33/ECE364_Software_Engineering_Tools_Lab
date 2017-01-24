#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-10-04 15:16:25 -0400 (Tue, 04 Oct 2016) $
#$Revision: 94400 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab06/xmlOperations.py $
#$Id: xmlOperations.py 94400 2016-10-04 19:16:25Z ee364a07 $

import re

def convertToAttrib():
    result = []
    with open ("points.xml", "r") as input:
        content = input.read()
    expr = r"^<[\w|\ |\=|?\")|\.]+>"
    header = re.findall(expr, content)
    print(header)
    ccc = "<coordinates>"
    ccc1 = "</coordinates>"
    ppp = "<point>"
    ppp1 = "</point>"
    expr = r"<point>(.*?)</point>"
    points = re.findall(expr, content, re.DOTALL)
    for item in points:
        expr = r"<ID>([\w]*?)</ID>"
        id = re.findall(expr, item, re.DOTALL)[0]
        expr = r"<X>[\ |\\\n]*([\w|\.|\+|\-]*?)[\ |\\\n]*</X>"
        x = re.findall(expr, item, re.DOTALL)[0]
        expr = r"<Y>[\ |\\\n]*([\w|\.|\+|\-]*?)[\ |\\\n]*</Y>"
        y = re.findall(expr, item, re.DOTALL)[0]
        result.append((id, x, y))
    with open ("points_out.xml", "w") as output:
        output.write(str(header))
        output.write("\n")
        output.write(ccc)
        output.write("\n")
        for item in result:
            output.write("   <point ID=\""+item[0]+"\" X=\""+item[1]+"\" Y=\""+item[2]+"\" />\n")
        output.write(ccc1)

def getGenres():
    with open ("books.xml", "r") as input:
        content = input.read()
    expr = r"<genre>(.*?)</genre>"
    result = re.findall(expr, content)
    result = set(result)
    result = list(result)
    result.sort()
    return result

def getAuthorOf(bookName):
    finalname = ""
    with open ("books.xml", "r") as input:
        content = input.read()
    expr = r"<author>(.*?)</author>[\ |\\\n]+<title>(.*?)</title>"
    result = re.findall(expr, content)
    for (name, title) in result:
        if title == bookName:
            finalname = name
    if finalname == "":
        return None
    else:
        return finalname

def getBookInfo(bookID):
    final = ()
    with open ("books.xml", "r") as input:
        content = input.read()
    expr = r"<book id=\"(.*?)\">[\ |\\\n]+<author>(.*?)</author>[\ |\\\n]+<title>(.*?)</title>"
    result = re.findall(expr, content)
    for (ID, name, title) in result:
        if ID == bookID:
            final = (title, name)
    if final == ():
        return None
    else:
        return final

def getBooksBy(authorName):
    result = []
    with open ("books.xml", "r") as input:
        content = input.read()
    expr = r"<author>(.*?)</author>[\ |\\\n]+<title>(.*?)</title>"
    find = re.findall(expr, content)
    for (name, title) in find:
        if name == authorName:
            result.append(title)
    result.sort()
    return result

def getBooksBelow(bookPrice):
    result = []
    with open ("books.xml", "r") as input:
        content = input.read()
    expr = r"<title>(.*?)</title>[\ |\\\n]+<genre>(.*?)+</genre>[\ |\\\n]+<price>(.*?)</price>"
    find = re.findall(expr, content)
    for (title, genre, price) in find:
        if float(price) < bookPrice:
            result.append(title)
    result.sort()
    return result

def searchForWord(word):
    result = []
    with open ("books.xml", "r") as input:
        content = input.read()
    expr = r"<title>(.*?)</title>[\ |\\\n]+<genre>(.*?)</genre>[\ |\\\n]+<price>(.*?)</price>[\ |\\\n]+<publish_date>(.*?)</publish_date>[\ |\\\n]+<description>(.*?)</description>"
    find = re.findall(expr, content, re.DOTALL)
    for (title, genre, price, pub, description) in find:
        if (word in title) or (word in description):
            result.append(title)
    result.sort()
    return result

if __name__ == '__main__':
    convertToAttrib()

    result = getGenres()
    print(result)

    result = getAuthorOf("Oberon's Legacy")
    print(result)

    result = getBookInfo("bk105")
    print(result)

    result = getBooksBy("O'Brien, Tim")
    print(result)

    result = getBooksBelow(5.0)
    print(result)

    result = searchForWord("trip")
    print(result)