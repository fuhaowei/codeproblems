class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        store = {}
        stack.append((0,nums2[0]))

        for idx in range(1,len(nums2)):
            while stack and nums2[idx] > stack[-1][1]:
                idx2, number = stack.pop()
                store[number] = nums2[idx]
            stack.append((idx, nums2[idx]))


        ans = []
        for number in nums1:
            if number not in store:
                ans.append(-1)
            else:
                ans.append(store[number])

        return ans



        #create stack        
        #pass through the array from left to right
            #if the element is bigger then what's on the stack, pop off all the way until we reach a bigger element
                #add that index into a res array


            #if smaller, then just add onto stack

            #get index of nums1 using find, then create final result arr 


