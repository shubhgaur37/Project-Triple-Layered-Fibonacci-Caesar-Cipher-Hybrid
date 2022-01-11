class Vignere:
    def __init__(self):
        #Creating a vignere matrix
        self.vignere_mat=[]
        for i in range(26):
            t=[]
            for j in range(26):
                if i+j<26:
                    t.append(chr(i+j+65))
                else:
                    t.append(chr(i+j-26+65))

            self.vignere_mat.append(t)
            
#####################################################################################
    def encrypt_helper(self,PT,Key):
        CT=''
        n=len(PT)
        m=len(Key)
        #extending the key in case it is short
        while m<n:
            Key+=Key[:n-m]
            m=len(Key)
        else:
            Key=Key[:n]


        for i in range(n):
            col=ord(PT[i])-65
            row=ord(Key[i])-65
            CT+=self.vignere_mat[row][col]

        return CT
    
    def encrypt(self,PT,Key):
        CT=''
        PT_arr=PT.upper().split()
        Key=Key.upper()
        for i in PT_arr:
            CT+=self.encrypt_helper(i,Key)+' '
        return CT[:-1]
#####################################################################################


    def decrypt_helper(self,CT,Key):
        PT=''
        n=len(CT)
        m=len(Key)
        #extending the key in case it is short
        while m<n:
            Key+=Key[:n-m]
            m=len(Key)
        else:
            Key=Key[:n]

        for i in range(n):
            row=ord(Key[i])-65
            for j in range(26):
                if self.vignere_mat[row][j]==CT[i]:
                    col=j
                    break
            PT+=self.vignere_mat[0][col]


        return PT



    def decrypt(self,CT,Key):
        PT=''
        CT_arr=CT.upper().split()
        Key=Key.upper()
        for i in CT_arr:
            PT+=self.decrypt_helper(i,Key)+' '
        return PT[:-1]
