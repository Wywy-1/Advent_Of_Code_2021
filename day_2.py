from abc import update_abstractmethods


class Vector:
    '''Represents direction and degree of movement from a starting 
    point (0,0)'''

    #Constructor
    def __init__(token, hor, vir):
        token.hor = hor     #i.e., "forward"
        token.vir = vir     #i.e., "down" and "-1(up)"
    
    #Modifiers
    def add_hor(self, num):
        self.hor += num


    def add_vir(self, num):
        self.vir += num


def update_vector(sub, dir, degree):
    '''Modifies a vector-class object when given a 
    direction (forward, up, or down) and a degree of movement
    Inputs:     vector object, string, num'''

    if (dir == "forward"):
        sub.add_hor(degree)
        #print(f'Going forward {degree} units: sub.hor = {sub.hor}')    #test
    elif (dir == "down"):
        sub.add_vir(degree)
        #print(f'Going down {degree} units: sub.vir = {sub.vir}')   #test
    else:
        sub.add_vir(-1*degree)
        #print(f'Going up {degree} units: sub.vir = {sub.vir}') #test


sub = Vector(0,0)

''' test: update_vector 
update_Vector(sub, "forward", 5)
update_Vector(sub, "forward", 12)
update_Vector(sub, "down", 7)
update_Vector(sub, "up", 2)
'''

#print("Vector for submarine is: ", sub.hor, sub.vir, sub.num)