# Find_Permutation.py
'''
IDIIDD
1234567 // sorted
1324765 // answer
'''
s = "DDDDIIIIII"
def find_permutation(s)
	ans = list(range(1, len(s)+2))
	start = 0
	end = 0
	pointer = 0

	while pointer < len(s):
		if s[pointer] == 'D':
			start = pointer
			end = pointer
			while pointer < len(s) and s[pointer] == 'D':
				pointer += 1
				end = pointer
			ans[start:end+1] = ans[start:end+1][::-1]
	pointer += 1
	return ans
print(find_permutation(s))
#[5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11]