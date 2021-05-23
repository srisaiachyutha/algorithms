POS_INFINITY = float('inf')
NEG_INFINITY = float('-inf')

# TODO  testing to be done for this


class FenwickTree:
    data = []
    length = 0
    function = None
    function_name = ''

    def __init__(self, parameter, function_name='min') -> None:
        self.function_name = function_name
        if function_name == 'min':
            self.function = self.min
        elif function_name == 'max':
            self.function = self.max
        elif function_name == 'add':
            self.function = self.add

        if not isinstance(function_name, str):
            self.function = function_name

        if isinstance(parameter, list):
            self.length = len(parameter)
            self.data = [0]*self.length
            for index, element in enumerate(parameter):
                self.update(index, element)

        elif isinstance(parameter, int):
            self.length = parameter
            self.data = [0]*parameter

    def add(self, one, two):
        return one + two

    def min(self, one, two):
        return one if one < two else two

    def max(self, one, two):
        return two if one < two else one

    def update(self, index, value):
        while index < self.length:
            self.data[index] = self.function(self.data[index], value)
            index |= (index + 1)

    def get(self, index):
        if self.function_name == 'min':
            result = POS_INFINITY
        elif self.function_name == 'max':
            result = NEG_INFINITY
        elif self.function_name == 'add':
            result = 0
        while index >= 0:
            result = self.function(result, self.data[index])
            index = (index & (index + 1)) - 1
        return result

    def get(self, left, right):
        return self.function(self.get(left), self.get(right))


def fun(one, two):
    return one + two


# n = int(input())
# l = list(map(int,input().split()))
# l = [i%2 for i in l]
# tree = FenwickTree(l,fun)
# for i in range(int(input())):
#     t = list(map(int,input().split()))
#     if t[0] == 0:
#         tree.update(t[1],t[2] % )
#     else:
#         ans = tree.get(t[1],t[2])
#         if t[0]== 2:

#             print()
