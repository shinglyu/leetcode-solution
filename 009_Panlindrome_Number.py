class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        lptr = 1
        rptr = 1
        
        if (x < 0):
            return False
        while (x / lptr > 0):
            if (x / lptr / 10 > 0):
                lptr *= 10
            else:
                break
        
        while lptr > rptr:
            if (x / lptr % 10 != x / rptr % 10):
                return False
            lptr /= 10
            rptr *= 10
        return True
            
