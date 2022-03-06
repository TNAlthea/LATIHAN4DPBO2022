from Vehicle import Vehicle

class Airplane(Vehicle):
    #private members      
    __age = 1000
    __type = "Ipsum" 
    __wingsLength = "Dolor Meters"

    ##Constructor
    def __init__(self, age = 1000, type = "Ipsum"):
        self.__age = age
        self.__type = type

    ##Get-set
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getWingsLength(self):
        return self.__wingsLength

    #Output/Print
    def outsAir(self):
        print("Age: %s" % (self.__age))
        print("Type: %s" % (self.__type))
        print("Wings Length: %s" % (self.__wingsLength))

    