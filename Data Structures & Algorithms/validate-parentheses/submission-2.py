class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for i in range(len(s)):
            if(len(stack)==0):
                stack.append(s[i])
            else: 
                if(s[i] == "]" and stack[-1] == "[" 
                or s[i] == ")" and stack[-1] == "(" 
                or s[i] == "}" and stack[-1] == "{"):
                    stack.pop() 
                else:
                    stack.append(s[i])

        return len(stack) == 0
    



        

