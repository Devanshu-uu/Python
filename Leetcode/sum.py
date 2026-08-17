class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> int:
        reversel1 = ""
        reversel2 = ""
        
        # 1. Convert list elements to strings
        for i in l1:
            reversel1 += str(i)
        for j in l2:
            reversel2 += str(j)
            
        # 2. Add them as integers AFTER both loops finish
        ans = int(reversel1) + int(reversel2)
        return ans


l1 = [2, 2, 3]  # Represents 223
l2 = [5, 2, 3]  # Represents 523

a = Solution()
print(a.addTwoNumbers(l1, l2))  # Output: 746 (223 + 523)