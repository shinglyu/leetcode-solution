class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0:
            return "" # early return, otherwise the minlen min() will fail
            
        minlen = min(map(len, strs))
        for i in range(1, minlen+1): #The prefix can't be longer then the shortest string
            prefix = strs[0][0:i]
            for string in strs:
                if not string.startswith(prefix):
                    return prefix[:-1]
        return prefix #We might reach the case like ["a", "a"]
