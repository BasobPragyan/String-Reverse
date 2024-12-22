class reverse:
    def __init__(self,name):
        self.name=name
    def streverse(self):
       print(self.name[::-1])
    
s1=input("Enter name : ")
s2=reverse(s1)
s2.streverse()