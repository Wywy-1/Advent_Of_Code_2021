def calc_gamma():
    '''Calculates the most common bit in each index of a series of binary words (x12 bits) 
    from a .txt file.
    
    TODO #1 Input: file name

    Output: string'''

    test_file = ['1100','1110','1111','1100']
    
    gamma = ''
    gamma_intlist = [0,0,0,0]
    gamma_float = [0.0,0.0,0.0,0.0]

    word_counter = 0
    
    # Adds the value of bits in corresponding indices across all words in test_file
    #   Also counts the number of words (lines) in test file, records in word_counter
    for line in test_file:
        # Enumerate gives each element of line an index. "count" is the index, "bit_value"
        #   is the value at that index
        #   
        for count, bit_value in enumerate(line):
            gamma_intlist[count] += int(bit_value)
        word_counter += 1
    
    print("At 27, after first for-loop in calc_gamma, gamma_intlist is:")
    print(*gamma_intlist)

    # Averages the raw numbers in each index of gamma_intlist by number of words.
    #   Uses these averages to discern which occurs more often, 0 or 1, for
    #   each index across all words, stores in gamma_intlist
    #   TODO #3 Discern how to best address cases where equal 1 and 0, currently
    #       you're assigning those indices with a "2".
    for count,value in enumerate(gamma_intlist):
        gamma_float[count] = value/word_counter
        if (gamma_float[count] < 0.5):
            gamma_intlist[count] = 0
        elif (gamma_float[count] > 0.5):
            gamma_intlist[count] = 1
        else:
            gamma_intlist[count] = 2
    
    # convert integer list, gamma_int_list, into string, gamma
    for num in gamma_intlist:
        gamma += str(num)

    return gamma


def calc_epsilon():
    '''Note, since epsilon is just the compliment of gamma
    you just need to inverse each place on gamma, 
    bitwise NOT'''
    eps = 0

    return eps


def calc_pwr_consum(gamma):
    gamma = calc_gamma()

    print('gamma in binary is\t{}'.format(gamma))
    # TODO #2 Convert gamma (str) into decimal number


if __name__ == "__main__":
    calc_pwr_consum(0)
    #calc_gamma()   #test