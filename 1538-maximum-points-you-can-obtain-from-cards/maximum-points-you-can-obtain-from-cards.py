class Solution(object):
    def maxScore(self, c, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total=sum(c)
        a=len(c)
        if k==a:

            return total

        left=0
        right=a-1
        score=sum(c[:k])
        max_sum=score
        for i in range(1,k+1):
            score=score - c[k-i]+c[a-i]
            max_sum=max(max_sum,score)
        return max_sum
        