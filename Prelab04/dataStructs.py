#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-09-18 20:20:19 -0400 (Sun, 18 Sep 2016) $
#$Revision: 93786 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab04/dataStructs.py $
#$Id: dataStructs.py 93786 2016-09-19 00:20:19Z ee364a07 $

import glob

def uniqueLetters(s):
    s = list(s)
    s = set(s)
    s = list(s)
    s.sort()
    s.reverse()
    new = "".join(s)
    return new

def scaleSet(aSet, num):
    new = list(aSet)
    for i in range(len(new)):
        new[i] = round(new[i] * num, 2)
    new = set(new)
    return new

def printNames(aSet):
    new = list(aSet)
    new.sort()
    new = "\n".join(new)
    return new

def getStateName(stateAbb):
    know = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    for key, value in know.items():
        if value == stateAbb:
            new = key
    return new

def getZipCodes(stateName):
    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}
    for name in d1.keys():
        if name == stateName:
            abb = d1[name]
    new = []
    for key, value in d2.items():
        if value == abb:
            new.append(key)
    new = set(new)
    return new

def printSortedMap(s):
    new = []
    for (lastName, firstName, mi), weight in s.items():
        out = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
        new.append(out)
    new.sort()
    new = "\n". join(new)
    return new

def switchNames(s):
    new = {}
    for (last, first, mi), weight in s.items():
        name = "{0} {1}".format(first, last)
        new[name] = weight
    return new

def getPossibleMatches(record, n):
    new = []
    for name, (mm, dd, yy) in record.items():
        if ((mm == n) or (dd == n) or (yy == n)):
            new.append(name)
    new = set(new)
    return new

def getPurchaseReport():
    result = {}
    price = {}
    with open('purchases/Item List.txt', 'r') as itemlist:
        allline = itemlist.readlines()
        allline = allline[2:]
        for line in allline:
            sp = line.split()
            temp = str(sp[1])
            temp = temp[1:]
            temp = float(temp)
            price[sp[0]] = temp
    filenames = glob.glob('./purchases/purchase_*')
    for filename in filenames:
        with open (filename, 'r') as input:
            allline = input.readlines()
            allline = allline[2:]
            sum = 0
            for line in allline:
                sp = line.split()
                sum = sum + (price[sp[0]] * int(sp[1]))
        name = filename.split('_')
        name = name[1]
        name = name.split('.')
        name = name[0]
        name = int(name)
        sum = round(sum, 2)
        result[name] = sum
    return result

def getTotalSold():
    result = {}
    filenames = glob.glob('./purchases/purchase_*')
    for filename in filenames:
         with open (filename, 'r') as input:
             allline = input.readlines()
             allline = allline[2:]
             for line in allline:
                 sp = line.split()
                 if result.get(sp[0]) == None:
                     result[sp[0]] = int(sp[1])
                 else:
                     result[sp[0]] = result[sp[0]] + int(sp[1])
    return result



if __name__ == "__main__":
    result = uniqueLetters("ABDBDARWET")
    print(result)

    result = scaleSet({3.12, 5.0, 7.2, 15.24}, 2.1)
    print(result)

    result = printNames({"John", "Marry", "Jacob", "Connor", "Kyle"})
    print(result)

    result = getStateName("CA")
    print(result)

    result = getZipCodes("California")
    print(result)

    result = printSortedMap({("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9})
    print(result)

    result = switchNames({("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9})
    print(result)

    result = getPossibleMatches({"John": (2, 10, 95), "Alex": (10, 20, 95), "Felix": (10, 2, 97)}, 95)
    print(result)

    result = getPurchaseReport()
    print(result)

    result = getTotalSold()
    print(result)