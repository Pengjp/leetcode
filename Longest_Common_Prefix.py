# Longest_Common_Prefix.py

def longestCommonPrefix(strs):
	if not strs:
		return ""
	# longest prefix is the word with shortest length
	shortest = sorted(strs, key=lambda x:len(x))[0] # nlogn a bit faster
	for index, letter in enumerate(shortest):
		for word in strs:
			if word[index] != letter:
				return shortest[:index]
	return shortest 

print(longestCommonPrefix(['flight','flower','fly','flow']) == 'fl')