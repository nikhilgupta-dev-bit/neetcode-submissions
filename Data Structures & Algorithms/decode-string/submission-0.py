class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        #ab2[c]3[d]1[x]
        curr=""

        for i in s:
            if i!="]":# as we reach here we are at a point where we reach to innner side of the string 
                stack.append(i)
            else :
                curr=""
                while stack and stack[-1]!="[":
                    curr=stack.pop()+curr
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(curr*int(num))
        return "".join(stack)

            
            