'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
###########################################################################################
'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:
Input:
s = "aaabb", k = 3
Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input:
s = "ababbc", k = 2
Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
###########################################################################################
'''
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations or citations == [0]:
            return 0
        elif len(citations) == 1:
            return 1
        for h in range(0, len(citations)+1):
            if abs(-h-1) <= len(citations):
                if h <= citations[-h] and h >= citations[-h-1]:
                    return h
            else:
                if h <= citations[0]:
                    return h
###########################################################################################
'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l1 = list(range(1, n+1))
        def get(n, k, l1):
            ans = ''
            x = 1
            for i in range(1, n):
                x *= i

            number = k % x
            if number == 0:
                first = k//x - 1
            else:
                first = k//x

            if n > 0:
                ans = str(l1.pop(first))
                return ans + get(n-1, number, l1 )
            else:
                return ans

        return get(n, k, l1)
######################################################################################