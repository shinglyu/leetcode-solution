class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxarea = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxarea = max(maxarea, area)
				# We can early return if there is no chance for a bigger area left
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea

#Brute force: will exceed time limit

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for i in range(len(height)-1, 0, -1):
            for j in range(0, i):
                area = min(height[i], height[j]) * (i-j)
                maxarea = max(maxarea, area)
        return maxarea
