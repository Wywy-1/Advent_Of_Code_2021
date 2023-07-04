from abc import update_abstractmethods
#from .day_1 import get_depth_data


class Vector:
    '''Represents direction and degree of movement from a starting 
    point; (0,0) where (horizontal, vertical)'''

    #Constructor
    def __init__(token, hori, virt):
        token.hori = hori     #i.e., "forward"
        token.virt = virt     #i.e., "down" (+) and "up" (-)
    
    #Modifiers
    def add_hori(self, num):
        self.hori += num


    def add_virt(self, num):
        self.virt += num


def get_depth_data(fileName):
    '''Extracts data taken from a .txt file 
    Returns:    a list'''
    data = []

    with open(fileName, encoding='utf-8') as file:

        for line in file:       # Split() makes 1 line read from file
            x = line.split()    #   into 2 elements, and creates a
            data.append(x)      #   2D array of the data.

    return data
    

def update_vector(vec, dir, degree):
    '''Modifies a vector-class object when given a 
    direction (forward, up, or down) and a degree of movement
    Inputs:     vector object, string, num'''

    if (dir == "forward"):
        vec.add_hor(degree)
    elif (dir == "down"):
        vec.add_vir(degree)
    else:
        vec.add_vir(-1*degree)  # If not "forward" or "down", assumes up.


def calculate_course(data, vec):
    
    for i in range(len(data)):
        update_vector(vec, data[i][0], int(data[i][1]))
    

def main():
    sub = Vector(0,0)
    data = []
    fileName = "input_day_2.txt"

    data = get_depth_data(fileName)        
    calculate_course(data, sub)
    print("Sub is now:\n\tForward\t%d,\n\tDown\t%d." % (sub.hori, sub.virt))


if __name__ == "__main__":
    main()
