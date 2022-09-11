class Vector:
    '''The direction of our submarine'''
    #Constructor
    def __init__(self, hor, vir, num):
        self.hor = hor
        self.vir = vir
        self.num = num

sub = Vector(0,0,0)
#print("Vector for submarine is: ", sub.hor, sub.vir, sub.num)