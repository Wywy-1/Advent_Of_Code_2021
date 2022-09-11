from day_1 import get_depth_data

def add_three(data, i):
    '''Adds three consecutive items in a list

    Returns:    sum of three consecutive items in a list'''

    sum = 0

    for n in range(i, i+3):
        sum += data[n]

    print(sum)

    return sum


def compare(data, i):
    '''Compares the sum of three consecutive list items to 
    the sume of three consecutive list items one removed.

    Inputs:     list, starting index
    returns:    True if first three is smaller the next three
                False if first three is larger'''

    return add_three(data, i) < add_three(data, i+1)


def iterate_depth_data(data):
    '''Iterates through a list of ints and calls compare() 
    to compare three consecutive items by the following three
    consecutive numbers. Returns the number of times the former
    is a smaller number than the latter.

    Inputs:     list of ints
    Returns:    int'''

    num = 0

    for n in range(len(data)-3):
        if compare(data, n):
            num += 1
        print('')

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
