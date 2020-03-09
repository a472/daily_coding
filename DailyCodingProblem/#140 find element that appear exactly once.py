"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

def findExactlyOnce(arr):
    xor=arr[0]

    for i in range(1,len(arr)-1):
        xor=xor^arr[i]

    set_bit = xor & ~(xor-1)

    x=0
    y=0
    for i in range(len(arr)):
        if set_bit & arr[i]:
            x=x^arr[i]
        else:
            y=y^arr[i]
    return x,y
print(findExactlyOnce([2, 4, 6, 8,4, 10, 2, 10]))
