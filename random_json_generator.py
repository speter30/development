import random
from car import Car
from car import PickUp
from car import SportsCar
from db import database
from datetime import datetime
import json

def random_json_generator(length):
    identity = 1
    data = {}
    data['cars'] = []
    
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
        randomBrandNumber = random.randint(0, len(pickupBrands) - 1)

        randomProductionYear = random.randint(1950, currentYear)
        if randomProductionYear == currentYear:
            randomProductionMonth = random.randint(1, currentMonth)

        else:
            randomProductionMonth = random.randint(1, 12)
            randomProductionDate = [randomProductionYear, randomProductionMonth, 1]

        if random.randint(1, 2) == 1:
            if pickupBrands[randomBrandNumber] == "Ford":
                randomTypeNumber = random.randint(0, len(pickupFords) - 1)
                chosenCarType = pickupFords[randomTypeNumber]

                if chosenCarType == "F-150":
                    maxPayloadCapacity = 1503
                elif chosenCarType == "FD-100":
                    maxPayloadCapacity = 1332
                elif chosenCarType == "F-550":
                    maxPayloadCapacity = 1210 

                data['cars'].append({"id": identity, "brand": pickupBrands[randomBrandNumber], 
                                "type": chosenCarType, "date" : randomProductionDate,
                                "maxPayloadCapacity": maxPayloadCapacity})

            elif pickupBrands[randomBrandNumber] == "Toyota":
                randomTypeNumber = random.randint(0, len(pickupToyotas) - 1)
                chosenCarType = pickupToyotas[randomTypeNumber]

                if chosenCarType == "Tundra":
                    maxPayloadCapacity = 1732
                elif chosenCarType == "C-500":
                    maxPayloadCapacity = 1129
                elif chosenCarType == "T100":
                    maxPayloadCapacity = 1294 
                elif chosenCarType == "Tacoma":
                    maxPayloadCapacity = 1185 

                data['cars'].append({"id": identity, "brand": pickupBrands[randomBrandNumber], 
                                "type": chosenCarType, "date" : randomProductionDate,
                                "maxPayloadCapacity": maxPayloadCapacity})

            else:
                randomTypeNumber = random.randint(0, len(pickupNissans) - 1)
                chosenCarType = pickupNissans[randomTypeNumber]
            
                if chosenCarType == "Frontier":
                    maxPayloadCapacity = 1800
                elif chosenCarType == "Titan":
                    maxPayloadCapacity = 1374
                elif chosenCarType == "NP200":
                    maxPayloadCapacity = 1273 
                elif chosenCarType == "Navara":
                    maxPayloadCapacity = 1088 

                data['cars'].append({"id": identity, "brand": pickupBrands[randomBrandNumber], 
                                "type": chosenCarType, "date" : randomProductionDate,
                                "maxPayloadCapacity": maxPayloadCapacity})

            identity += 1
        else:
            if sportBrands[randomBrandNumber] == "Audi":
                randomTypeNumber = random.randint(0, len(sportAudis) - 1)
                chosenCarType = sportAudis[randomTypeNumber]

                if chosenCarType == "TT":
                    maxSpeed = 280
                elif chosenCarType == "R8":
                    maxSpeed = 290
                elif chosenCarType == "RS 7":
                    maxSpeed = 307 

                data['cars'].append({"id": identity, "brand": sportBrands[randomBrandNumber], 
                                "type": chosenCarType, "date" : randomProductionDate,
                                "maxSpeed": maxSpeed})

            elif sportBrands[randomBrandNumber] == "Porsche":
                randomTypeNumber = random.randint(0, len(sportPorsches) - 1)
                chosenCarType = sportPorsches[randomTypeNumber]

                if chosenCarType == "Cayman":
                    maxSpeed = 293
                elif chosenCarType == "Carrera":
                    maxSpeed = 275
                elif chosenCarType == "Boxster":
                    maxSpeed = 310 
                elif chosenCarType == "Targa":
                    maxSpeed = 306 

                data['cars'].append({"id": identity, "brand": sportBrands[randomBrandNumber], 
                                "type": chosenCarType, "date" : randomProductionDate,
                                "maxSpeed": maxSpeed})

            else:
                randomTypeNumber = random.randint(0, len(sportLamborghinis) - 1)
                chosenCarType = sportLamborghinis[randomTypeNumber]
            
                if chosenCarType == "Aventador":
                    maxSpeed = 295
                elif chosenCarType == "Huracan":
                    maxSpeed = 304
                elif chosenCarType == "Urus":
                    maxSpeed = 280 
                elif chosenCarType == "Sián":
                    maxSpeed = 315 

                data['cars'].append({"id": identity, "brand": sportBrands[randomBrandNumber], 
                                "type": chosenCarType, "date" : randomProductionDate,
                                "maxSpeed": maxSpeed})

            identity += 1

    with open('random_generated_car_db.json', 'w') as outfile:
        json.dump(data, outfile, indent = 2)

database = random_json_generator(1000)