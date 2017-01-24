#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-11-01 11:17:52 -0400 (Tue, 01 Nov 2016) $
#$Revision: 95216 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab09/CompositeMap.py $
#$Id: CompositeMap.py 95216 2016-11-01 15:17:52Z ee364a07 $

class Entry:

    def __init__(self, k1, k2, v):
        if (isinstance(k1, int) and isinstance(k2, int) and isinstance(v, str)):
            self.key = (k1, k2)
            self.value = v
        else:
            raise TypeError("Error: k1, k2 should be type int, v should be type str.")
        
    def __str__(self):
        result = "("+ str(self.key[0]) + ", " + str(self.key[1]) + "): \"" + self.value + "\""
        return result

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False

class Lookup:

    def __init__(self, name):
        if name == "":
            raise ValueError("Error: name cannot be empty")
        else:
            self._name = name
            self._container = {}

    def __str__(self):
        result = "[\"" + self._name + "\": "+ "{0:02x}".format(len(self._container)) + " Entries]"
        return result

    def add(self, entry):
        for item in self._container:
            if item.key == entry.key:
                raise KeyError("same key exists")
        result = list(self._container)
        result.append(entry)
        self._container = set(result)

    def update(self, entry):
        exist = False
        for item in self._container:
            if item.key == entry.key:
                item.value = entry.value
                exist = True
        if exist == False:
            raise KeyError("entry does not exist in table")

    def addOrUpdate(self, entry):
        try:
            self.add(entry)
        except:
            self.update(entry)

    def remove(self, entry):
        exist = False
        for item in self._container:
            if item.key == entry.key:
                exist = True
                result = list(self._container)
                result.remove(entry)
                self._container = set(result)
        if exist == False:
            raise KeyError("entry does not exist")

    def count(self):
        return len(self._container)

    def __getitem__(self, item):
        exist = False
        if (isinstance(item, int)):
            result = []
            for entry in self._container:
                if entry.key[0] == item or entry.key[1] == item:
                    result.append(entry.value)
                    exist = True
            result.sort()
            return result
        elif (isinstance(item, tuple)):
            for entry in self._container:
                if entry.key == item:
                    exist = True
                    return entry.value
        if exist == False:
            raise KeyError("not found")

    def __setitem__(self, key, value):
        c1 = Entry(key[0], key[1], value)
        self.addOrUpdate(c1)

if __name__ == '__main__':
    c1 = Entry(1,2,"lol")
    c2 = Entry(1,3,"haha")
    c3 = Entry(1,4,"muhaha")
    look1 = Lookup("class1")
    look1.add(c1)
    look1.add(c2)
    look1.addOrUpdate(c3)
    look1.remove(c3)
    look1[(1,4)] = "muhaha"
    print(look1[(1,4)])



