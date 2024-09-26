def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=' ')

        for j in hashTable[i]:
            print('-->', end=' ')
            print(j, end=' ')

        print()


HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


insert(HashTable,10,'Riyadh')
insert(HashTable,25,'Makkah')
insert(HashTable,20,'Madinah')
insert(HashTable,9,'Jeddah')
insert(HashTable,21,'Dammam')
insert(HashTable,21,'Qaseem')

display_hash(HashTable)