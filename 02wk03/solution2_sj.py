## Ssomjang
class Solution_sj:
    def addTwoNumbers(self, l1, l2):
        my_l1 = []
        my_l2 = []
        
        while l1 != None:
            my_l1.append(str(l1.val))
            
            l1 = l1.next
            
        while l2 != None:
            my_l2.append(str(l2.val))
            
            l2 = l2.next
    
        my_l1 = list(reversed(my_l1))
        my_l2 = list(reversed(my_l2))
        my_l1_int = int(''.join(my_l1))
        my_l2_int = int(''.join(my_l2))
        print(my_l2_int)
        
        answer_int = my_l1_int + my_l2_int
        

        answer_int_str_list_reverse = list(reversed(list(str(answer_int))))

        for i in range(len(answer_int_str_list_reverse)):
            if i == 0:
                answerList = ListNode(answer_int_str_list_reverse[i])
            else:
                new_node = ListNode(answer_int_str_list_reverse[i])
                currNode = answerList
                while currNode.next != None:
                    currNode = currNode.next
                currNode.next = new_node

        return answerList