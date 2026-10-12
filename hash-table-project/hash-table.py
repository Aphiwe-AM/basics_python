class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum([ord(char) for char in string])

    def add(self, key, value):
        hashed_value = self.hash(key)

        if hashed_value not in self.collection:
            self.collection[hashed_value] = {}

        self.collection[hashed_value][key] = value


table = HashTable()
table.add("software developer", "Aphiwe")
print(table.collection)