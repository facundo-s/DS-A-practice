class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if not stack:
                stack.append(char)
                continue
            if char == stack[-1]:
                stack.pop()
                continue
            stack.append(char)
        return "".join(stack)
        
        # stack = [S]
        # while stack:
        #     word = stack.pop()
        #     if word == "":
        #         break
        #     last_letter = word[0]
        #     for i in range(1,len(word)):
        #         #iterate over all the letters to find a duplicate
        #         #if a duplicate is found, remove it, add it to the stack
        #         if word[i] == last_letter:
        #             stack.append(word[:i-1]+word[i+1:])
        #             break
        #         last_letter = word[i]
        #     if not stack:
        #         #if after checking the word for duplicates, none is found, exit loop
        #         break
        # return word
                