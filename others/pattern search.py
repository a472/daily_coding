"""
Given a text txt[0..n-1] and a pattern pat[0..m-1],
write a function search(char pat[], char txt[])
that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
"""

# method 1
import re
pat = "AABA"
txt = "AABAACAADAABAABA"
result = re.finditer(r'(?=AABA)', txt)          # using lookahed
for x in result:
	print(x.start())


# method 2 KMP only search non-overlap pattern
j=0
i=1
lps=[0]*len(pat)

#let's first create largest prefix same as suffix array on pattern
while i<len(pat):
	if pat[j]==pat[i]:
		lps[i]=j+1
		i+=1
		j+=1
	else:
		if j!=0:
			j=lps[j-1]
		else:
			i+=1


#now search pattern within text
i=0
j=0
while i<len(txt) :
	if txt[i]==pat[j]:
		j+=1
		i+=1
	else:
		if j!=0:
			j=lps[j-1]
		else:
			i+=1

	if j==len(pat):
		print("pattern found at ",i - len(pat))
		j=0



