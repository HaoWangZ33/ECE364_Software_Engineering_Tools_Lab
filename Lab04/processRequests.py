#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-09-20 11:05:00 -0400 (Tue, 20 Sep 2016) $
#$Revision: 93839 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab04/processRequests.py $
#$Id: processRequests.py 93839 2016-09-20 15:05:00Z ee364a07 $

def processRequests():
    permission = getAccessControlByLogin()
    result = []
    with open ('ServerRequests.txt', 'r') as input:
        allline = input.readlines()
        for line in allline:
            sp = line.split()
            ID = sp[0]
            URL = sp[2]
            sp = sp[2].split('/')
            controller = sp[3]
            action = sp[4]
            result.append((ID, URL, controller, action, (controller in permission[ID])))
    return result

def getAccessControlByLogin():
    result = {}
    with open ('AccessControl.txt', 'r') as input:
        allline = input.readlines()
        allline = allline[2:]
        for line in allline:
            sp = line.split()
            name = sp[0]
            perm = sp[2]
            if name in result:
                newlist = result[name]
                newlist.append(perm)
                result[name] = newlist
            else:
                result[name] = [perm]
    for key, value in result.items():
        newset = set(value)
        result[key] = newset
    return result

def getAccessControlByController():
    nameID = {}
    result = {}
    with open ('Logins.txt', 'r') as logininput:
        allline = logininput.readlines();
        allline = allline[2:]
        for line in allline:
            sp = line.split()
            name = sp[0] + " " +sp[1]
            ID = sp[3]
            nameID[ID] = name
    with open ('AccessControl.txt', 'r') as input:
        allline = input.readlines()
        allline = allline[2:]
        for line in allline:
            sp = line.split()
            ID = sp[0]
            perm = sp[2]
            if perm in result:
                newlist = result[perm]
                newlist.append(nameID[ID])
                result[perm] = newlist
            else:
                result[perm] = [nameID[ID]]
    for key, value in result.items():
        newset = set(value)
        result[key] = newset
    return result

def getActionsOfController():
    result = {}
    with open ('ServerRequests.txt', 'r') as input:
        allline = input.readlines()
        for line in allline:
            sp = line.split()
            sp = sp[2]
            sp = sp.split('/')
            controller = sp[3]
            action = sp[4]
            if controller in result:
                newlist = result[controller]
                newlist.append(action)
                result[controller] = newlist
            else:
                result[controller] = [action]
    for key, value in result.items():
        newset = set(value)
        result[key] = newset
    return result

def isAccessAllowedFor(userID, url):
    permission = getAccessControlByLogin()
    if permission.get(userID) == None:
        return False
    perm = permission[userID]
    sp = url.split('/')
    controller = sp[3]
    return controller in perm

def getRequestsBy(userID):
    result = []
    permission = getAccessControlByLogin()
    if permission.get(userID) == None:
        return result
    logs = processRequests()
    for item in logs:
        ID = item[0]
        if ID == userID:
            URL = item[1]
            TF = item[4]
            result.append((URL, TF))
    result.sort()
    return result

def aggregateUserRequests():
    result = {}
    logs = processRequests()
    nameID = {}
    with open ('Logins.txt', 'r') as logininput:
        allline = logininput.readlines();
        allline = allline[2:]
        for line in allline:
            sp = line.split()
            name = sp[0] + " " +sp[1]
            ID = sp[3]
            nameID[ID] = name
    for ID, name in nameID.items():
        numTrue = 0
        numFalse = 0
        for entry in logs:
            if entry[0] == ID:
                if entry[4] == True:
                    numTrue = numTrue + 1
                elif entry[4] == False:
                    numFalse = numFalse + 1
        result[name] = (numTrue, numFalse)
    return result

def aggregateControllerRequests():
    result = {}
    controllerS = getAccessControlByController()
    logs = processRequests()
    for controller,_ in controllerS.items():
        numTrue = 0
        numFalse = 0
        for entry in logs:
            if entry[2] == controller:
                if entry[4] == True:
                    numTrue = numTrue + 1
                elif entry[4] == False:
                    numFalse = numFalse + 1
        result[controller] = (numTrue, numFalse)
    return result

if __name__ == "__main__":
    result = getAccessControlByLogin()
    print(result)

    result = getAccessControlByController()
    print(result)

    result = getActionsOfController()
    print(result)

    result = processRequests()
    print(result)

    #result = isAccessAllowedFor("jkelly", "http://www.purdue.com/Proceedings/Page14")
    result = isAccessAllowedFor("grichardson", "http://www.purdue.com/Internal/Page03")
    print(result)

    result = getRequestsBy("hwilson")
    print(result)

    result = aggregateUserRequests()
    print(result)

    result = aggregateControllerRequests()
    print(result)