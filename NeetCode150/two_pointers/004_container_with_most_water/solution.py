class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        l = 0
        r = len(height)-1
        while l < r:
            h = min(height[l],height[r])
            area = max(area, h*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return area