- fuggveny altalanosabbra. Pl. 
   -> getCarsSortedByParameter(self, param, ascend/descend) returns list of objects
   -> filterCarsByProductionDate(self, listOfObject)
   -> filterCarsByEngineSize(self, listOfObject)

- testcase-ek irasa:
  -> test_inputBrandValid ==> String max 10 karakter hosszan, tesztelni hogy hosszabbal probalsz es nem engedi
  -> test_sortByAge
  -> test_getYoungerThan(10 years) => getCarsSortedByParameter(age, ascending) - objektumokat ad vissza
     utana pedig filterCarsByProductionDate => megnezeni hogy csak a 10 evnel fiatalabbak maradtak-e bent
     
- json file, pelda:
   {
    car-1 {
       id: 1,
       brand: "Ford"
       ...
     },
     car-2: {
     
     }
   }
  
  fileName = "input_test_set_1.json"
  db.load(fileName) => ez feltolti a myDict strukturat.

- Legkozelebb folytatjuk: egy helyen betenni a try-catch strukturat-exception handling
