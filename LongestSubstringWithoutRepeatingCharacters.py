# Time Complexity : O(n) 
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# traversing the given string s to check all possible substrings using start pointer
# start starts from 0, and we take the length of substring from 0 to n - 1
# instead of checking if the current character is a repeat character, we store every character in a hashmap
# so that the search is constant
# key in hashmap - the character we have already seen
# value - in case of repeating character, where should the next substring start from (i + 1)
# as we move along, if we have not seen a character before, we add it in the map - s[i], i+1
# if we have seen the character before, we move our start to map[s[i]]
# however if map[s[i]] < start (the value that comes out of the map is smaller than current start) - this means moving backwards
# but we will get repitions if we move backwards, because would have seen some repitions to come at the current start
# so we need to make sure we do not move backwards
# thus start changes to max(start, map[s[i]])
# we maintain the max length of longest substring, by checking length of every substrig, and updating maxx if the length of the current string (from start to i) is greater than max
# at the end we return max

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        
        start = 0
        maxx = 0
        map = {}
        # traversing over the string given
        for i in range(len(s)):
            # current character
            c = s[i]
            # if it exists in map
            if c in map:
                # update start
                start = max(start, map[c])
            # update max
            maxx = max(maxx, i - start + 1)
            # and add/update the value of the character in the map
            map[c] = i + 1
        
        return maxx