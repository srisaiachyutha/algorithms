class BinaryIndexTree :
	def __init__(self, n):
		self.tree = [0]*(n+1)
		self.len  = len(self.tree)
	def updateValueAtIndex(self, index , value):
		while index < self.len:
			self.tree[index] += value
			index += ( index & -index)
	def getCumulativeValueAtIndex(self, index):
		sum = 0
		while index > 0:
			sum += self.tree[index]
			index -= ( index & -index)
		return sum
	def getOriginalFrequencyAtIndex(self, index):
		total = self.tree[index]
		if index > 0:
			check = index - ( index & -index)
			index -=1
			while index != check:
				total -= self.tree[index]
				index -= (index & -index)
		return total
