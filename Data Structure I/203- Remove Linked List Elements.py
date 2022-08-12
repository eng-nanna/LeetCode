'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''temp = head
        prev = None
        
        while temp and temp.next:
            prev = temp
            temp = temp.next
            if temp.val == val:
                prev.next = prev.next.next
            
        return head'''
        
        arr = []
        newList = head
        newListHead = head
        while head != None:
            if head.val != val:            
                arr.append(head.val)
            head = head.next
        
        if len(arr) == 0:
            newListHead = None
            
        for i in range(len(arr)):
            newList.val = arr[i]
            if(i == len(arr) - 1):
                newList.next = None
            else:
                newList = newList.next
        
        return newListHead