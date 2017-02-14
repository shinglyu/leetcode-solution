# Too slow
class Solution(object):
    def _isValidList(self, preorder):
        #print preorder
        if preorder == ["#"]:
            return True
        if preorder[0] == "#":
            return False
        subtree_strings = preorder[1:]
        #print(subtree_strings)
        for split_index in range(1, len(subtree_strings),2): # min is "#", max is everything except the right child "#"
            left, right = subtree_strings[:split_index], subtree_strings[split_index:]
            print(left, right)
            if self._isValidList(left) and self._isValidList(right):
                return True
        return False
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        return self._isValidList(preorder.split(","))

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        indeg = -1 # Indegree, vertex that points "in" to a node; root has no indegree so we compensate it by -1
        outdeg = 0 # Outdegree, vertex that point "out" from a node
        for node in nodes:
            indeg += 1 # every node contributes to 1 indegree, except root; But we +=1  for root too, so we compensentae it by -1
            if outdeg - indeg < 0: # if we run out of outdegree, this can't be a valid tree
                return False
            if node != "#":
                outdeg += 2 # If it's an internal node, it contributes to 2 outdegree in addition to the 1 indegree already added earlier
        return indeg == outdeg # For every "out" there is an corresponding "in", so the number must equal

# We could also use one variable difd = outdeg - indeg, and += and -= it instead
# of handling two variables

