import logging
from car import Car
from car import PickUp
from car import SportsCar
from db import database
import datetime
import json
from bson import json_util

def main():
    logging.basicConfig(filename='car_traces.log',
                        level=logging.INFO,
                        filemode='w')
    logging.info("The program has started")
    
    inputFile = "random_generated_car_db.json"
    
    carDb = database()
    res = carDb.loadJsonFile(inputFile)
    if res == -1:
        return -1

    #print(carDb.getDict()[4].getProductionDate())
    #carDb.filterCarsByProductionDate()
    carDb.getCarsSortedByParameter("age", "ascend")

    #print(carDb.getDict()[1].getMaxPayloadCapacity())
    #print(len(carDb.getDict()))
    #carDb.getCarsSortedByParameter("age", "descend")
    
    #print(carDb.getYoungPickUps())
    #print(carDb.getDict()[2].getMaxSpeed())
    
    # json file feltöltése
    #with open("car_db.json", "w") as write_file:
    #    for i in carDb.getDict():
    #        json.dump(carDb.getDict()[i].__dict__, write_file, default = json_util.default)

if __name__ == '__main__':
    main()