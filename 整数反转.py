#整数反转
class Solution:
    def reverse(self, x: int) -> int:
        #等于0直接返回
        if x == 0:
            return 0
        #将x转为字符窜，进行翻转
        str_x = str(x)
        #判断x是否为负数，为负数则在翻转加上‘-’。
        int_x = ''
        if str_x[0] == '-' :
            int_x += '-'
        #结尾有‘-’则去除,开头有0,int()会自动去除，
        int_x += str_x[::-1].rstrip('-')
        int_x = int(int_x)
        #是否溢出
        #32位系统  int的范围为 -2**31  到 2**31-1
        #64位系统  int的范围为 -2**63  到 2**63-1
        if -2**31<int_x<2**31-1:
            return int_x
        
        return 0
        
