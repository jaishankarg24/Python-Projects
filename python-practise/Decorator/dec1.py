
def division(d):
	def inn(x,y):
		if y==0:
			return 'Provid non zero denominator'
		else:
			return d(x,y)
	return inn

@division
def div(a,b):
	return a/b

print(div(10,5))
print(div(10,0))