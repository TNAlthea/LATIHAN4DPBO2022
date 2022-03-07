from Job import Job 

class Driver(Job):
    #private members      
    __licenseID = 12300000
    __vehicleType = "Lorem" 
    __activeUntil = "Ipsum 3000"

    #Constructor
    def __init__(self, licenseID = 12300000, vehicleType = "Lorem", activeUntil = "Ipsum 3000"):
        self.__licenseID = licenseID
        self.__vehicleType = vehicleType
        self.__activeUntil = activeUntil

    ##Get-Set
    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID

    def getLicenseID(self):
        return self.__licenseID

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicleType(self):
        return self.__vehicleType

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getActiveUntil(self):
        return self.__activeUntil

    #Output/Print
    def outsDriver(self):
        print("Active Until: %s" % (self.__activeUntil))
        print("License ID: %d" % (self.__licenseID))
        print("Vehicle Type: %s" % (self.__vehicleType))


    
