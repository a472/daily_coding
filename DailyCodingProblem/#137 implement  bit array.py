"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i
"""

class BitArray:
	def __init__(self, size):
		self.__set_indices = set()
		self.size = size

	def set(self, i, val):
		if i>=self.size:
			raise LookupError("Invalid index")
		elif val and not i in self.__set_indices:
			self.__set_indices.add(i)
		elif not val and i in self.__set_indices:
			self.__set_indices.remove(i)

	def get(self, i):
		if i>=self.size:
			raise LookupError("Invalid index")
		elif i in self.__set_indices:
			return 1
		else:
			return 0

ba = BitArray(10)

ba.set(2,1)

try:
	print(ba.get(2))
except LookupError as le:
	print(le)

try:
	print(ba.get(18))
except LookupError as le:
	print(le)

try:
	print(ba.get(6))
except LookupError as le:
	print(le)



