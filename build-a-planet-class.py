** start of main.py **

class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        #raise type error if arguments are non strings
        if not isinstance(self.name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        
        #raise a value error 
        if not self.name or not self.planet_type or not self.star:
            raise ValueError("name, planet_type, and star must be non-empty strings")

# method about the orbit of the planet
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

# str method
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

# make three instances of planet
planet_1 = Planet('mars', 'small', "nep")
planet_2 = Planet('jupiter', 'big', 'zara')
planet_3 = Planet('neptune', 'medium', 'none')

# print all three orbit methods
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

# call str function on all three instances
print(planet_1)
print(planet_2)
print(planet_3)
        






** end of main.py **

