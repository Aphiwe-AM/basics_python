class Character:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._health = 100
        self._mana = 50 
    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level
        
    
    #assign a health property
    @property
    def health(self):
        return self._health
    
    #health getter
    @health.setter
    def health(self, new_health):
        #set health retrictions 
        if new_health < 0:
            new_health = 0
        if new_health > 100:
            new_health = 100

        #assign self to new health
        self._health = new_health

    #assign mana property
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, new_mana):
        #mana retrictions 
        if new_mana < 0:
            new_mana = 0
        if new_mana > 50:
            new_mana = 50
        #set self mana to new mana
        self._mana = new_mana
     
     #function for leveling up
    def level_up(self):
        self._level += 1

        self._health = 100
        self._mana = 50
        print(f"You have leveled up to 'level' {self._level}")
    
    def __str__(self):
        return f'''Name: {self._name}
level: {self.level}
Mana: {self.mana}
Health: {self.health}
'''
    

    
rena = Character("rena")
rena.health -= 45
rena.mana -= 12
print(rena)
rena.level_up()
print(rena)