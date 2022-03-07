class Vehicle():
    #private members      
    __fuelType = "Lorem"
    __maxPassengers = 100 
    __name = "Dolor"

    #Constructor
    def __init__(self, fuelType = "Lorem", maxPassengers = 100, name = "Dolor"):
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
        self.__name = name

    ##Get-Set
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def getFuelType(self):
        return self.__fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def getMaxPassengers(self):
        return self.__maxPassengers

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    #Output/Print
    def outsVec(self):
        print("Name: %s" % (self.__name))
        print("Fuel Type: %s" % (self.__fuelType))
        print("Max Passengers: %d" % (self.__maxPassengers))

    def move(self):
        print(">>%s is on its way to you...\n" % (self.__name))

    
