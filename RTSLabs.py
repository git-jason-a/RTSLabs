#!/usr/bin/env python3



class RTSLabs:
    
    def __init__(self):
      self.aboveBelowDict = {"above" : 0, "below" : 0}
      self.outputString = ""

    def aboveBelow(self,aboveBelowList,aboveBelowInt):     
        assert(type(aboveBelowInt) is int),("aboveBelowInt " + aboveBelowInt + " is not an int.")
        aboveBelowDict = self.aboveBelowDict   
        for item in aboveBelowList:
            if not type(item) is int:
                print(item +" is not an int")
            elif item > aboveBelowInt:
                aboveBelowDict["above"] += 1
            elif aboveBelowInt > item:
                aboveBelowDict["below"] += 1      
        return aboveBelowDict

    def stringRotation(self,inputString,rotationInt):
        assert(type(inputString) is str),(str(inputString) + " is not a string.")
        assert(len(inputString)>rotationInt),("Length of inputString " + str(inputString) + " must be greater than rotationInt " + str(rotationInt))
        outputString = self.outputString 
        prefixString = inputString[rotationInt:len(inputString)]
        outputString = (prefixString+inputString[:rotationInt])
        return outputString



#test cases (uncomment to run)

#1. success

#myObj = RTSLabs() 
#myList = [1,8,2,8,4,76,3,2,9]
#myInt = 4
#print(myObj.aboveBelow(myList,myInt))
#print(myObj.stringRotation("thisIsAnewString",4))

#2. success but will inform that o is not an int
#myObj1 = RTSLabs()
#myList = [1,"o",2,8,4,76,3,2,9]
#myInt = 4
#print(myObj1.aboveBelow(myList,myInt))
#print(myObj1.stringRotation("thisIsAnewString",4))

#3. fail myInt value is not type int
#myObj2 = RTSLabs()
#myList = [1,8,2,8,4,76,3,2,9]
#myInt = ""
#print(myObj2.aboveBelow(myList,myInt))
#print(myObj2.stringRotation("thisIsAnewString",4))

#4. fail stringRotation 1st argument is not a string
#myObj3 = RTSLabs()
#myList = [1,8,2,8,4,76,3,2,9]
#myInt = 6
#print(myObj3.aboveBelowDict)
#print(myObj3.stringRotation(7,4))

#5. fail stringRotation 2nd argument is longer that string length, unable to perform rotation
myObj4 = RTSLabs()
myList = [1,8,2,8,4,76,3,2,9]
myInt = 6
print(myObj4.aboveBelow(myList,myInt))
print(myObj4.stringRotation("thi",4))
