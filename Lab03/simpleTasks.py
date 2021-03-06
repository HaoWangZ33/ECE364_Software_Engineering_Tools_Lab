#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-09-13 11:15:02 -0400 (Tue, 13 Sep 2016) $
#$Revision: 93487 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab03/simpleTasks.py $
#$Id: simpleTasks.py 93487 2016-09-13 15:15:02Z ee364a07 $

# The following variable(s) are the only lines of code that should be outside of a function.

accounts = [
    'Mark Thomas:    $11.99   $52.08   $81.15   $79.16   $16.23   $88.11   $21.20   $0.02   ',
    'Gregory Powell:      $97.42     $96.05     $71.82     $24.79     $14.42     $60.84     $35.46     ',
    'Kevin Wood:     $93.37    $16.73    $97.05    $14.57    $53.29    ',
    'Martin Watson:     $20.53    $90.58    $22.07    $1.28    $75.40    $48.98    $36.46    $42.65    $5.01  $52.62  ',
    'Frank Young:     $32.02    $51.20    $0.99    $51.85    $88.38    $67.26    $62.72    $47.36    $38.89    ',
    'Michelle Thompson:     $2.44    $100.72    $81.44    $48.07    $68.71    $23.11    $79.23    $71.02    ',
    'Anne Harris:     $30.10    $58.32    $6.22    $3.67    $30.02    $37.65    $6.17    $41.30    $51.15    ',
    'Kelly Cooper:      $73.74     $57.63     $91.94     $42.94     $59.26     $64.30     $13.59     $19.69     $4.11 ',
    'Benjamin Foster:      $4.22     $63.02     $73.07     $99.73     $24.00     $77.79     $20.30     ',
    'Marie Perry:    $32.90   $80.27   $70.18   $68.74   $14.11   $7.38   ',
    'Cynthia Simmons:      $91.64     $56.95     $40.73     $61.28     $53.88     $77.05     $6.88     $23.37     ']

def getRowSum(accList):
    new = []
    for item in accList:
        count = 0
        sum = 0
        person = item.split()
        for piece in person:
            if count >= 2:
                str(piece)
                new_piece = piece[1:]
                sum = sum + float(new_piece)
            count = count + 1
        sum = round(sum, 2)
        new.append(sum)
    return new

def getDoublePalindromes():
    new = []
    for num in range(10, 1000001):
        num_str = str(num)
        yes_10 = 1
        for i in range(len(num_str)):
            if num_str[i] != num_str[len(num_str) - 1 - i]:
                yes_10 = 0
                break
        if yes_10 == 1:
            num_bin = bin(num)
            num_bin = num_bin[2:]
            yes_2 = 1
            for i in range(len(num_bin)):
                if num_bin[i] != num_bin[len(num_bin) - 1 - i]:
                    yes_2 = 0
                    break
            if yes_2 == 1:
                new.append(num)
    return new

def scaleVector(s, vList):
    if (isinstance(s, int) or isinstance(s, float)) and (isinstance(vList, list)) and (len(vList) != 0):
        for i in range(len(vList)):
            vList[i] = vList[i] * s
        return vList
    else:
        return None

def convertToBoolean(num):
    if (isinstance(num, int)) and (0 <= num <= 255):
        num_bin = bin(num)
        num_bin = num_bin[2:]
        if len(num_bin) < 8:
            num_bin = '0' * (8 - len(num_bin)) + num_bin
        new = []
        for i in num_bin:
            if i == '1':
                new.append(True)
            elif i == '0':
                new.append(False)
        return new
    else:
        return None

def convertToInteger(boolList):
    if (isinstance(boolList, list)) and (len(boolList) != 0):
        new = ''
        for item in boolList:
            if isinstance(item, bool):
                if item is True:
                    new = new + '1'
                elif item is False:
                    new = new + '0'
            else:
                return None
        new = int(new, 2)
        return new
    else:
        return None

def getWords(sentence, n):
    new = []
    in_string = sentence.split()
    for item in in_string:
        if (len(item) == n) and (item not in new):
            new.append(item)
    return new

def isSubListOf(superList, subList):
    if (isinstance(superList, list)) and (isinstance(subList, list)) and (len(superList) >= len(subList)):
        for i in range(len(superList)):
            if superList[i] == subList[0]:
                break
        j = 0
        yes = 1
        while (i < len(superList)) and (j < len(subList)):
            if superList[i] != subList[j]:
                yes = 0
                break
            else:
                i = i + 1
                j = j + 1
        if yes == 1:
            return True
        else:
            return False
    else:
        return None

def getElementsAt(l, i):
    new = []
    for item in l:
        if i in range(len(item)):
            new.append(item[i])
        else:
            new.append(0)
    return new


if __name__ == "__main__":
    result = getRowSum(accounts);
    print(result)

    result = getDoublePalindromes()
    print(result)

    result = scaleVector(5, [0, 1, 2, 3])
    print(result)

    result = convertToBoolean(135)
    print(result)

    result = convertToInteger([True, False, False, False, False, True, True, True])
    print(result)

    result = getWords("the power of this engine matches that of the one we use last year", 4)
    print(result)

    result = isSubListOf([0, -3, 2, 2, 8, 1, 4], [-3, 2, 2, 8])
    print(result)

    result = getElementsAt([[9, 1, 0, 3], [1, 3, 7], [11, 35, 96, -1, 85], [43, 17]], 5)
    print(result)