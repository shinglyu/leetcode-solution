class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxSize = 0;
        for (int idx = 0; idx < s.length(); ++idx){
          for (int len = maxSize; len < s.length() - idx; ++len) {
            
            //cout << idx << len << s.substr(idx, len) << endl;
            
            if (this->_noRepeat(s.substr(idx, len))){
              maxSize = len;
            }
            else {
                break;
                
            }
          }
        }
        return maxSize;
    }
private: 
    bool _noRepeat(string s){  
      map<char, int> contains;
      for (string::iterator idx = s.begin(); idx != s.end(); idx++){ 
        //cout << *idx << endl;
        //cout << contains.find(idx) << endl;
        map<char, int>::iterator it = contains.find(*idx);
        if (it == contains.end()){
            contains.insert(pair<char, int>(*idx, 1));
        }
        else {
            return false;
        }
      }
      return true;
    }
};
