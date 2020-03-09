"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a phone number, return all valid words that can be created using that phone number.

For instance, given the phone number 364
we can construct the words ['dog', 'fog'].
"""

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
    ans=[]
    total=lettersMaps[int(phone[0])]
    for i in phone[1:]:
        temp=[]
        for j in range(len(total)):
            for char in lettersMaps[int(i)]:
                temp.append(total[j]+char)
        total=temp
    for word in total:
        if word in validWords:
            ans.append(word)
    return ans

print(makeWords('364'))
# ['dog', 'fog']


