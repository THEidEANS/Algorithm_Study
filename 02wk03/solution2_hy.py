## H.Kim
class Solution_hy:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_str = str(l1.val)
        while l1.next:
            l1 = l1.next
            l1_str = l1_str + str(l1.val)
        
        l2_str = str(l2.val)
        while l2.next:
            l2 = l2.next
            l2_str = l2_str + str(l2.val)
        
        # reverse the numbers
        l1_num = int(l1_str[::-1])
        l2_num = int(l2_str[::-1])
        
        # str cast에서 속도차이가 있나..?

        # add them together
        res_int = l1_num + l2_num
        res_str = str(res_int)
        
        # change int -> LinkedList
        root = ListNode(res_str[-1])    # last digit
        result_linked = root
        for num in res_str[-2::-1]:     # reverse loop except last digit
            result_linked.next = ListNode(num)
            result_linked = result_linked.next

        result_linked = root
        
        return result_linked