def calc_gamma():
    '''Calculates the most common bit in each index of a series of binary words (x12 bits) 
    from a .txt file.
    
    TODO #1 Input: file name
    Output: list of integers, gamma'''

    test_file = ['1100','1110','1111','1101']
    
    gamma = [0,0,0,0]
    gamma_float = [0.0,0.0,0.0,0.0]

    word_counter = 0
    
    # Adds the value of bits in corresponding indices across all words in test_file
    #   Also counts the number of words (lines) in test file, records in word_counter
    for line in test_file:
        for count, bit_value in enumerate(line):
            gamma[count] += int(bit_value)
        word_counter += 1
    
    # Averages the raw numbers in each index of bit_tracker by number of words.
    #   Uses these averages to discern which occurs more often, 0 or 1 for
    #   each index across all words.
    print('Calculating averages of each bit index:')

    for count,value in enumerate(gamma):
        gamma_float[count] = value/word_counter
        if (gamma_float[count] < 0.5):
            gamma[count] = 0
        else:
            gamma[count] = 1
    
    print('{}'.format(gamma))

    return gamma


def calc_epsilon():
    '''Note, since epsilon is just the compliment of gamma
    you just need to inverse each place on gamma, 
    bitwise NOT'''
    eps = 0b000000000000

    return eps

def calc_pwr_consum(gamm, epsilon):
    gamma = calc_gamma()

    print('gamma in decimal is\t%d' % gamma)
    print('gamma in binary is\t%s' % bin(gamma))


if __name__ == "__main__":
    #calc_pwr_consum(0,0)
    calc_gamma()   #test