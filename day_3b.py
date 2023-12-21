#from day_3 import get_pwr_data

def item_at_index_most(data, index):
    
    index_record_0 = []
    index_record_1 = []

    # Appends all items with a 0 at index to index_record_0 Then appends all
    #   other items (i.e., those that start with a 1) to index_record_1.
    for item in data:
        if item[index] == '0':
            index_record_0.append(item)
        else:
            index_record_1.append(item)

    # Returns the larger of either index_record_0 or index_record_1
    if len(index_record_0) > len(index_record_1):
        return index_record_0
    else:
        return index_record_1


def place_holder():
    test_data = ['100100110110',
                '101110110110',
                '010100010100',
                '011001110000',
                '000000000111',
                '000010110001',
                '001111000001',
                '100010000001',
                '010100110011',
                '010000010110',
                '010000000011',
                '010101001000']
    
    ogr: list(str) = []
    ogr = item_at_index_most(test_data, 0)
    
    print('ogr in place_holder now consists of:\t{}'.format(ogr))
    #co2sr: str = []

    #print('First item in test data:\t\t\t{}'.format(test_data[0]))
    #print('First index of first item in test data:\t\t{}'.format(test_data[0][0]))
    #print('Second index of first item in test data:\t{}'.format(test_data[0][1]))


if __name__ == "__main__":
    place_holder()

#oxygen generator rating (OGR)

#To find oxygen generator rating, determine the most common value (0 or
#1) in the current bit position, and keep only numbers with that bit in
#that position. If 0 and 1 are equally common, keep values with a 1 in
#the position being considered.

#E.G: Start with all 12 numbers and consider only the first bit of each
# number. There are more 1 bits (7) than 0 bits (5), so keep only the 7
# numbers with a 1 in the first position: 11110, 10110, 10111, 10101,
# 11100, 10000, and 11001.
#   Then, consider the second bit of the 7 remaining numbers: there are
#       more 0 bits (4) than 1 bits (3), so keep only the 4 numbers 
#       with a 0 in the second position: 10110, 10111, 10101, and 
#       10000.
#   In the third position, three of the four numbers have a 1, so keep
#       those three: 10110, 10111, and 10101.
#   In the fourth position, two of the three numbers have a 1, so keep
#       those two: 10110 and 10111.
#   In the fifth position, there are an equal number of 0 bits and 1
#       bits (one each). So, to find the oxygen generator rating, keep
#       the number with a 1 in that position: 10111.
#   As there is only one number left, stop; the oxygen generator rating
#       is 10111, or 23 in decimal.



#CO2 scrubber rating (CO2SR)

#To find CO2 scrubber rating, determine the least common value (0 or 1)
#in the current bit position, and keep only numbers with that bit in
#that position. If 0 and 1 are equally common, keep values with a 0 in
#the position being considered.

#E.G: Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
#   Then, consider the second bit of the 5 remaining numbers: there are
#       fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers 
#       with a 1 in the second position: 01111 and 01010.
#   In the third position, there are an equal number of 0 bits and 1
#       bits (one each). So, to find the CO2 scrubber rating, keep the
#       number with a 0 in that position: 01010.
#   As there is only one number left, stop; the CO2 scrubber rating is
#       01010, or 10 in decimal.


#Both the oxygen generator rating and the CO2 scrubber rating are 
#values that can be found in your diagnostic report - finding them is
#the tricky part. Both values are located using a similar process that
#involves filtering out values until only one remains. Before 
#searching for either rating value, start with the full list of binary
#numbers from your diagnostic report and consider just the first bit
#of those numbers. Then:
#Keep only numbers selected by the bit criteria for the type of rating
#value for which you are searching. Discard numbers which do not match
#the bit criteria. If you only have one number left, stop; this is the
#rating value for which you are searching. Otherwise, repeat the
#process, considering the next bit to the right.

#Multiply the OSR and CO2SR to get Life Support Rating. Of the first
#   12 numbers in the input, this number should be 230 (decimal)