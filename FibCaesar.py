#fibonacci Caesar Cipher:doesnt require a key
class FibonacciCaesar:
    def fibonacciTerm(self,n):
        if n==1 or n==2:
            return 1
        a=1
        b=1
        c=0
        i=3
        while i<=n:
            c=a+b
            a=b
            b=c
            i+=1
        return c
######################################################################################
    def encrypt(self,PT):
        CT=''
        PT_arr=PT.upper().split()
        for i in PT_arr:
            CT+=self.encrypt_helper(i)+' '
        return CT[:-1]

    def encrypt_helper(self,PT):
        n=len(PT)
        CT=''
        for i in range(n):
            ascii=ord(PT[i])
            CT+=chr(65+(ascii-65+self.fibonacciTerm(i+1))%26)
        return CT
######################################################################################

    def decrypt(self,CT):
        PT=''
        CT_arr=CT.upper().split()
        for i in CT_arr:
            PT+=self.decrypt_helper(i)+' '
        return PT[:-1]

    def decrypt_helper(self,CT):
        n=len(CT)
        PT=''
        for i in range(n):
            ascii=ord(CT[i])
            PT+=chr(65+(ascii-65-self.fibonacciTerm(i+1))%26)
        return PT
######################################################################################


