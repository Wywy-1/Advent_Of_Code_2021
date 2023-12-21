from day_3 import get_pwr_data


def find_least(index_record_0, index_record_1):
    '''Returns the smaller of either index_record_0 or index_record_1.
    Will return index_record_0 if index_record_0 and index_record_1 are
    equal.
    Input:  list[str], list[str]
    Returns:    list[str]'''

    if len(index_record_0) <= len(index_record_1):  # If ir0 is smaller or equal       
        return index_record_0
    else:
        return index_record_1


def find_most(index_record_0, index_record_1):
    '''Returns the larger of either index_record_0 or index_record_1.
    Will return index_record_1 if index_record_0 and index_record_1 are
    equal.
    Input:  list[str], list[str]
    Returns:    list[str]'''

    if len(index_record_0) > len(index_record_1):
        return index_record_0
    else:   # Where equal, keep the number with a "1"
        return index_record_1


def sort_to_0_1 (data, index, least_most):
    '''Sorts items in data into two lists: One where indices have a 0 at
    index, and one where indices have a 1 at index.
    Calls find_most if least_most == "most", and find_least otherwise.
    Returns a list with either the items that had the most 1s or 0s at 
    index, or the least, respectively.
    Input:  list[str], int, string
    Returns:    list[str]'''

    index_record_0 = []
    index_record_1 = []

    # Appends all items with a 0 at index to index_record_0 Then appends all
    #   other items (i.e., those that start with a 1) to index_record_1.
    for item in data:
        if item[index] == '0':
            index_record_0.append(item)
        else:
            index_record_1.append(item)

    if least_most == 'most':
        return find_most(index_record_0, index_record_1)
    else:
        return find_least(index_record_0, index_record_1)


def find_ratings():
    data = get_pwr_data('input_day_3.txt')
    
    ogr: list(str) = []     # "Oxygen Generator Rating"
    co2sr: list(str) = []   # "CO2 Scrubber Rating"

    # Compute first-case for OGR and CO2SR using test_data
    ogr = sort_to_0_1(data, 0, 'most')
    co2sr = sort_to_0_1(data, 0, 'least')
    
    # Subsequent cases, OGR feeds into item_at_index_most until we reach the
    #   OGR rating.
    for count in range(len(data)):
        ogr = sort_to_0_1(ogr, count, 'most')
        if len(ogr) == 1:   # Break when there is only one item left
            break

    # Subsequent cases of CO2SR similarly feed into item_at_index_least
    #   until we reach the CO2SR rating.
    for count in range(1,len(data)):
        co2sr = sort_to_0_1(co2sr, count, 'least')
        if len(co2sr) <= 1:   # Break when there is only one item left
            break

    print('Oxygen Generator Rating\t{}'.format(ogr))
    print('CO2 Scrubber Rating\t{}'.format(co2sr))

    ogr = int(ogr[0],2)
    co2sr = int(co2sr[0],2)

    lsr = ogr * co2sr
    print('life support rating is\t{}'.format(lsr))


if __name__ == "__main__":
    find_ratings()