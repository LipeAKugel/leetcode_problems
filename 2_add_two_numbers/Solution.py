# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l3 = ListNode()
    n1 = l1
    n2 = l2
    n3 = l3
    
    n3.val = n1.val + n2.val
    while True:
      if n1.next is None and n2.next is None:
        if n3.val > 9:
          n3.next = ListNode(val=1)
          n3.val -= 10
        return l3
      elif n1.next is None:
        n2 = n2.next
        n3.next = ListNode(val=n2.val)
      elif n2.next is None:
        n1 = n1.next
        n3.next = ListNode(val=n1.val)
      else:
        n1 = n1.next
        n2 = n2.next
        n3.next = ListNode(val=n1.val + n2.val)

      if n3.val > 9:
        n3.next.val += 1
        n3.val -= 10
        
      n3 = n3.next
        