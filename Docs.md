Part 1: Randomized Quicksort Analysis

1. Implementation
Please review Random-QS.py to see the implementation of Randomized Quicksort and Deterministic Quicksort.
The implementation is efficient and handles various edge cases, such as arrays with
reverse array, repeated elements, empty arrays, and already sorted arrays.

2. Analysis
The average time complexity of Randomized Quicksort is O(nlogn).
The random pivot prevents the worst-case scenario.
In deterministic Quicksort the unbalance partitions can lead to O(n^2)

3. Comparison
Please check the output to verify the below comparison:

-Randomly Generated arrays
Both algorithm perform similar performance on average, though Randomized Quicksort have little bit better consistency.
-Already Sorted Arrays
Randomized Quicksort is faster than Deterministic Quicksort.
-Reverse Sorted Arrays
Randomized Quicksort outperform Deterministic Quicksort.
-Arrays with repeated elements
Randomized Quicksort outperform Deterministic Quicksort.

4. Observation
Randomized Quicksort generally performs better or more consistently because
it avoids the worst-case scenario through random pivot selection.
Deterministic Quicksort (using the first element as a pivot) performs poorly
on already sorted and reverse sorted arrays, demonstrating the O(n^2) worst case.


Part 2: Hashing with Chaining

1. Implementation
Please check file HashChain.py for implementation of hash table using chaining for collision resolution.
The implementation support all 3 operations: Insert, Search, Delete.

2. Analysis
Time Complexity for these 3 operation is O(1) with worst case scenario of O(n).
The load factor do affects the performance of these 3 operations.
A higher load factor increases collisions and search time, while lower load factor maintains effective operations.
Resizing the table will help to keep the load factor low and reduce the chance of collision.
In this case, I have set the load factor to 75%, so whenever the the slots exceed 75% the size of table is doubled.
See reference in Readme.md file.


