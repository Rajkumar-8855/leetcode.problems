class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        s=sum(arr[:k])
        count=0
        avg=s/k
        if avg>=threshold:
            count+=1
        for i in range(k,len(arr)):
            s=s+arr[i]-arr[i-k]
            avg=s/k
            if avg>=threshold:
                count+=1

        return count        

            
        