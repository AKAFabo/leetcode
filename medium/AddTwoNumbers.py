class Solution:

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:


        str1 = ""
        str2 = ""

        current = l1      
        while current:
            str1+= str(current.val)
            current = current.next

        current = l2
        while current:
            str2+= str(current.val)
            current = current.next

        total = int(str1[::-1]) + int(str2[::-1])

        digits = str(total)[::-1]

        dummy = ListNode()
        tail = dummy

        for d in digits:
            tail.next = ListNode(int(d))
            tail = tail.next
        return dummy.next