#act no need bounds -> mid never gets to 0 or len(arr) - 1

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)

        def cond(idx): 
            
            if arr[idx -1] < arr[idx] > arr[idx + 1]:
                return 0

            #if left or right bound

            # if idx == 0:
            # #left bound, skip checking left side
            #     return 1

            # if idx == len(arr) - 1:
            # #right bound, skip checking right side
            #     return -1

            #not a bound, check both
            if arr[idx -1] < arr[idx] < arr[idx + 1]:
                return 1

            if arr[idx -1] > arr[idx] > arr[idx + 1]:
                return -1
            

        while low < high:
            mid = (low + high) // 2
            res = cond(mid)
            if res == 0:
                return mid

            elif res == -1:
                high = mid

            else:
                low = mid + 1
                
        return -1