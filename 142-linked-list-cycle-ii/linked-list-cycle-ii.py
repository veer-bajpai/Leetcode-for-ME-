class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head            