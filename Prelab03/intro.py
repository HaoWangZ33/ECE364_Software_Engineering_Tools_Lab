def getHeadAverage(l, n):
    newl = l[0:n]
    suml = sum(newl)
    return suml / n

def getTailMax(l, m):
    new_m = -1 * m
    new_l = l[new_m:]
    return max(new_l)

def getNumberAverage(l):
    count = 0
    sum = 0
    for item in l:
        if (isinstance(item, int)) or (isinstance(item, float)):
            sum = sum + item
            count = count + 1
    return sum/count

def getFormattedSSN(n):
    new = str(n)
    while len(new) < 9:
        new = "0" + new
    final = new[0]+new[1]+new[2] + "-"+ new[4]+new[5] + "-" + new[6]+new[7] +new[8]
    return final

def findName(l, s):
    for person in l:
        name = person.split()
        if (name[0] == s) or (name[1] == s):
            n = person
            break
    return n

def getColumnSum(mat):
    new = []
    for i in range(len(mat[0])):
        sum = 0
        for item in mat:
            sum = sum + item[i]
        new.append(sum)
    return new

def getFormattedNames(ln):
    new = []
    for person in ln:
        name = person[2] + ", " + person[0] + " " + person[1]
        new.append(name)
    return new

def getElementwiseSum(l1, l2):
    count = 0
    if len(l1) != len(l2):
        if len(l1) < len(l2):
            count = len(l2) - len(l1)
            while count > 0:
                l1.append(0)
                count = count - 1
        else:
            count = len(l1) - len(l2)
            while count > 0:
                l2.append(0)
                count = count - 1
    new = []
    for i in range(len(l1)):
        sum = l1[i] + l2[i]
        new.append(sum)
    return new

def removeDuplicates(l):
    new = []
    for item in l:
        if item not in new:
            new.append(item)
    return new

def getMaxOccurrence(l):
    max_num = 0
    max_occ = 0
    temp = l[0]
    occ = 0
    l.sort()
    for item in l:
        if item == temp:
            occ = occ + 1
        else:
            if occ > max_occ:
                max_occ = occ
                max_num = temp
            temp = item
            occ = 1
    return max_num

def getMaxProduct(l):
    length = len(l) - 2
    max = 0
    for i in range(length):
        temp1 = i + 1
        temp2 = i + 2
        temp = (l[i]) * (l[temp1]) * (l[temp2])
        if temp > max:
            max = temp
    return max

# if __name__ == '__main__':
#     result = getHeadAverage([20, 30, 40], 2)
#     print(result)
#
#     result = getTailMax([100, 90, 80, 70], 3)
#     print(result)
#
#     result = getNumberAverage([1.5, 2, 3.5, 'abc'])
#     print(result)
#
#     result = getFormattedSSN(12345)
#     print(result)
#
#     result = findName(['hao wang', 'hao lol', 'lol lol'], 'hao')
#     print(result)
#
#     result = getColumnSum([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
#     print(result)
#
#     result = getFormattedNames([["first", "MID", "last"], ["first", "MID", "last"], ["first", "MID", "last"]])
#     print(result)
#
#     result = getElementwiseSum([1,2,3], [1,2,3,4,5])
#     print(result)
#
#     result = removeDuplicates([1, 1, 2, 3, 4, 4, 4, 5, 6])
#     print(result)
#
#     result = getMaxOccurrence([1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2])
#     print(result)
#
#     result = getMaxProduct([3, 7, -2, 2, 3, 5])
#     print(result)