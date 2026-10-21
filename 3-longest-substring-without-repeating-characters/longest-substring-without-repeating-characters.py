class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=""
        length=0
        for i in range(len(s)):
            if s[i] not in a:
                a+=s[i]
            else:
                a=a[a.index(s[i])+1:]
                a=a+s[i]
            length=max(length,len(a))
        return length
        