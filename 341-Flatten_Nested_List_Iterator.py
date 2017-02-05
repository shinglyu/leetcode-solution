# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#Using a stack of [list, index] pairs.

# class NestedIterator(object):
#
#     def __init__(self, nestedList):
#         self.stack = [[nestedList, 0]]
#
#     def _curr_stack(self): # curr_list, index
#         return self.stack[-1]
#
#     def _advance_curr_index(self):
#         self.stack[-1][1] += 1
#
#     def next(self):
#         self.hasNext()
#         nestedList, i = self._curr_stack()
#         self._advance_curr_index()
#         return nestedList[i].getInteger()
#
#     def hasNext(self):
#         # Will make sure the current stack is an integer
#         s = self.stack
#         while s:
#             # Until we find the next integer
#             nestedList, i = self._curr_stack()
#             if i == len(nestedList):
#                 s.pop()
#             else:
#                 x = nestedList[i]
#                 if x.isInteger():
#                     return True
#                 else:
#                     self._advance_curr_index() # Next time we get back to this level, we'll need to process the next element
#                     s.append([x.getList(), 0])
#         return False

class NestedIterator(object):

    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)

    def next(self):
        return self.value

    def hasNext(self):
        try:
            self.value = next(self.gen)
            return True
        except StopIteration:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
