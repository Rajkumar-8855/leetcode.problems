class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        a=0
        for i in pushed:
            stack.append(i)
            while stack and a<len(pushed) and  stack[-1]==popped[a]:
                stack.pop()
                a+=1
            
        return a==len(popped)
                       
        