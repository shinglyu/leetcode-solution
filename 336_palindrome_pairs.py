# Take 1, too slow
class Solution(object):
    def isPalindrome(self, x, y):
        candidate = x + y
        half_size = len(candidate) / 2 # integer division
        if half_size == 0:
            return True
        return candidate[0:half_size] == candidate[-half_size:][::-1]
            
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                word_i = words[i]
                word_j = words[j]
                if len(word_i) > len(word_j):
                    long_word = word_i
                    short_word = word_j
                else:
                    long_word = word_j
                    short_word = word_i
                
                if short_word[::-1] in long_word:
                    if self.isPalindrome(word_i, word_j):
                       output.append([i, j])
                    if self.isPalindrome(word_j, word_i):
                       output.append([j, i])
        return output
        
# Take 2, too slow
class Solution(object):
    def isPalindrome(self, candidate):

        half_size = len(candidate) / 2 # integer division
        if half_size == 0:

            return True

        return candidate[0:half_size] == candidate[-half_size:][::-1]
            
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                word_i = words[i]
                word_j = words[j]
                if len(word_i) > len(word_j):
                    long_word, short_word = word_i, word_j
                    l, s = i, j
                elif len(word_i) < len(word_j):
                    long_word, short_word = word_j, word_i
                    l, s = j, i
                else: 
                    #print("same")
                    if word_i == word_j[::-1]:
                        output.append([i,j])
                        output.append([j,i])
                    continue
                #print(l, s)
                
                if len(short_word) == 0:
                    if self.isPalindrome(long_word):
                        output.append([l,s])
                        output.append([s,l])
                        continue
                if long_word[0:len(short_word)] == short_word[::-1]:
                    #print("match long perfix")
                    if self.isPalindrome(long_word[len(short_word):]):

                        output.append([l,s])
                if long_word[-len(short_word):] == short_word[::-1]: # mind that [-0:]
                    #print("match long suffix")
                    #print(long_word, short_word)
                    if self.isPalindrome(long_word[0:-len(short_word)]):

                        output.append([s,l])
        return output

# Final solution
def palindromePairs(self, words):
    d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), [] # create a dictionary of reversed word -> index
    # The reason we need to reverse it here is that later we want to find a word in the dict that is a reverse of perfix or postfix
    for i, w in enumerate(words):
        for j in xrange(len(w)+1): # xrange is a generator version of range, so it can lazily evaluate
            prefix, postfix = w[:j], w[j:]
            if prefix in d and i != d[prefix] and postfix == postfix[::-1]: # e.g. "abcdc" split to "ab" and "cdc", we want to find a word in the dict that reverse to "ab", then we have a match. And obviously itself dosen't count (i != d[prefix]).
                res.append([i, d[prefix]])
            if j>0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                res.append([d[postfix], i])
    return res 

# The complexity for the previous two is O(n^2) dispite some skipping. 
# The final solution is O(n* L^2), where L is the average word length. Because we need to interate through n words; for each iteration, we need to split the word in all possible ways, it's count is propotional to L, the for each split we need to do a fast hashmap search (This reduces the n factor in the slow methods) and do a O(L) reverse of the posfix or prefix in the if condition.
