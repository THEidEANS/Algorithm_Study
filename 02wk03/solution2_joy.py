# Joy
class Solution_joy:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp1=''
        temp2=''  
        while(l1):
            temp1=temp1+str(l1.val)
            l1=l1.next
        while(l2):
            temp2=temp2+str(l2.val)
            l2=l2.next   
        tmp1=list(temp1)
        tmp2=list(temp2)
        len_1=len(tmp1)
        len_2=len(tmp2)
        
        tran_1=[]
        tran_2=[]
        for i in range(len_1):
            tran_1.append(tmp1[len_1-(i+1)])
        for i in range(len_2):
            tran_2.append(tmp2[len_2-(i+1)])
        
        answer=int(''.join(tran_1))+int(''.join(tran_2))   
        an_li=list(str(answer))
        an_li.reverse()
        
        for i,item in enumerate(an_li):
            if(i==0):
                answer_list=ListNode(int(item))
            else:
                new=ListNode(int(item))
                current=answer_list
                while (current.next!=None):
                    current=current.next
                current.next=new
                
                    
        return answer_list