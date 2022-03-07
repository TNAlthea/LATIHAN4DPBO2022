from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

from Person import Person
from Job import Job
from Driver import Driver

#VEHICLE FAMILY (Actually i don't know what "classifier word/term" that has to be used here. As a result, i refer them as a "family")
#VEHICLE FAMILY contains 3 classes such as Airplane, Ship, and Vehicle itself.
#*Hierarchical explanation can be read on readme.md @ TNAlthea github*

#DUMMY DATA
##SHIP
Fubuki = Ship()
Fubuki.setName("Fubuki")
Fubuki.setAge(94)
Fubuki.setCountryOfManufacture("Japan")
Fubuki.setFuelType("Diesel fuel marine")
Fubuki.setMaxPassengers(219)
Fubuki.setType("Destroyer Class Type I/Fubuki-Class")

Yamato = Ship()
Yamato.setName("Yamato")
Yamato.setAge(80)
Yamato.setCountryOfManufacture("Japan")
Yamato.setFuelType("Diesel fuel marine")
Yamato.setMaxPassengers(2767)
Yamato.setType("Yamato-Class Battleships")

Pensacola = Ship()
Pensacola.setName("Pensacola")
Pensacola.setAge(97)
Pensacola.setCountryOfManufacture("United States")
Pensacola.setFuelType("Diesel fuel marine")
Pensacola.setMaxPassengers(530)
Pensacola.setType("Pensacola-Class Cruiser")

NewMexico = Ship()
NewMexico.setName("New Mexico")
NewMexico.setAge(104)
NewMexico.setCountryOfManufacture("United States")
NewMexico.setFuelType("Diesel fuel marine")
NewMexico.setMaxPassengers(530)
NewMexico.setType("New Mexico-Class Battleships")

Moskva = Ship()
Moskva.setName("Moskva")
Moskva.setAge(43)
Moskva.setCountryOfManufacture("Soviet Union")
Moskva.setFuelType("Diesel fuel marine")
Moskva.setMaxPassengers(480)
Moskva.setType("Slava-Class Cruiser")

##AIRCRAFT
Boeing737 = Airplane()
Boeing737.setName("Boeing 737")
Boeing737.setAge(55)
Boeing737.setWingsLength("64 meters")
Boeing737.setFuelType("Kerosene")
Boeing737.setMaxPassengers(210)
Boeing737.setType("Narrow-Body Airliner")

Boeing747 = Airplane()
Boeing747.setName("Boeing 747")
Boeing747.setAge(52)
Boeing747.setWingsLength("76 meters")
Boeing747.setFuelType("Kerosene")
Boeing747.setMaxPassengers(467)
Boeing747.setType("Wide-Body Airliner")

Boeing787 = Airplane()
Boeing787.setName("Boeing 787 Dreamliner")
Boeing787.setAge(15)
Boeing787.setWingsLength("68 meters")
Boeing787.setFuelType("Kerosene")
Boeing787.setMaxPassengers(467)
Boeing787.setType("Wide-Body Airliner")

AirbusA380 = Airplane()
AirbusA380.setName("Airbus A380")
AirbusA380.setAge(19)
AirbusA380.setWingsLength("80 meters")
AirbusA380.setFuelType("Kerosene and GTL")
AirbusA380.setMaxPassengers(850)
AirbusA380.setType("Wide-Body Airliner")

AirbusA350 = Airplane()
AirbusA350.setName("Airbus A350")
AirbusA350.setAge(12)
AirbusA350.setWingsLength("212 ft 5 in")
AirbusA350.setFuelType("SAF")
AirbusA350.setMaxPassengers(350)
AirbusA350.setType("Wide-Body Airliner")


#PERSON FAMILY contains 3 classes such as Driver, Job, and Person itself.
#PERSON WITH A NON-DRIVER JOB
Ilham = Job()
Ilham.setName("Ilham Kurniawan")
Ilham.setGender("Male")
Ilham.setNIK(123456)
Ilham.setCompanyName("PT Mencari Cinta Sejati")
Ilham.setNIP(1337)
Ilham.setPosition("CEO")

Tatang = Job()
Tatang.setName("Tatang Daedalus")
Tatang.setGender("Male")
Tatang.setNIK(654321)
Tatang.setCompanyName("PT Mencari Cinta Sejati")
Tatang.setNIP(1337)
Tatang.setPosition("Human Resource and Development")

Santi = Job()
Santi.setName("Santi Santiago")
Santi.setGender("Female")
Santi.setNIK(100101)
Santi.setCompanyName("PT Mencari Cinta Sejati")
Santi.setNIP(1337)
Santi.setPosition("Accountant")

#PERSON WITH DRIVER AS A JOB
Rusman = Driver()
Rusman.setName("Rusman")
Rusman.setGender("Male")
Rusman.setNIK(1017)
Rusman.setCompanyName("Gondar Holdings Limited")
Rusman.setNIP(1337420)
Rusman.setPosition("Super Senior Driver Masterclass")
Rusman.setLicenseID(320001)
Rusman.setVehicleType("Pickup Truck")
Rusman.setActiveUntil("Lifetime")

Maman = Driver()
Maman.setName("Maman Racing")
Maman.setGender("Male")
Maman.setNIK(99999999)
Maman.setCompanyName("Stock Car Auto Racing, LLC (NASCAR)")
Maman.setNIP(500)
Maman.setPosition("Mind Racer")
Maman.setLicenseID(123999)
Maman.setVehicleType("SUV")
Maman.setActiveUntil("Lifetime")


#OUTPUT
##VEHICLE
###SHIP
print("     =============")
print("======SHIP OUTPUT======")
print("     =============\n")
Fubuki.outsVec()
Fubuki.outsShip()
Fubuki.move()

Yamato.outsVec()
Yamato.outsShip()
Yamato.move()

NewMexico.outsVec()
NewMexico.outsShip()
NewMexico.move()

Pensacola.outsVec()
Pensacola.outsShip()
Pensacola.move()

Moskva.outsVec()
Moskva.outsShip()
Moskva.move()

###AIRPLANE
print("     =================")
print("======AIRPLANE OUTPUT======")
print("     =================\n")
Boeing737.outsVec()
Boeing737.outsAir()
Boeing737.move()

Boeing747.outsVec()
Boeing747.outsAir()
Boeing747.move()

Boeing787.outsVec()
Boeing787.outsAir()
Boeing787.move()

AirbusA350.outsVec()
AirbusA350.outsAir()
AirbusA350.move()

AirbusA380.outsVec()
AirbusA380.outsAir()
AirbusA380.move()

##PERSON WITH A NON-DRIVER JOB
print("    ===================")
print("=====NON-DRIVER OUTPUT=====")
print("    ===================\n")
Ilham.outsPerson()
Ilham.outsJob()
Ilham.sleep(0)

Tatang.outsPerson()
Tatang.outsJob()
Tatang.sleep(1)

Santi.outsPerson()
Santi.outsJob()
Santi.sleep(0)

##PERSON WITH DRIVER JOB
print("    ===============")
print("=====DRIVER OUTPUT=====")
print("    ===============\n")
Rusman.outsPerson()
Rusman.outsJob()
Rusman.outsDriver()
Rusman.sleep(1)

Maman.outsPerson()
Maman.outsJob()
Maman.outsDriver()
Maman.sleep(0)
