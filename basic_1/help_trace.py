class A:
    def get_x(self, neg=False):
        if neg:
            return -5
        else:
            return 5

    x = property(get_x)
    neg_x = property(get_x(False))
class B(A):
	pass

ins=A()
#Check is instance
print(isinstance(ins,A))
#Print out the whole class defination 
#print help(A)
#Check the is subclass  (B sub A Parent)
print issubclass(B,A)

