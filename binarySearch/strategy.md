## Binary Search solutions:

1.  Firstly, on the size of the arbitary n.

    > If bigger than 1x10*18: have to binary search, O(logn).

    > If smaller than 1x10*7: linear search starts being possible, O(n).

    > If smaller than  1x10*6: we need o(nlogn)

    > If smaller than 1x10*3: we can use O(n^2) algorithms.


2. To make sure that BS can be used, we need to make sure that our problem space is monotonic, which explains why you have to sort the array first.
    > BS however also works on functions rememeber: if function is monotonically increasing or decreasing, then you can use binary search to find the answer. For example, find the smallest x such that f(x) >= k, or find the largest x such that f(x) <= k.

    > For example,koko eat bananas is monotic, because if you can eat all the bananas in h hours, then you can eat all the bananas in h+1 hours. 

3. If our question was about minimum integers, use floor divide. you can't have 2.2, so the minimum possible integer is 3. This is simply // in python.

4. If our question was about maximum integers, use ceiling divide. you can't have 2.2, so the maximum possible integer is 2. We then use  return (n + d - 1) // d \
The idea is to translate the numerator upwards so that floor division rounds down to intended ceiling, but only works with integers of course.



generalized:

```
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

```


000111
-> to find first 1 floor divide
to find last 0 ceil divide