def recursive_binary_exponentiation(a, n):
    """
    calculating the a to the power n , i.e is a^n recursively
    """
    if n == 0:
        # returning the identity matrix here
        m = matrix()
        m.data[0][1] = 0
        m.data[1][0] = 0
        return m
    temp = recursive_binary_exponentiation(a, n//2)
    if n & 1 == 1:
        return temp * temp * a
    return temp * temp


def fibonocci(n):
    """
    this function will return the nth fibonocii number
    """
    # here passing the [[0,1],[1,1]] as input to the matrix
    m = matrix()
    m.data[0][0] = 0

    ans = recursive_binary_exponentiation(m, n)
    # ans will have the [[0,1],[1,1]] ^ n

    temp = matrix()
    temp = temp * ans
    # first row of the temp stores the n and n+1 th fibonoci numbers
    print('for n', n, temp.data)
    return temp.data[0][1]


class matrix:
    def __init__(self):
        self.data = [[1 for j in range(2)] for _ in range(2)]

    def __mul__(self, other):
        temp = matrix()
        temp.data[0][0], temp.data[0][1], temp.data[1][0], temp.data[1][1] = (self.data[0][0] * other.data[0][0] + self.data[0][1] * other.data[1][0],
                                                                              self.data[0][0] * other.data[0][1] +
                                                                              self.data[0][1] *
                                                                              other.data[1][1],
                                                                              self.data[1][0] * other.data[0][0] +
                                                                              self.data[1][1] *
                                                                              other.data[1][0],
                                                                              self.data[1][0] * other.data[0][1] + self.data[1][1] * other.data[1][1])
        return temp


#print(list(fibonocci(i) for i in range(1, 5)))
# print(fibonocci(1000))
