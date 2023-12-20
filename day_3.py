def get_pwr_data(fileName):
    '''Extracts data taken from a file, "fileName"
    Input:      a string 
    Returns:    a list[str]'''

    data: list[str] = []
    with open(fileName, encoding='utf-8') as file:
        for line in file:
            data.append(str(line))
    return data


def find_compliment(gamma):
    '''Takes an int-list of 0s and 1s and returns an int-list representing
    the former's compliment: That is, examines each index of the former and
    replaces 0s with 1s and 1s with 0s, then stores these in the latter.
    Input: int-list
    Return: int-list'''

    eps = []
    for x in gamma:
        if x == 0:
            eps.append(1)
        else:
            eps.append(0)
    return eps


def calc_gam_eps():
    '''Calculates the most common bit, 0 or 1, for each index across a
    series of binary words (x12 bits) taken from a .txt file.
        Returns: two int-lists'''

    pwr_data = get_pwr_data('input_day_3.txt')
    gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
    epsilon = gamma
    indices_averages = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    word_counter = 0
    
    # Adds the value of the bits in corresponding indices across all words 
    #   in test_file, saves to gamma_intlist.
    #   Also counts the number of words (lines) in test file, records in 
    #       word_counter
    for line in pwr_data:
        for x in range(12):
            gamma[x] += int(line[x])
        word_counter += 1

    # Divides the values stored in each index of gamma_intlist by the number
    # of words taken from the text file to get the average of values for
    # each index. Then uses these averages to discern which occurs more 
    # often, 0 or 1, for each index across all words. Stores this 
    # information in gamma_intlist.
    for count,value in enumerate(gamma):
        indices_averages[count] = (value/word_counter)
        if (indices_averages[count] < 0.5):
            gamma[count] = 0
        elif (indices_averages[count] > 0.5):
            gamma[count] = 1
        else:   # When 0 and 1 occur equally as often
            gamma[count] = 1
    
    epsilon = find_compliment(gamma)
    return gamma, epsilon


def calc_pwr_consum(gamma, epsilon):
    '''Calculates the power consumption of the christmas submarine and
    prints the results to terminal.
    Input: int-list, int-list'''

    gamma, epsilon = calc_gam_eps()

    # Convert each int in an int-list, gamma and epsilon, to binary.
    binary_gamma = "".join(format(x,'b') for x in gamma)
    binary_epsi = "".join(format(x,'b') for x in epsilon)

    # Converts binary_gamma and binary_epsi into singular decimal integers
    decimal_gamma = int(binary_gamma, 2)
    decimal_epsi = int(binary_epsi, 2)

    print("Printing binary gamma: {}".format(binary_gamma))
    print("Printing decimal gamma: {}\n".format(decimal_gamma))
    print("Printing binary epsilon: {}".format(binary_epsi))
    print("Printing decimal epsilon: {}\n".format(decimal_epsi))
    print("Your power consumption is {}\n".format(decimal_gamma * decimal_epsi))


if __name__ == "__main__":
    calc_pwr_consum(0,0)
