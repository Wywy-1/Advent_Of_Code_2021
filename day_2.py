from abc import update_abstractmethods
#from .day_1 import get_depth_data


class Vector:
    '''Represents direction and degree of movement from a starting 
    point; (0,0) where (horizontal, vertical)'''

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
    elif (dir == "down"):
        sub.add_vir(degree)
    else:
        sub.add_vir(-1*degree)


def get_depth_data(fileName):
    '''Extracts data taken from a file, "fileName" 
    Returns:    a list'''
    data = []
    with open(fileName, encoding='utf-8') as file:

        for line in file:
            x = line.split()
            data.append(x)
            #data.append(int(line))

    return data


def iterate_depth_list(data, sub):
    
    for i in range(len(data)):
        #print('Line: %d\t%s' % (i, data[i]))           # 'Line: 9 ['forward', 8]
        #print('\tDirection:\t%s'  % (data[i][0]))      # 'Direction  forward'
        #print('\tDegree:\t\t%d' % (int(data[i][1])))   # 'Degree     8'
        update_vector(sub, data[i][0], int(data[i][1]))
    
    print("Sub is now:\n\tForward\t%d,\n\tDown\t%d." % (sub.hor, sub.vir))


sub = Vector(0,0)
data = []
fileName = "testInput_2.txt"

data = get_depth_data(fileName)        
iterate_depth_list(data, sub)