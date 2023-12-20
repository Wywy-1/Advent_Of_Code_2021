def calc_gam_eps():
    '''Calculates the most common bit in each index of a series of binary words (x12 bits) 
        from a .txt file.
        Output: string'''

    test_file = ['1100','1110','1111','1100']    #TODO #1 Input: file name
    
    gamma_intlist = [0,0,0,0]
    gamma_float = [0.0,0.0,0.0,0.0]
    epsilon = ''

    word_counter = 0
    
    # Adds the value of bits in corresponding indices across all words in test_file,
    #   saves to gamma_intlist
    #   Also counts the number of words (lines) in test file, records in word_counter
    for line in test_file:
        for count, bit_value in enumerate(line):
            gamma_intlist[count] += int(bit_value)
        word_counter += 1

    # Averages the raw numbers in each index of gamma_intlist by number of words/lines.
    #   Uses these averages to discern which occurs more often, 0 or 1, for
    #   each index across all words, stores in gamma_intlist.
    #   TODO #3 Discern how to best address cases where 1 and 0 occur equally 
    #       often, currently you're assigning those indices with a "1".
    for count,value in enumerate(gamma_intlist):
        gamma_float[count] = value/word_counter
        if (gamma_float[count] < 0.5):
            gamma_intlist[count] = 0
        elif (gamma_float[count] > 0.5):
            gamma_intlist[count] = 1
        else:   # When 0 and 1 occur equally as often
            gamma_intlist[count] = 1
    
    epsilon = find_compliment(gamma_intlist)

    return gamma_intlist, epsilon


def intList2string(x): 
    '''Converts an integer-list into a string.'''

    con_string=''

    for num in x:
        con_string += str(num)

    return con_string


def find_compliment(gamma):
    '''Takes an int-list and returns an int-list
    representing the former's compliment: examines
    each index of the former and replaces 0s with
    1s and 1s with 0s in the latter.
    Input: int-list
    Return: int-list'''
    eps = []

    for x in gamma:
        if x == 0:
            eps.append(1)
        else:
            eps.append(0)

    return eps


def calc_pwr_consum(gamma, epsilon):
    '''Calculates the power consumption of the christmas submarine and
    prints the results to terminal.
    Input: int-list, int-list'''
    gamma, epsilon = calc_gam_eps()

    bin_gamma = " ".join(format(x,'b') for x in gamma)  # Converts each int in int-list into binary
    bin_epsi = " ".join(format(x,'b') for x in epsilon)

    print("Printing binary gamma: {}".format(bin_gamma))
    print("Printing binary epsilon: {}".format(bin_epsi))
    # TODO #2 Convert gamma (str) into decimal number


if __name__ == "__main__":
    calc_pwr_consum(0,0)
