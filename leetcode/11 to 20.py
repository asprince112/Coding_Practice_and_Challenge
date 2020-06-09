'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
                return l2
        else:
            if l2 == None:
                return l1
        
        while l1 and l2:
            x = l1.val + l2.val
            if x < 10:
                ans = ListNode(x)
                ans.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                ans = ListNode(x % 10)
                ans.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ans

###############################################################################################
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tem = []
        ans = 0 
        for i in list(s):
            if i not in tem:
                tem.append(i)
            else:
                if ans < len(tem):
                    ans = len(tem)

                tem = tem[tem.index(i)+1:]
                tem.append(i)

        if ans < len(tem):
            ans = len(tem)

        return ans

###########################################################################################
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        
        return  (num[(len(num)-1)//2] + num[len(num)//2]) / 2

##########################################################################################
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''
if len(s) >= 2:
        d = len(s)
        for i in range(d+1):
            for j in range(i+1):

                if s[i-j:d-j] == s[i-j:d-j][::-1]:
                    return s[i-j:d-j]
    else:
        return s

###################################################################################
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        head = 0
        tail = len(height) - 1
        for i in range(len(height)):
            width = abs(head - tail)
            if height[head] < height[tail]:   
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1

            if res > water:
                water = res
        return water

########################################################################################
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        ans = b = 0
        l1 = list(s)
        for i in range(len(s)):
            a = roman[l1.pop()]
            if a < b:
                ans -= a
            else:
                ans += a
            b = a
        return ans

########################################################################################
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        m = ['', 'M', 'MM', 'MMM']
        c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return m[num//1000] + c[(num%1000)//100] + x[(num%100)//10] + i[num%10]

########################################################################################
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

########################################################################################
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        a = list(str(x))
        a.reverse()
        if a[-1] == '-':
            a = a[:-1]
            for i in range(len(a)):
                ans += int(a[i]) * (10 ** (len(a) - i - 1))
            ans = 0 - ans

        else:
            for i in range(len(a)):
                ans += int(a[i]) * (10 ** (len(a) - i - 1))
                
        if - (2 ** 31) < ans < (2 ** 31) - 1:
            return ans
        else:
            return 0
########################################################################################
'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = nums[:n]
        l2 = nums[n:]
        ans = []
        for i in range(n):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans