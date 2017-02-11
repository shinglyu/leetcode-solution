# brute force O(log_3 n)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rem = n
        while rem >= 3:
            if rem % 3 != 0:
                return False
            rem = rem/3
        if rem == 1:
            return True
        else:
            return False

# A cleaner solution:

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rem = n
        while rem % 3 == 0:
            rem = rem/3
        return rem == 1:

# Other thoughts: covert the number to base 3, if it's in a form 10000..0 then
# return true

# math.log(n, 3) % 1 == 0 << mind the percision problem

if n > 0: #Mind that log can't accept negative or zero
    return round(math.log(n, 3), 10) % 1.0 < (0.1 ** 10) # need rounding
    # or
    return n == round(3 ** round(math.log(n, 3))) # take log an power it back, with rounding

else:
    return False

# Find the largest 3's power within the Int limit x, then x % n must be 0
