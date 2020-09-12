1. Hashing functions
    - TBD
2. Collision resolution
    - In case there are instances where multiple values can be assigned to the same reference/index, we want to save both values for the same index instead of re-writing it. This can be done by either saving multiple index-to-values {3=val1, 3=val2,..., 3=valn}, or create an array of values at an index {3 = [val1, val2,..., valn]}
3. Performance of basic hash table operations
    - Average case of hash tables typically take up O(1) time, but WORST CASE CONDITIONS will be O(n)
4. Load factor
    - Load Factor = (Items in hash Table)/(Number of slots). So an array with length = 20, and there are 4 different values, give a load factor of 5 (20/4=5); if the different values were equal to the length of the array (20 different value), load factor would be 1
5. Automatic resizing
    -
6. Various use cases for hash tables
    -