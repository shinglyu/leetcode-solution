class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort() # sort it first O(nlogn)
        half_size = len(nums[::2]) # get the first half size
        nums[::2], nums[1::2] = nums[:half_size][::-1], nums[half_size:][::-1] # revert the smaller half and larger half, then put the reversed smaller half in position 0, 2, 4... and reversed larger half in 1,3,5...
        # reversing the halfs make sure the larger part of the smaller half is in the front, and the smaller part of the larger half is in the end, so there is minimal chance that we'll have equal or close numbers placed next to each other.
        # Proof using the location of the median: https://discuss.leetcode.com/topic/32861/3-lines-python-with-explanation-proof/27

# Another idea:

# The "baseline" for the wiggling property is the median number, if we pick numbers above then below median repeatedly, we get a wiggling sequence.

# So the first is to find the median, then do a three way partitoning of the numbers, put the numbers smaller than the median to one side, the bigger to the other side. Then if let's say we have 

# index 0 1 2 3 4 5 6 (3 is the median)

#Then we can order them as 

#4   5  6
#   0   1  2  3 => 4 0 5 1 6 2 3

# We can do the three way partition first, then reorder, or we can modify the three way partition and put the number in the right place right away.

