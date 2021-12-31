#!/usr/bin/env python3

class RTSLabs:
    
    aboveBelowDict = {"above" : 0, "below" : 0}
    outputString = ""
    
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



