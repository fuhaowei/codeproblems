#heap

-> data structure mainly used to represent a pq, represented as a binary tree. heaps are complete binary trees.

-> 2 types of heaps -> min heap (parent node always smaller value than child nodes), max heap (parent node always larger value than child nodes)

-> if type not mentioned, refers to minheap -> python is minheap default. just use -ve values to make it maxheap, but just pop out wtv that comes out

-> heap operations:
    -> heapify -> used to create a heap from an array
    -> hq.heappush(heap, value)-> inserts a new element into the heap (O(LOG(N) time complexity)) -> rmbr heap keeps the height log right
    -> extract -> returns the min/max element from the heap
    -> delete -> deletes an element from the heap
    -> decrease/increase key -> decreases/increases the value of a key in the heap
    -> merge -> merges 2 heaps into 1 heap
    -> build heap -> used to create a heap from an array
    -> heap sort -> used to sort an array



## time complexities
-> heapify is o(n), pushing or popping is logn, nlargest or smallest is nlogk.

1. **Heap Construction**: `heapq.nlargest` starts by taking the first \(k\) elements from the iterable and heapifying them into a min-heap. Heapifying \(k\) elements will take \(O(k)\) time.
   
2. **Iterating and Maintaining Heap**: It then iterates over the remaining \(n-k\) elements. For each new element, it's compared to the smallest (root) element of the heap.
   - If it's larger, it replaces the root and then the heap is adjusted (heapify down operation) to maintain the heap invariant. The time complexity for this step is \(O(\log k)\) since it involves deleting the smallest element and inserting a new one, each taking \(O(\log k)\).


### seems to be this strategy -> maintaining like a certain k size of heap, so pushing or popping would be like log k instead of repeatedly calling



```
import heapq as hq
# Simple array is heap
minHeap = []
hq.heapify(minHeap)
# Adding an element to the heap
hq.heappush(minHeap, 5)

#since minheap, will remove the smallest value 2
value = hq.heappop(minHeap)

```


4 patterns where i use a heap!

1. Top K Pattern
    -> kth largest numebr in array
    -> top k frequent words
2. Merge K sorted pattern
    -> merge k sorted.. haha
    -> k pairs with smallest sum
3. 2 heaps pattern
    -> find median from data stream
4. minimum number pattern
    -> meeting rooms 2



Top K Pattern

LC #215 - Kth largest number in an array
LC #973 - K closest points to origin
LC #347 - Top k frequent elements/numbers
LC #692 - Top k frequent words
LC #264 - Ugly Number II
LC #451 - Frequency Sort
LC #703 - Kth largest number in a stream
LC #767 - Reorganize String
LC #358 - Rearrange string K distance apart
LC #1439 - Kth smallest sum of a matrix with sorted rows

Merge K sorted pattern

LC #23 - Merge K sorted
LC #373 - K pairs with the smallest sum
LC #378 - K smallest numbers in M-sorted lists

Two Heaps Pattern

LC #295 - Find median from a data stream
LC #480 - Sliding window Median
LC #502 - Maximize Capital/IPO

Minimum number Pattern

LC #1167 - Minimum Cost to connect sticks/ropes
LC #253 - Meeting Rooms II
LC #759 - Employee free time
LC #857 - Minimumcost to hire K workers
LC #621 - Minimum number of CPU (Task scheduler)
LC #871 - Minimum number of Refueling stops


#implementing heaps

-> simple array can be used to represent a heap where array indecies refer to the node positions in the tree.
-> parent and child nodes can be accessed with indices -> root node is i = 0, parent node is parent(i) = (i-1)/2, left child is left(i) = 2i + 1, right child is right(i) = 2i + 2

-> if you heapify a list in python and go print that, you will see this represented


# follow ups -> O(n) non-heap solution involving quick-select and Lomuto's partition algorithm 