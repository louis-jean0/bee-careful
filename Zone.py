import random
from Plant import Plant
from CarnivorousPlant import CarnivorousPlant

class Zone:
    def __init__(self,width,height,x,y):
        self.zone_id = (x,y)
        self.minX = width * x
        self.maxX = (width * (x+1))-1
        self.minY = height * y
        self.maxY = (height * (y+1))-1
        self.width = width
        self.height = height
        self.plants = []
        self.carnivorous_plants = []
        self.listPlantTotal = []
        self.has_carnivorous_plant = False
        self.nbPlante = 1
        self.nbCarniPlante = 0
        self.nbPlanteCooldown = 0
        self.score = 0

    def is_too_close(self, new_position, ecartPlante):
        for plant in self.plants + self.carnivorous_plants:
            if abs(plant.position[0] - new_position[0]) < ecartPlante and abs(plant.position[1] - new_position[1]) < ecartPlante:
                return True
        return False

    def populate_zone(self, num_plants_total):
        self.nbPlante = num_plants_total
        max_pollen = 500
        cooldown = 5000
        ecartPlante = 30

        for _ in range(num_plants_total):
            positionRandom = []
            while True:
                positionRandom = [random.randint(self.minX, self.maxX-50), random.randint(self.minY, self.maxY-50)]
                if not self.is_too_close(positionRandom, ecartPlante):
                    break

            if random.randint(0, 100) < 20:
                self.carnivorous_plants.append(CarnivorousPlant(positionRandom))
                self.listPlantTotal.append(CarnivorousPlant(positionRandom))   
            else:
                self.plants.append(Plant(positionRandom, max_pollen, cooldown))
                self.listPlantTotal.append(Plant(positionRandom, max_pollen, cooldown))

        self.has_carnivorous_plant = len(self.carnivorous_plants) > 0

    def random_position(self):
        return [random.randint(self.minX, self.maxX-50), random.randint(self.minY, self.maxY-50)]
    
    def getMinX(self):
        return self.minX

    def getMaxX(self):
        return self.maxX

    def getMinY(self):
        return self.minY

    def getMaxY(self):
        return self.maxY

    def getPlants(self):
        return self.listPlantTotal
    
    def getNbPlant(self):
        return self.nbPlante
        
    def analyseZone(self,position):
        
        return self.zone_id[0] == position[0] and self.zone_id[1] == position[1] 
        
    def getNbPlantesOccupee(self):
        occupee = 0
        
        for plant in self.plants:
            
            if plant.IsOccupee or plant.onCooldown:
                occupee += 1
        return occupee
        
    def printZone(self):
        print("Zone : ",self.zone_id,"  self.nbPlante = ", self.nbPlante,"  self.nbCarniPlante = ",self.nbCarniPlante,"self.nbPlanteCooldown = ",self.nbPlanteCooldown,"self.score = ",self.score)
        
    def printListePlante(self):
        for plant in self.plants:
            print(plant.IsOccupee,"    ",plant.onCooldown)
        print("*******************************************")
        