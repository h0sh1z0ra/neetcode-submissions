class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {')': '(', ']':'[', '}':'{'}

        for char in s:
            # ========================================================
            # If length of stack isn't 0, and the close bracket character
            # is in the hashmap, pop it from the stack. If the stack is length 0
            # when the close bracket is seen, that means there's no open bracket
            # (and vice versa); thus false. Else, if it's not yet in the stack,
            # append it
            # ======================================================== 
            if char in bracketMap:
                if len(stack) != 0 and stack[-1] == bracketMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0