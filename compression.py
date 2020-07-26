# compression.py

'''
in: 'abaasass'
out: 'aba2sas2'
'''

def compression(S):
	out = ""
	i = 0
	while i < len(S):
		count = 1
		while i < len(S) - 1 and S[i] == S[i + 1]: # if next == current, then increment count and i.
			count += 1
			i = i + 1

		out += S[i]

		if count == 1:
			out += ''
		else:
			out += str(count)
		i += 1
	return out

assert compression('abaasass') == 'aba2sas2'