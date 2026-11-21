
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        a=[]
        time=0
    
        for i in range(len(tickets)):
            a.append(i)
             
        
        while a:

            person=a.pop(0)
            tickets[person]-=1
            time+=1
            if tickets[person]:
                a.append(person)


            if person==k and tickets[person]==0:
                return time

        return time