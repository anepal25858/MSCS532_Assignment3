# Implementing a Hash Table using chaining for collision resolution
class HashTable:
    def __init__(self, initial_capacity = 5):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1

        # Resizing the table only when 75% of the slots are filled
        if self.load_factor() > 0.75:
            self._resize()

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                self.size -= 1
                return True
        return False

    def load_factor(self):
        return self.size / self.capacity
# Since We setup the initial capacity as 5 and have 4 output which is more than 75%,
# resize function will double the slot from 5 to 10 as shown in output
    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]

        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_capacity
                new_table[new_index].append([key, value])

        self.capacity = new_capacity
        self.table = new_table

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Test
hash_table = HashTable()

# Insert
hash_table.insert('A', 100)
hash_table.insert('B', 150)
#hash_table.insert('C', 200)
hash_table.insert('D', 250)

# Search
A = hash_table.search('A')
B = hash_table.search('B')
E = hash_table.search('E')

# Delete
hash_table.delete('B')
deleted_B = hash_table.search('B')

# final state
hash_table.display()


