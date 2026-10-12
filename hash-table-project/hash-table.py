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

    def remove(self, key):
        hashed_value = self.hash(key)

        if hashed_value not in self.collection:
            return "Member not found"

        self.collection[hashed_value].pop(key, "Member not found")

        if self.collection[hashed_value] == {}:
            del self.collection[hashed_value]

    def lookup(self, key):
        hashed_value = self.hash(key)

        if hashed_value in self.collection:
            if key in self.collection[hashed_value]:
                return self.collection[hashed_value][key]
        
    


table = HashTable()
table.add("Aphiwe", "full stack software developer")
table.add("ewihpA", "developer")
print(table.lookup("Aphiwe"))
print(table.collection)
table.remove("lubonati")
print(table.lookup("ewihpA"))
print(table.collection)