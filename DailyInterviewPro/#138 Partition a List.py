"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a list of numbers and an integer k,
partition/sort the list such that the all numbers less than k occur before k,
and all numbers greater than k occur after the number k.

https://leetcode.com/problems/partition-list/
"""


def partition(head: ListNode, x: int) -> ListNode:
	preHead = None
	preTail = None
	postHead = None
	postTail = None
	temp = head

	while temp:
		if temp.val < x:
			if preHead == None:
				preHead = temp
				preTail = temp

			else:
				preTail.next = temp
				preTail = preTail.next
		else:
			if postHead == None:
				postTail = temp
				postHead = temp
			else:
				postTail.next = temp
				postTail = postTail.next

		temp = temp.next

	if preTail == None:
		return postHead
	if postTail == None:
		return preHead

	postTail.next = None
	preTail.next = postHead
	return preHead
	

# print(partition_list([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))   use linked list here
# [2, 2, 2, 2, 2, 2, 2, 5, 5]