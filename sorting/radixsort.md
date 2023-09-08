Radix Sort is a non-comparative integer sorting algorithm that distributes elements into buckets according to individual digits. It processes the digits from the least significant to the most significant. Here's how the algorithm works:

### Algorithm Steps:

1. **Identify the Maximum Element**: Determine the maximum element in the array to find the number of digits needed (`maxDigits`).

2. **Loop Through Each Digit**: For each digit \(i\) from the least significant digit (LSD) to the most significant digit (MSD), perform the following steps:

    a. **Distribution**: Place each element into a bucket corresponding to the \(i^{th}\) digit.
    
    b. **Collection**: Collect the numbers back from the buckets, overwriting the input array.
    
3. **Return the Sorted Array**: The array will be sorted after the last iteration.

### Example Code in Python:

Here is an example code snippet illustrating the Radix Sort algorithm in Python:

```python
def counting_sort(arr, digit_getter):
    count = [0] * 10
    output = [0] * len(arr)
    
    for num in arr:
        index = digit_getter(num)
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = len(arr) - 1
    while i >= 0:
        index = digit_getter(arr[i])
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    return output

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        arr = counting_sort(arr, lambda num: (num // exp) % 10)
        exp *= 10
    
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array:", radix_sort(arr))
```

### Time Complexity:

- **Average Case**: \(O(n \cdot k)\)
- **Worst Case**: \(O(n \cdot k)\)
- **Best Case**: \(O(n \cdot k)\)

Here, \(n\) is the number of elements and \(k\) is the number of digits in the maximum number.

### Space Complexity:

- **Space Complexity**: \(O(n + k)\)

Radix Sort uses additional space for the counting array and the output array, leading to a space complexity of \(O(n + k)\).

### Advantages:

- Radix Sort is fast for numbers and strings.
- It's stable, which means that two objects with equal sort keys appear in the same order in the sorted output as they appear in the input array.

### Disadvantages:

- The algorithm is restricted to integers and some types of floating-point numbers.
- The constant factors hidden in the \(O(n \cdot k)\) time complexity can be substantial.

Let me know if you would like to dive deeper into any aspect of Radix Sort!