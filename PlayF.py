#Some changes in playfair cipher(6x6) key matrix is used to accomodate j 
#Because of this we had to change the order of encryption,playfair(modified) acts as the last layer of encryption

class Playfair():#a key is passed first
    def __init__(self,key):
        self.key=key.upper()
        self.playfair_mat=[[0 for i in range(6)] for j in range(6)]
        self.createPlayfairMatrix(self.key)


    def findEmpty(self):
        for i in range(6):
            for j in range(6):
                if self.playfair_mat[i][j]==0:#empty
                    return (i,j)
        return (-1,-1) #no empty place

    def createPlayfairMatrix(self,key):
        present={}
        flag=False
        #for letters
        for i in range(26):
            present[chr(i+65)]=False
        for i in range(10):
            present[str(i)]=False
        
        for i in key:
            if not present[i]:#letter hasn't come in matrix yet
                row,col=self.findEmpty()
                if row==-1 and col==-1:
                    break
                else:
                    self.playfair_mat[row][col]=i
                    present[i]=True
        else:
            row,col=self.findEmpty()
            while row!=-1 and col!=-1:
                if not flag:
                    for i in range(26):
                        letter=chr(65+i)
                        if not present[letter]:
                            self.playfair_mat[row][col]=letter
                            present[letter]=True
                            break
                    else:
                        flag=True#means all alphabets are present in the playfair matrix
                else:
                
                    for i in range(10):
                        if not present[str(i)]:
                            self.playfair_mat[row][col]=str(i)
                            present[str(i)]=True
                            break
                        

                row,col=self.findEmpty()

    def findLetterIndex(self,l):
            for i in range(6):
                for j in range(6):
                    if self.playfair_mat[i][j]==l:
                        return i,j
            
########################################################################################

    def encrypt(self,PT):
        CT=''
        PT_arr=PT.upper().split()
        for i in PT_arr:
            CT+=self.encrypt_helper(i)+' '
        return CT[:-1]

    def encrypt_helper(self,PT):
        #Finding the character to append to make pairs
        s=0
        for i in self.key:
            s+=ord(i)
        ch=str(s%10)

        #making a list by splitting PT into pairs
        pairlist=[]
        n=len(PT)
        i=0#iterator

        while i<n-1:
            if PT[i]!=PT[i+1]:
                pairlist.append(PT[i]+PT[i+1])
                i+=2
            else:
                #add a character ch
                pairlist.append(PT[i]+ch)
                i+=1
        else:
            if i<n:
                pairlist.append(PT[i]+ch)
                i+=1
        CT=''

        for i in pairlist:
            #finding row and column of letters in playfair_mat
            #for 0th letter
            row1,col1=self.findLetterIndex(i[0])
            row2,col2=self.findLetterIndex(i[1])
            if col1!=col2 and row1!=row2:
                CT+=self.playfair_mat[row1][col2]+self.playfair_mat[row2][col1]
            elif col1==col2:
                if row1==5:
                    CT+=self.playfair_mat[0][col2]+self.playfair_mat[row2+1][col1]
                elif row2==5:
                    CT+=self.playfair_mat[row1+1][col2]+self.playfair_mat[0][col1]
                else:
                    CT+=self.playfair_mat[row1+1][col2]+self.playfair_mat[row2+1][col1]
            elif row1==row2:
                    if col1==5:
                        CT+=self.playfair_mat[row1][0]+self.playfair_mat[row2][col2+1]
                    elif col2==5:
                        CT+=self.playfair_mat[row1][col1+1]+self.playfair_mat[row2][0]
                    else:
                        CT+=self.playfair_mat[row1][col1+1]+self.playfair_mat[row2][col2+1]

        return CT

    ##################################################################################
    def decrypt(self,CT):
        PT=''
        CT_arr=CT.upper().split()
        for i in CT_arr:
            PT+=self.decrypt_helper(i)+' '
        return PT[:-1]
    
    
    def decrypt_helper(self,CT):
        pairlist=[]
        n=len(CT)
        for i in range(0,n-1,2):
            pairlist.append(CT[i]+CT[i+1])
        PT=''
        for i in pairlist:
            #finding row and column of letters in playfair_mat
            #for 0th letter
            row1,col1=self.findLetterIndex(i[0])
            row2,col2=self.findLetterIndex(i[1])
            if col1!=col2 and row1!=row2:
                PT+=self.playfair_mat[row1][col2]+self.playfair_mat[row2][col1]
            elif col1==col2:
                if row1==0:
                    PT+=self.playfair_mat[5][col2]+self.playfair_mat[row2-1][col1]
                elif row2==0:
                    PT+=self.playfair_mat[row1-1][col2]+self.playfair_mat[5][col1]
                else:
                    PT+=self.playfair_mat[row1-1][col2]+self.playfair_mat[row2-1][col1]
            elif row1==row2:
                    if col1==0:
                        PT+=self.playfair_mat[row1][5]+self.playfair_mat[row2][col2-1]
                    elif col2==0:
                        PT+=self.playfair_mat[row1][col1-1]+self.playfair_mat[row2][5]
                    else:
                        PT+=self.playfair_mat[row1][col1-1]+self.playfair_mat[row2][col2-1]
        #finding character to remove
        s=0
        for i in self.key:
            s+=ord(i)
        ch=str(s%10)
        #removing the character ch from PT
        PT=PT.replace(ch,'')
        return PT