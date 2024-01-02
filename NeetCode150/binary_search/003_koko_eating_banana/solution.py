class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        r = max(piles)
        l = 1
        k = r

        while l<=r:
            m = (l+r)//2
            hours = 0
            for p in piles:
                hours += p/m if p%m==0 else p//m+1
            if hours <= h:
                k = min(k,m)
                r = m-1
            else:
                l = m+1
        return k
