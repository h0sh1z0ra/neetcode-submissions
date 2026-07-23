class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']':'[', '}':'{'}

        for char in s:
            if char in closeToOpen:
                if len(stack)!=0 and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True

        else:
            return False