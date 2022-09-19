import json

def get_depth_data(fileName):
    '''Extracts data taken from a file, "fileName" 
    Returns:    a list'''
    data = []
    with open(fileName, encoding='utf-8') as file:

        for line in file:
            data.append(int(line))
            
    return data


def iterate_depth_data(data):
    '''Iterates over each data point in list, "data", and 
    returns the number of times a data point is smaller than the next point.
    Returns:    int'''
    num = 0
    for n in range(len(data)-1):
        if (data[n] < data[n+1]):
            num += 1
    return num
    

def main():
    '''Initializes the data list and prints results of
    iterate_depth_data'''
    data = []
    #fileName = 'TestInput'
    fileName = 'input_day_1'

    data = get_depth_data(fileName)
    print(iterate_depth_data(data))

if __name__ == "__main__":
    main()