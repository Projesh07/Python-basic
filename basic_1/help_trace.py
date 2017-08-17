class A:
    def get_x(self, neg=False):
        if neg:
            return -5
        else:
            return 5

    x = property(get_x)
    neg_x = property(get_x(False))
print help(A)
