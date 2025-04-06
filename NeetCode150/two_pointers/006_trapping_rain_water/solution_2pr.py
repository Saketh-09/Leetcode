class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l= 0
        r=len(height)-1
        lmax = height[l]
        rmax = height[r]
        ans = 0
        while l<r:
            if height[l]<=height[r]:
                l+=1
                if height[l]>lmax:
                    lmax = height[l]
                else:
                    ans+=lmax-height[l]
            else:
                r-=1
                if height[r]>rmax:
                    rmax = height[r]
                else:
                    ans+=rmax-height[r]
        return ans
            
