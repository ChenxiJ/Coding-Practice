hashTableTry1 = [None] * 10

def insertTry1(hashTable, key, value):
    hashKey = hashingFunction(key)
    hashTable[hashKey] = value
    return hashTable

# collision when two keys return to the same slot in the hash table
# two methods: linear probing (some way to continue looking for empty slot)
# and chaining (multiple items in the same slot)

# chaining: implement hash table as a nested list (list inside a list)
hashTable = [[] for _ in range(10)]

# use a very simple modulo operator for hashing function
def hashingFunction(key):
    return key % len(hashTable)

def insertTry2(hashTable, key, value):
    hashKey = hashingFunction(key)
    hashTable[hashKey].append(value)
    return hashTable


# so far for self-implemented hashing function, python has built-in hashing function,
# mapping all the integer and string to one integer

def insert(hashTable, key, value):
    hashKey = hash(key) % len(hashTable)
    keyExists = False
    bucket = hashTable[hashKey]

    for i, kv in enumerate(bucket):
        k, v = kv
        #  this is because in the hash map, when same key comes, replace the old one
        if key == k:
            keyExists = True
            break
    if keyExists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))
    return hashTable

insert(hashTable, 10, 'Nepal')
insert(hashTable, 25, 'USA')
insert(hashTable, 20, 'India')
insert(hashTable, 20, 'UK')


def search(hashTable, key):
    hashKey = hash(key) % len(hashTable)
    bucket = hashTable[hashKey]
    for i,kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v


def delete(hashTable, key):
    hashKey = hash(key) % len(hashTable)
    keyExists = False
    bucket = hashTable[hashKey]

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            keyExists = True
            break
    if keyExists:
        del bucket[i]
    else:
        print('key not exsited')
    return hashTable