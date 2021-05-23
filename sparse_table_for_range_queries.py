class Sparse:
    def __init__(self, arr) -> None:
        self.logs = [0, 0]
        for i in range(2, len(arr)+2):
            self.logs.append(self.logs[i//2] + 1)
        self.table = [[0 for i in range(self.logs[len(arr)] + 1)] for _ in arr]
        for index, value in enumerate(arr):
            self.table[index][0] = value

    def precompute(self) -> None:
        for j in range(1, self.logs[len(self.table)] + 2):
            i = 0
            while i + (1 << j) <= len(self.table):
                self.table[i][j] = Sparse.function('min', self.table[i][j-1],
                                                   self.table[i + (1 << (j-1))][j-1])
                i += 1

    @classmethod
    def function(cls, type, one, two):
        if type == 'max':
            return max(one, two)
        elif type == 'min':
            return min(one, two)
        elif type == 'sum':
            return one + two

    def query(self, type, left, right):
        if type == 'sum':
            total = 0
            for j in range(self.logs[len(self.table)], -1, -1):
                if ((1 << j) <= right - left + 1):
                    total += self.table[left][j]
                    left += 1 << j
            return total
        elif type == 'max':
            j = self.logs[right - left + 1]
            return max(self.table[left][j], self.table[right - (1 << j) + 1][j])
        elif type == 'min':
            j = self.logs[right - left + 1]
            return min(self.table[left][j], self.table[right - (1 << j) + 1][j])


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split(' ')))
    s = Sparse(l)
    s.precompute()
    for i in range(int(input())):
        d = list(map(int, input().split(' ')))
        print(s.query('min', d[0], d[1]))
