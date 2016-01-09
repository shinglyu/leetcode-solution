/* 
 * We have to helpers
 * rightMostOccurancePos is a hashmap: char => its right most occurance position
 * startPos is the starting point of the currently searching substring
 * 
 * Start from index 0, move idx along the string
 * if found new char, put its latest (right most) occurance index into the map
 * else if it's an existing one
 *   check if the current substring (from startPos to current idx) is the largest, if yes => increase the global largest record
 *   since we found an existing char, we "cut off" the old occurance of the char and start a new search from the right of the new string.
 *   e.g. if we've seen "xyzabc", then we see a "xyzabca", we cut off the old "a" and start from "b"
 *
 *   Finally, the string may terminate so the last startPos to the end may be a longer string than the maxSize recorded, hence the last max()
 *   
 *     
 */ 
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> rightMostOccurancePos;
        int startPos = 0; // Start position of the currently longest substring

        int maxSize = 0; 
        for (int idx = 0; idx < s.length(); ++idx){
          if (rightMostOccurancePos.find(s[idx]) == rightMostOccurancePos.end()){
            rightMostOccurancePos.insert(pair<char, int>(s[idx], idx));
          }
          else {
            if ((idx - startPos) >= maxSize){
              maxSize = (idx - startPos);
            }
              startPos = max(rightMostOccurancePos[s[idx]] + 1, startPos);
              rightMostOccurancePos[s[idx]] = idx;
          }
        }
        int lastSubstringSize = s.length() - startPos;
        return max(maxSize, lastSubstringSize);
    }
};
