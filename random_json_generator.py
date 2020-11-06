import random
from car import Car
from car import PickUp
from car import SportsCar
from db import database
from datetime import datetime
import json
from bson import json_util

def random_json_generator(length):
    identity = 1
    data = {}
    data['cars'] = []
    
    generatedDb = database()

    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    pickupBrands = ["Ford", "Toyota", "Nissan"]
    pickupFords = ["F-150", "FD-100", "F-550"]
    pickupToyotas = ["Tundra", "C-500", "T100", "Tacoma"]
    pickupNissans = ["Frontier", "Titan", "NP200", "Navara"]

    sportBrands = ["Audi", "Lamborghini", "Porsche"]
    sportAudis = ["TT", "R8", "RS 7"]
    sportPorsches = ["Cayman", "Boxster", "Carrera", "Targa"]
    sportLamborghinis = ["Aventador", "Huracan", "Urus", "Sián"]

    for i in range(length):
        randomProductionYear = random.randint(1950, currentYear)
        if randomProductionYear == currentYear:
            randomProductionMonth = random.randint(1, currentMonth)

        else:
            randomProductionMonth = random.randint(1, 12)
            
        randomProductionDate = [randomProductionYear, randomProductionMonth, 1]

        if random.randint(1, 2) == 1:
            newPickUp = PickUp()
            newPickUp.setId(identity)
            newPickUp.setProductionDate(randomProductionDate)
            
            randomBrandNumber = random.randint(0, len(pickupBrands) - 1)
            newPickUp.setBrand(pickupBrands[randomBrandNumber])

            if pickupBrands[randomBrandNumber] == "Ford":
                randomTypeNumber = random.randint(0, len(pickupFords) - 1)
                chosenCarType = pickupFords[randomTypeNumber]

                if chosenCarType == "F-150":
                    newPickUp.setMaxPayloadCapacity(1503)
                elif chosenCarType == "FD-100":
                    newPickUp.setMaxPayloadCapacity(1332)
                elif chosenCarType == "F-550":
                    newPickUp.setMaxPayloadCapacity(1210)

            elif pickupBrands[randomBrandNumber] == "Toyota":
                randomTypeNumber = random.randint(0, len(pickupToyotas) - 1)
                chosenCarType = pickupToyotas[randomTypeNumber]

                if chosenCarType == "Tundra":
                    newPickUp.setMaxPayloadCapacity(1732)
                elif chosenCarType == "C-500":
                    newPickUp.setMaxPayloadCapacity(1129)
                elif chosenCarType == "T100":
                    newPickUp.setMaxPayloadCapacity(1294)
                elif chosenCarType == "Tacoma":
                    newPickUp.setMaxPayloadCapacity(1185)

            else:
                randomTypeNumber = random.randint(0, len(pickupNissans) - 1)
                chosenCarType = pickupNissans[randomTypeNumber]
            
                if chosenCarType == "Frontier":
                    newPickUp.setMaxPayloadCapacity(1800)
                elif chosenCarType == "Titan":
                    newPickUp.setMaxPayloadCapacity(1374)
                elif chosenCarType == "NP200":
                    newPickUp.setMaxPayloadCapacity(1273)
                elif chosenCarType == "Navara":
                    newPickUp.setMaxPayloadCapacity(1088)

            newPickUp.setCarType(chosenCarType)
            generatedDb.addItem({newPickUp.getId() : newPickUp})

            identity += 1
        
        else:
            newSportsCar = SportsCar()
            newSportsCar.setId(identity)
            newSportsCar.setProductionDate(randomProductionDate)
            
            randomBrandNumber = random.randint(0, len(sportBrands) - 1)
            newSportsCar.setBrand(sportBrands[randomBrandNumber])
            
            if sportBrands[randomBrandNumber] == "Audi":
                randomTypeNumber = random.randint(0, len(sportAudis) - 1)
                chosenCarType = sportAudis[randomTypeNumber]

                if chosenCarType == "TT":
                    newSportsCar.setMaxSpeed(280)
                elif chosenCarType == "R8":
                    newSportsCar.setMaxSpeed(290)
                elif chosenCarType == "RS 7":
                    newSportsCar.setMaxSpeed(307)

            elif sportBrands[randomBrandNumber] == "Porsche":
                randomTypeNumber = random.randint(0, len(sportPorsches) - 1)
                chosenCarType = sportPorsches[randomTypeNumber]

                if chosenCarType == "Cayman":
                    newSportsCar.setMaxSpeed(293)
                elif chosenCarType == "Carrera":
                    newSportsCar.setMaxSpeed(275)
                elif chosenCarType == "Boxster":
                    newSportsCar.setMaxSpeed(310)
                elif chosenCarType == "Targa":
                    newSportsCar.setMaxSpeed(306)

            else:
                randomTypeNumber = random.randint(0, len(sportLamborghinis) - 1)
                chosenCarType = sportLamborghinis[randomTypeNumber]
            
                if chosenCarType == "Aventador":
                    newSportsCar.setMaxSpeed(295)
                elif chosenCarType == "Huracan":
                    newSportsCar.setMaxSpeed(304)
                elif chosenCarType == "Urus":
                    newSportsCar.setMaxSpeed(280)
                elif chosenCarType == "Sián":
                    newSportsCar.setMaxSpeed(315)

            newSportsCar.setCarType(chosenCarType)
            generatedDb.addItem({newSportsCar.getId() : newSportsCar})

            identity += 1

    #with open('random_generated_car_db.json', 'w') as outfile:
    #    json.dump(data, outfile)

    with open('random_generated_car_db.json', 'w') as writeFile:
        writeFile.write("{\"cars\": [ \n")
        #json.dump(generatedDb.getDict(), writeFile,
        #    default = json_util.default, indent = 2)
        length  = len(generatedDb.getDict())
        for i in generatedDb.getDict():
            json.dump(generatedDb.getDict()[i].__dict__, writeFile, 
                default = json_util.default, indent = 2)
            if i < length:
                writeFile.write(",")
        writeFile.write("]}")

database = random_json_generator(200)