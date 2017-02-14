class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
	    # Build a hashmap of "string" => bit array
        # The bit represents the characters ordered by their encoded order
        # (ord())
        # If a char exist, we flip its bit to 1
        # e.g. "abd" => 1011
        #               dcba
        charbits = {}
        for word in words:
            bit_pattern = 0
            for char in word:
                # shift an 1 to its correct index, "a" => 1, "b" => 2, etc.
                # Then "OR" it with the existing pattern
                bit_pattern |= (1 << (ord(char) - ord('a')))
                #                               ^ offset so that "a" is in index 0
                #print("{0:b}".format(bit_pattern))
            charbits[word] = bit_pattern


        # We start from the larger ones, so we can early return
        sorted_words = sorted(words, key=len, reverse=True) # copy, we could do this in-place
        max_size = 0
        for i in range(0, len(sorted_words)):
            # This early return is optional
            if len(sorted_words[i]) ** 2 < max_size:
                return max_size
            for j in range(i+1, len(sorted_words)):
              # Bitwise XOR will make it == 0 if they don't share chars
              if (charbits[sorted_words[i]] & charbits[sorted_words[j]]) == 0:
                    max_size = max(max_size, len(sorted_words[i]) * len(sorted_words[j]))
        return max_size
