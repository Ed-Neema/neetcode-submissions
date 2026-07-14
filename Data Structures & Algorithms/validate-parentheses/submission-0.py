class Solution:
    #edge cases
    #1. Empty string - True
    #2. All opening brackets
    #3. All closing brackets
    def isValid(self, s: str) -> bool:
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        stack = []

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            else:
                popped = stack.pop()
                if bracket == "]" and popped == "[":
                    continue
                elif bracket == "}" and popped == "{":
                    continue
                elif bracket == ")" and popped == "(":
                    continue
                else:
                    return False
        if len(stack) != 0:
            return False
        else: 
            return True


        