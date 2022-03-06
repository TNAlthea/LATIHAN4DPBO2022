from Person import Person

class Job(Person):
    #private members      
    __NIP = 12300000
    __companyName = "Dolor"
    __position = "Male" 

    #Constructor
    def __init__(self, NIP = 12300000, position = "Lorem", companyName = "Ipsum"):
        self.__NIP = NIP
        self.__position = position
        self.__companyName = companyName

    ##Get-Set
    def setNIP(self, NIP):
        self.__NIP = NIP

    def getNIP(self):
        return self.__NIP

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def getCompanyName(self):
        return self.__companyName

    #Output/Print
    def outsJob(self):
        print("Company Name: %s" % (self.__companyName))
        print("NIP: %d" % (self.__NIP))
        print("Position: %s" % (self.__position))


    