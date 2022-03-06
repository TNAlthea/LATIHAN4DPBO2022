from Vehicle import Vehicle

class Ship(Vehicle):
    #private members      
    __age = 1000
    __type = "Ipsum" 
    __countryOfManufacture = "Dolor"

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

    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    #Output/Print
    def outsShip(self):
        print("Age: %s" % (self.__age))
        print("Type: %s" % (self.__type))
        print("Country of Manufacture: %s" % (self.__countryOfManufacture))

    