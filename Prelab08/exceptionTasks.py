#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-10-23 22:25:42 -0400 (Sun, 23 Oct 2016) $
#$Revision: 94961 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab08/exceptionTasks.py $
#$Id: exceptionTasks.py 94961 2016-10-24 02:25:42Z ee364a07 $

from prelab08addon import performProcessing

class PointND:
    def __init__(self, *args):
        self.n = 0
        self.t = ()
        for item in args:
            if isinstance(item, float):
                temp = list(self.t)
                temp.append(item)
                self.t = tuple(temp)
                self.n = self.n + 1
            else:
                raise ValueError("Cannot instantiate an object with non-float values.")

    def __str__(self):
        temp = list(self.t)
        result = "("
        for i in range(len(temp)):
            result = result + "{0:.2f}".format(temp[i]) + ", "
        result = result[:-2]
        result = result + ")"
        return result

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n == other.n:
            diff = 0.0
            for i in range(len(self.t)):
                diff = diff + (self.t[i] - other.t[i])**2
            result = (diff)**0.5
            return result
        else:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
            return None

    def nearestPoint(self, points):
        if (points):
            closestP = PointND()
            closestDis = self.distanceFrom(points[0])
            closestP.n = points[0].n
            closestP.t = points[0].t
            for point in points:
                dis = self.distanceFrom(point)
                if dis < closestDis:
                    closestP.n = point.n
                    closestP.t = point.t
                    closestDis = dis
            return closestP
        else:
            raise ValueError("Input cannot be empty.")
            return None

    def clone(self):
        newPoint = PointND()
        newPoint.n = self.n
        newPoint.t = self.t

    def __add__(self, other):
        if isinstance(other, PointND):
            if self.n == other.n:
                newPoint = PointND()
                newPoint.n = self.n
                temp = []
                for i in range(len(self.t)):
                    temp.append(self.t[i] + other.t[i])
                newPoint.t = tuple(temp)
                return newPoint
            else:
                raise ValueError("Cannot operate on points with different cardinalities.")
                return None
        elif isinstance(other, float):
            newPoint = PointND()
            newPoint.n = self.n
            temp = list(self.t)
            for i in range(len(temp)):
                temp[i] = temp[i] + other
            newPoint.t = tuple(temp)
            return newPoint

    def __sub__(self, other):
        if isinstance(other, PointND):
            if self.n == other.n:
                newPoint = PointND()
                newPoint.n = self.n
                temp = []
                for i in range(len(self.t)):
                    temp.append(self.t[i] - other.t[i])
                newPoint.t = tuple(temp)
                return newPoint
            else:
                raise ValueError("Cannot operate on points with different cardinalities.")
                return None
        elif isinstance(other, float):
            newPoint = PointND()
            newPoint.n = self.n
            temp = list(self.t)
            for i in range(len(temp)):
                temp[i] = temp[i] + other
            newPoint.t = tuple(temp)
            return newPoint

    def __mul__(self, other):
        newPoint = PointND()
        newPoint.n = self.n
        temp = list(self.t)
        for i in range(len(temp)):
            temp[i] = temp[i] * other
        newPoint.t = tuple(temp)
        return newPoint

    def __truediv__(self, other):
        newPoint = PointND()
        newPoint.n = self.n
        temp = list(self.t)
        for i in range(len(temp)):
            temp[i] = temp[i] / other
        newPoint.t = tuple(temp)
        return newPoint

    def __neg__(self):
        newPoint = PointND()
        newPoint.n = self.n
        temp = list(self.t)
        for i in range(len(temp)):
            temp[i] = -1 * temp[i]
        newPoint.t = tuple(temp)
        return newPoint

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if self.n == other.n:
            result = True
            for i in range(len(self.t)):
                if self.t[i] != other.t[i]:
                    result = False
            return result
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __ne__(self, other):
        if self.n == other.n:
            result = False
            for i in range(len(self.t)):
                if self.t[i] != other.t[i]:
                    result = True
            return result
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __gt__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 > dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __ge__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 >= dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __lt__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 < dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __le__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 <= dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

def createPoint(dataString):

    try:
        input = dataString.split(',')
        for i in range(len(input)):
            input[i] = float(input[i])
        point1 = PointND(*input)
    except ValueError as emess:
        return emess
    else:
        return point1

def distanceBetween(point1, point2):
    try:
        distance = point1.distanceFrom(point2)
    except ValueError as error:
        return error
    else:
        return distance

def checkVicinity(point, pointList, radius):
    le = 0
    gt = 0
    invalid = 0
    for item in pointList:
        try:
            distance = point.distanceFrom(item)
        except:
            invalid = invalid + 1
        else:
            if distance <= radius:
                le = le + 1
            else:
                gt = gt + 1
    return (le, gt, invalid)

def checkOperation(*args):
    try:
        performProcessing(*args)
    except Exception as e:
        if isinstance(e, ConnectionRefusedError):
            raise ConnectionRefusedError(e)
        if isinstance(e, OSError):
            return "The following Error occurred: " + str(e)
        else:
            return False
    else:
        return True


if __name__ == "__main__":
    result = createPoint("asd,2.701,19.77")
    print(result)
    point1 = PointND(10.0, 10.0)
    point2 = PointND(0.0, 0.0)
    point3 = PointND(10.0, 11.0, )
    point4 = PointND(9.0, 9.0, 9.0)
    result = distanceBetween(point1, point2)
    print(result)
    result = checkVicinity(point2, [point1, point3, point4], 14)
    print(result)
    checkOperation(123)
