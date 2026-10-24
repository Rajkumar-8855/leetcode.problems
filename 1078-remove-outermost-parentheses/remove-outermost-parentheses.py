class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        a=0
        for i in s:
            if i =="(":
                if a>0:
                    stack.append(i)
                a+=1
            else:
                a-=1
                if a>0:
                    stack.append(i)


        return "".join(stack)




                
        