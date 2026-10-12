class HashTable:
    def __init__(self):
        self.collections = {}

    def hash(self, string):
        return sum([ord(char) for char in string])

table = HashTable()
print(table.hash("mouse"))