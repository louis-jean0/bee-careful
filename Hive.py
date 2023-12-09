class Hive:
    
    def __init__(self, position):
        self.position = position  # Position de la ruche sur la grille
        self.stored_pollen = 0  # Quantité actuelle de pollen stocké
        self.shared_memory = []
        self.bee_waiting_list = []  # Liste d'abeilles en attente d'instructions
        self.zone_tier_list = []    # Liste de priorité des zones
        self.bee_zone_list = []     # Liste de tuple (bee,zone,time) associant une abeille, sa zone ainsi que le temps qu'elle met, incrémenter dans updates()
        self.temp = 0

    def add_to_bee_waiting_list_init(self,bee):
        self.bee_waiting_list.append(bee)

    def zone_priority_list_init(self):
        # initialisation des priorités pour les zones
        
        # zone de la ruche en tête de liste
        self.zone_tier_list.append(self.position)
        pass

    def update(self):
        # Mettre à jour la ruche à chaque tick du jeu
        # Cela pourrait inclure des actions comme la production de nouvelles abeilles
        
        pass
        
    def store_pollen_from_bee(self, amount):
        # Ajouter du pollen au stockage, sans dépasser la capacité
        self.stored_pollen += amount

    def wait_order(self,bee):
        # Fonction appelé par une abeille lorsqu'elle attend une action
        self.bee_waiting_list.append(bee)
        
    def give_action(self):
        # Donne une action à la 1ère abeille dans la liste
        if self.bee_waiting_list:
            current_bee = self.bee_waiting_list[0]
            print(len(self.zone_tier_list))
            current_bee.set_target(self.zone_tier_list[self.temp].plants[0].position)
            self.temp += 1
            if self.temp >len(self.zone_tier_list):
                self.temp = 0
            
            
            self.bee_waiting_list.pop(0)
     
    def draw_hive(self, window, position, zone_width, zone_height, image):
        x = position[0] * zone_width
        y = position[1] * zone_height
        window.blit(image,(x,y))