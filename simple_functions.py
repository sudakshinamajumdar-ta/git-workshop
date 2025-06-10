DEBUG = True

def double_number(a):
    """
    Double the input value by adding it to itself.

    Parameters
    ----------
    a : int or float
        The number to be doubled.

    Returns
    -------
    int or float
        The doubled result of the input number.
    """

    if DEBUG:
        print(f"[DEBUG] Inside double_number(): input = {a}")
    result = a + a
    if DEBUG:
        print(f"[DEBUG] Inside double_number(): result = {result}")
    return result

def square_number(a):
    """
    Compute the square of the input number.

    Parameters
    ----------
    a : int or float
        The number to be squared.

    Returns
    -------
    int or float
        The square of the input number.
    """

    if DEBUG:
        print(f"[DEBUG] Inside square_number(): input = {a}")
    result = a * a
    if DEBUG:
        print(f"[DEBUG] Inside square_number(): result = {result}")
    return result
