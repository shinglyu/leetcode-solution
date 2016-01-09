/*
O(n2) runtime, O(1) space – Brute force:

The brute force approach is simple. Loop through each element x and find if there is another value that equals to target – x. As finding another value requires looping through the rest of array, its runtime complexity is O(n2).

O(n) runtime, O(n) space – Hash table:

We could reduce the runtime complexity of looking up a value to O(1) using a hash map that maps a value to its index.
*/

/* 
My solution: 

Idea: Create a map of <value in nums, its index> so we can find the required (target - nums[idx2]) value in O(1)

for (every idx2 from 0 to end){
  Try to find (target - num[idx2]) in the map
  if found, it would be the idx1 value. Return.
  if not found, insert the new idx2 value to the map
}
*/

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {
      map<int, int> remain_2_idx;
      for (int idx2 = 0; idx2 < nums.size(); ++idx2){
        try {
          int idx1 = remain_2_idx.at(target - nums[idx2]);
          vector<int> ans = {idx1+1, idx2+1};
          return ans;
        }
        catch (const out_of_range& e) {
          remain_2_idx.insert(pair<int, int>(nums[idx2],idx2));
        }
      }
    }
};
