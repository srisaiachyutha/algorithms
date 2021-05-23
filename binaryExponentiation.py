def recursive_binary_exponentiation(a, n):
    """
    calculating the a to the power n , i.e is a^n recursively
    """
    if n == 0:
        return 1
    temp = recursive_binary_exponentiation(a, n//2)
    if n & 1 == 1:
        return temp * temp * a
    return temp * temp


def iterative_binary_exponentiation(a, n):
    """
    calculating the a to the power n , i.e is a^n iteratively
    """
    ans = 1
    while n > 0:
        if n & 1 == 1:
            ans = ans * a
        a = a * a
        n >>= 1
    return ans
