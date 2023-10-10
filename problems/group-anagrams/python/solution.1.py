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

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        _output = {}

        if len(strs) < 1:
            return []

        for str in strs:
            k = ''.join(sorted(str))
            if k in _output:
                _output[k].append(str)
            else:
                _output[k] = [str]

        return list(_output .values())




# Examples
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

solution = Solution()

result = solution.groupAnagrams(strs)
print(result)
