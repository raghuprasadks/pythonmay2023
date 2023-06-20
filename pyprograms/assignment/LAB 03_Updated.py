# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given
# You might add a helper functions as long as it is recursive and named helper_<function name as given in this file>

def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    ## YOUR CODE STARTS HERE
    if num == 1:
        return True
    if num == base:
        return True
    elif num < base:
        return False
    elif base == 1:
        return False
    else:
        return num % base == 0 and is_power_of(base, num // base)




def cut(a_list):
    """
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
	"""
    ## YOUR CODE STARTS HERE
    def cut(lst, ttl=[], previous=False):
        if lst == []:
            return ttl
        if lst[0] > 0 and not previous:
            ttl.append(lst[0])
            return cut(lst[1:], ttl, False)
        elif lst[0] > 0 and previous:
            return cut(lst[1:], ttl, False)
        elif lst[0] <= 0:
            cutindexes = abs(lst[0]-1)
            return cut(lst[1:cutindexes], ttl, True)
    
    return cut(a_list)

ttl =cut([10,20,-30,-40,30,-40,50,60])
print("final")
print(ttl)

ttl =cut([10,20,-30,-40,30,-40,50,60])
print("final")
print(ttl)




def right_max(num_list):
    """
    >>> right_max([3, 7, 2, 8, 6, 4, 5])
    [8, 8, 8, 8, 6, 5, 5]
    >>> right_max([1, 2, 3, 4, 5, 6])
    [6, 6, 6, 6, 6, 6]
    >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
    [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    def right_max(i, max_value):
        if i < 0:
            return []
        
        if max_value is None or num_list[i] > max_value:
            max_value = num_list[i]
        
        return right_max(i - 1, max_value) + [max_value]
    
    return right_max(len(num_list) - 1, None)




#def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    ## YOUR CODE STARTS HERE
    #return consecutive_digits(num, num % 10)

def consecutive_digits(num, prev_dig = 0):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    
    if num <= 0:
        return False
    cur_dig = num % 10
    if cur_dig == prev_dig:
        return True

    return consecutive_digits(num // 10, cur_dig)



def only_evens(num):
    """
    >>> only_evens(4386112)
    4862
    >>> only_evens(0)
    0
    >>> only_evens(357997555531)
    0
    >>> only_evens(13847896213354889741236)
    84862488426
    """
    def only_evens(num, even_num):
        if num == 0:
            return even_num

        digit = num % 10

        if digit % 2 == 0:
            return only_evens(num // 10, even_num) * 10 + digit
        else:
            return only_evens(num // 10, even_num)

    result = only_evens(num, 0)

    if result == 0:
        return 0

    return result



def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace is_power_of with the name of the function you want to test
    #doctest.run_docstring_examples(is_power_of, globals(), name='LAB3',verbose=True)

if __name__ == "__main__":
    run_tests()








