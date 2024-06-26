import pygame

from Zone import *
from utils import *

class Map:

    def __init__(self, grid_width, grid_height, zone_width, zone_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.zone_width = zone_width
        self.zone_height = zone_height
        self.zones = [[Zone(zone_width,zone_height,x,y) for x in range(grid_width)] for y in range(grid_height)]

    def populate_map(self, max_plants_per_zone):
        for row in self.zones:
            for zone in row:
                num_plants = random.randint(0, max_plants_per_zone)
                zone.populate_zone(num_plants)

    def draw(self, window):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rect = pygame.Rect(x * self.zone_width, y * self.zone_height, self.zone_width, self.zone_height)
                pygame.draw.rect(window, (255, 255, 255), rect, 1)  # Dessiner les bordures de chaque zone

    def getPlant(self,position):
        zone = self.zones[int(position[1])][int(position[0])]
        listPlants = zone.getPlants()
        rand = random.randint(0,zone.getNbPlant()-1)
        return listPlants[rand]
        
    def getListePlant(self,position):
        zone = self.zones[int(position[1])][int(position[0])]
        listPlants = zone.getPlants()
        
        return listPlants

    def getNbPlantZone(self,position):
        zone = self.zones[int(position[1])][int(position[0])]
        return zone.getNbPlant()
        
    def printMap(self):
        for row in self.zones:
            print("")
            for zone in row:
                zone.printZone()
                
        print("==================================================================================================================")
    
    def printPlanteMap(self):
        for row in self.zones:
            print("")
            for zone in row:
                zone.printListePlante()
        print("==================================================================================================================")