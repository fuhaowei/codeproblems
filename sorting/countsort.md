### Counting Sort Algorithm

Counting Sort is a non-comparison-based sorting algorithm that sorts integers within a specific range. It is particularly effective when the range of the input values is limited.

#### How It Works:

1. **Determine the Range:** Find the minimum and maximum values among the input elements.
2. **Initialize Count Array:** Create an array of zeros with a length equal to the range of input values.
3. **Count Occurrences:** Traverse the input array and for each element, increment its corresponding index in the count array.
4. **Cumulative Count:** Update the count array such that each element at each index stores the sum of the previous counts.
5. **Sort:** Use the count array to place the elements into their sorted position in a new array.

#### Time Complexity:
- **Average Case:** \( O(n+k) \)
- **Worst Case:** \( O(n+k) \)
- **Best Case:** \( O(n+k) \)

Here \( n \) is the number of elements in the input array and \( k \) is the range of the input.

#### Space Complexity:
- **Worst Case:** \( O(n+k) \)

### Code Example in Python:

Here's a highly organized Python code snippet to demonstrate Counting Sort.

```python
def counting_sort(arr):
    # Step 1: Determine the Range
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    # Step 2: Initialize Count Array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Step 3: Count Occurrences
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # Step 4: Cumulative Count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Sort
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

# Test the function
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)
```

### Detailed Explanations:

1. **Determine the Range:** Knowing the range helps to create a `count` array of an appropriate size.
   
2. **Initialize Count Array:** A count array is initialized with zeros. The size of the array is equal to the range of elements.
   
3. **Count Occurrences:** We traverse through the input array `arr` and for every element `arr[i]`, increment `count[arr[i] - min_val]`.
  
4. **Cumulative Count:** We transform `count` such that `count[i]` contains the number of elements less than or equal to `i`.
  
5. **Sort:** Elements are placed in their correct positions in the `output` array based on the `count` array. We then copy the sorted elements back into the original array.

I hope this detailed explanation and code meet your needs for thoroughness and organization. Let me know if you have any further questions!