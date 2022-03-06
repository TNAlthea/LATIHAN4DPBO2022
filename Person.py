class Person():
    #private members      
    __NIK = 12300000
    __name = "Lorem"
    __gender = "Ipsum" 

    #Constructor
    def __init__(self, NIK = 12300000, gender = "Lorem", name = "Dolor"):
        self.__NIK = NIK
        self.__gender = gender
        self.__name = name

    ##Get-Set
    def setNIK(self, NIK):
        self.__NIK = NIK

    def getNIK(self):
        return self.__NIK

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    #Output/Print
    def outsPerson(self):
        print("Name: %s" % (self.__name))
        print("NIK: %d" % (self.__NIK))
        print("Gender: %s" % (self.__gender))

    def sleep(self, parameter):
        if (parameter == 1):
            print(">>%s is sleeping... as always...\n" % (self.__name))
        else:
            print(">>%s NEVER SLEEP!\n" % (self.__name))

    