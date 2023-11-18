class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        #stack, but the stack doesn't have to be that thing
        #we can track the top k via some shit

        count_stack = []
        stack = []

        for letter in s:
            if stack and stack[-1] == letter:
                stack.append(letter)
                count_stack[-1] += 1
                while count_stack and count_stack[-1] == k:
                    for _ in range(k):
                        stack.pop()
                    count_stack.pop()

            else:
                stack.append(letter)
                count_stack.append(1)

        return "".join(stack)