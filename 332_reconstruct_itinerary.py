# The pitfall is that if you start from the smaller lexical order candidate, it
# might not end in a valid path. So if you reach a dead end, you need to
# "rollback" to the previous state. We use a recursion to do that, notice that
# we iterate through the possible candidate, remove it and add it back in case a
# rollback happens
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        starts = [ ticket for ticket in tickets if ticket[0] == "JFK"]
        for start in sorted(starts):
            tickets.remove(start)
            output = self.find_rec([start], tickets)
            if output is not None:
                return output
            else:
                tickets.append(start)
        return []

    def find_rec(self, itinerary, rem_tickets):
        if len(rem_tickets) == 0:
            return [ticket[0] for ticket in itinerary]+ [itinerary[-1][1]]
        next_from = itinerary[-1][1]
        next_tickets = [ticket for ticket in rem_tickets if ticket[0] == next_from]
        for next_ticket in sorted(next_tickets):
        #                  ^ remember to sort
            rem_tickets.remove(next_ticket)
            output = self.find_rec(itinerary + [next_ticket], rem_tickets)
            if output is not None:
                return output
            else:
                # put it back if we failed
                rem_tickets.append(next_ticket)
        # if we tested every candidate and still can't find a valid one, we are
        # at a dead end, rollback
        return None


# A more elegant solution, see
# https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c/4

# Explanation
#
# First keep going forward until you get stuck. That's a good main path already.
# Remaining tickets form cycles which are found on the way back and get merged
# into that main path. By writing down the path backwards when retreating from
# recursion, merging the cycles into the main path is easy - the end part of the
# path has already been written, the start part of the path hasn't been written
# yet, so just write down the cycle now and then keep backwards-writing the path.

# Example:
# Step 1
#                B
#
#
#         D     <--     C
#           \           ^
#            +-------+  |
#                    v  |
#         JFK   -->     A
#
# Step 2
#         +-->   B -----+
#         |             v
#
#         D             C
#         ^          /  ^
#         | +-------+   |
#           v
#         JFK           A
#
# From JFK we first visit JFK -> A -> C -> D -> A. There we're stuck, so we
# write down A as the end of the route and retreat back to D. There we see the
# unused ticket to B and follow it: D -> B -> C -> JFK -> D. Then we're stuck
# again, retreat and write down the airports while doing so: Write down D before
# the already written A, then JFK before the D, etc. When we're back from our
# cycle at D, the written route is D -> B -> C -> JFK -> D -> A. Then we retreat
# further along the original path, prepending C, A and finally JFK to the route,
# ending up with the route JFK -> A -> C -> D -> B -> C -> JFK -> D -> A.

import collections
class Solution(object):
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list) # inits an empty default value
        # using the given factory function "list()"
        for a, b in sorted(tickets, reverse=True):
            # sort it reversely, so smaller lexical order item goes to the end
            # (because we want to pop() from the end later)
            targets[a].append(b),
            # generates a dict of (key: from) -> (value: [ to_3, to_2, to_1])
            route = []
        def visit(airport):
            # for every potential path
            while targets[airport]:
               # get the smallest lexical order item from the end
               visit(targets[airport].pop())
            # we are at a dead end, so we rollback, but the path all the way
            # up to the branching point must be a valid suffix, otherwise we
            # won't be reaching a dead end, so we record the route from the end
            route.append(airport)
        visit('JFK')
        return list(reversed(route)) # or use route[::-1]
