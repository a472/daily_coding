"""
This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.
"""


# we will use DP and Histogram area concept to solve this problem

def hist_maxarea(arr):

	max_area = -1
	i = 1
	stack = [0]  # push index on top of stack not actual arr value

	while i < len(arr):

		if len(stack)==0 or arr[i] >= arr[stack[-1]]:
			stack.append(i)
			i += 1
		else:
			while len(stack) != 0 and arr[i] < arr[stack[-1]]:
				top = stack.pop()

				if len(stack) == 0:
					area = arr[top] * i
				else:
					area = arr[top] * (i - stack[-1] - 1)

				max_area = max(max_area, area)

	#if stack is not empty
	while len(stack) != 0:
		top = stack.pop()

		if len(stack) == 0:
			area = arr[top] * i
		else:
			area = arr[top] * (i - stack[-1] - 1)

		max_area = max(max_area, area)
	return max_area


def largest_rect_area(Mat):
	rows = len(Mat)
	cols = len(Mat[0])
	ans = -1
	arr = Mat[0]
	ans = max(ans, hist_maxarea(arr))
	for r in range(1, rows):
		for c in range(cols):
			if Mat[r][c] == 0:
				arr[c] = 0
			else:
				arr[c] += Mat[r][c]
		ans = max(ans, hist_maxarea(arr))

	return ans


mat = [[1, 0, 0, 0],
	   [1, 0, 1, 1],
	   [1, 0, 1, 1],
	   [0, 1, 0, 0]]
print(largest_rect_area(mat))
