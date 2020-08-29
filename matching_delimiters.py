# matching_delimiters.py

def is_mathched(expr):
	left = '({[<'
	right = ')}]>'

	S = [] # use a list to represent a stack
	for c in expr:
		if c in left: # push opening
			S.append(c)
		elif c in right:
			if not S: # nothing to mathch
				return False
			if left[right.index(c)] != S.pop():
				return False
	return len(S) == 0

a = ['( )(( )){([( )])}','((( )(( )){([( )])}))',')(( )){([( )])}','({[ ])}','(','[(5+x)-(y+z)]']

for i in a:
	if is_mathched(i):
		print("correct")
	else:
		print('incorrect')