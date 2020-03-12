"""
Given a string s, find length of the longest prefix which is also suffix.
The prefix and suffix should not overlap.

Input : aabcdaabc
Output : 4
The string "aabc" is the longest
prefix which is also suffix.

"""

# bruteforce
# string = "aabcdaabc"
string = "aaaa"

maxlen=0
for i in range(len(string)//2):
	if string[:i+1]==string[-(i+1):]:
		maxlen=i+1
print(maxlen)

# using KMP search approach
kmp=[0]*len(string)
i=1
j=0

while i<len(string):
	if string[j]==string[i]:
		kmp[i] = j + 1
		i += 1
		j += 1
	else:
		if j!=0:
			j=kmp[j-1]
		else:
			i+=1
#for non overlapping use this statement
j=min(len(string)//2,j)
print(j,kmp)
print(string[:j])