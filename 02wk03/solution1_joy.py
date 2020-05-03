# Joy
class Solution_joy:
    def reverse(self, x: int) -> int:
        if(x>0):
            int2str=str(x)
            mark=''
        else:
            int2str=str(x).replace("-",'')
            mark="-"
        reverse=[]
        listed=list(int2str)
        for i in range(len(listed)):
            reverse.append(listed[len(listed)-(i+1)])
        answer=int(mark+''.join(reverse))
        
        if(answer>2147483647):
            return 0
        elif(answer<-2147483647):
            return 0
        else:
            return answer