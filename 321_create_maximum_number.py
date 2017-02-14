class Solution(object):
    def maxN(self, nums, n):
        out = []
        drop_count = len(nums) - n
        for num in nums:
            # Using a drop means when we drop enough numbers, we just use the rest of the array
            while len(out) > 0 and drop_count > 0 and out[-1] < num: 
                out.pop()
                drop_count -= 1
            out.append(num)
        # But the rest of the array may be long, so trim it
        return out[:n]
        
    # merge sort style merge
    def merge(self, l1, l2):
        out = []
        while len(l1) > 0 or len(l2) > 0: # we could also just "for i in range(len(l1) + len(l2))"
            # compare the list (first element first) then pop
            # If we write (l1[0] > l2[0]) and any of the list is empty, we'll get index out of bound
            out.append(max(l1, l2).pop(0))
        return out
            
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        candidates = []
        for i in range(0, k+1):
            #print(i, k-i)
            if i > len(nums1) or k-i > len(nums2):
                continue
            #print(self.merge(self.maxN(nums1, i), self.maxN(nums2, k-i)))
            candidates.append(self.merge(self.maxN(nums1, i), self.maxN(nums2, k-i)))
        return max(candidates)
