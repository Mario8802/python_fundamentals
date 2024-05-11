class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, None)


hash_table = HashTable()
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("orange", 3)

print("Value for 'banana':", hash_table.search("banana"))  # Output: 7
print("Value for 'grape':", hash_table.search("grape"))    # Output: None
