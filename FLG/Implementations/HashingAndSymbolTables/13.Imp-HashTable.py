class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1           # muktiplier
        hv = 0             # hash value
        for ch in key:
            hv += mult * ord(ch)
        mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+ 1) % self.size
        return None

if __name__ == '__main__':
    ht = HashTable()
    ht.put("good", "eggs")
    ht.put("better", "ham")
    ht.put("best", "spam")
    ht.put("ad", "do not")
    ht.put("ga", "collide")
    for key in ("good", "better", "best", "worst", "ad", "ga"):
        v = ht.get(key)
    print(v)