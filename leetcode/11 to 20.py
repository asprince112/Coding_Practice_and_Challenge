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

'''