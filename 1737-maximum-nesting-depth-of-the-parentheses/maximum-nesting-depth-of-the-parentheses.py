class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count=0
        count=0
        for i in s:
            if i == "(":
                count+=1
                if count > max_count:
                    max_count=count
            elif i ==")":
                count-=1
        return max_count

        