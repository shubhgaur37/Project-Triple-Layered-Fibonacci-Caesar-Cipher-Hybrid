from FibCaesar import FibonacciCaesar
from PlayF import Playfair
from Vign import Vignere
class MixCipher():
    def __init__(self,Key):#key is a word
        self.Key=Key
        self.obj1=FibonacciCaesar()
        self.obj2=Vignere()
        self.obj3=Playfair(self.Key)
    
    def encrypt(self,PT):
        #vignere
        ct1=self.obj2.encrypt(PT,self.Key)
        #vignere to fibonacci caesar
        ct2=self.obj1.encrypt(ct1)
        #fibonacci caesar to playfair modified
        ct3=self.obj3.encrypt(ct2)
        return ct3
    
    def decrypt(self,CT):
        #playfair decrypt
        pt1=self.obj3.decrypt(CT)
        #fib caesar decrypt
        pt2=self.obj1.decrypt(pt1)
        #Vignere decrypt ans
        pt3=self.obj2.decrypt(pt2,self.Key)
        return pt3