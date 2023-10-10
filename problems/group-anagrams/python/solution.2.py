""""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict


#
# The complexity is O(m*n)
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        _output = defaultdict(list)
        for str in strs:
            count = [0] * 26 # a ... z
            for c in str:
                # ord('a') --> 97
                #
                # if we have ord('a') - ord('a') --> 0 so we take first element of the array
                # if we have ord('c') - ord('a') --> 2 so we take third element of the array
                # if we have ord('z') - ord('a') --> 25 so we take last element of the array
                count[ord(c) - ord('a')] += 1
            _output[tuple(count)].append(str)
        return _output.values()




# Examples
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

solution = Solution()

result = solution.groupAnagrams(strs)
print(result)