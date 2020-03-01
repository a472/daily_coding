"""
Hi, here's your problem today. This problem was recently asked by Apple:

Create a class that initializes with a list of numbers and has one method called sum.
sum should take in two parameters, start_idx and end_idx and
return the sum of the list from start_idx (inclusive) to end_idx` (exclusive).

"""


class ListFastSum:
	def __init__(self, nums):
		for i in range(1, len(nums)):
			nums[i] = nums[i - 1] + nums[i]
		self.nums = nums

	def sum(self, start_idx, end_idx):
		if start_idx - 1 < 0:
			return self.nums[end_idx - 1]
		return self.nums[end_idx - 1] - self.nums[start_idx - 1]


print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(1, 5))
# 12 because 3 + 4 + 5 = 12
