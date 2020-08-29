
''' assume that we have a large string named document, and our
goal is to produce a new string, letters, that contains only the alphabetic characters
of the original string (e.g., with spaces, numbers, and punctuation removed).'''
# Do not do this
letter = ''
for c in document:
	if c.isalpha():
		letters += c 
# strings are immutable, letters += c command would compute the concatentation, letters + c
# as a new string instance and then reassign the identifiers, letters. 
# it takes O(n^2) time

# A better approach
temp = [ ] # start with empty list
for c in document:
	if c.isalpha( ):
		temp.append(c) # append alphabetic character
letters = .join(temp) # compose overall result

# Even better approach
letters = ''.join(c for c in document if c.isalpha( )) # note that this is space efficiency since we use generator