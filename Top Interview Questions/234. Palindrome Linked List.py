'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        l = 0
        r = len(arr)-1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        
        return True'''
        fast = slow = head
    
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True