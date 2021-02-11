class Student:
	"""docstring for Student"""
	def __init__(self, name):
		
		self.name = name

	def display(self):
		print(self.name)

if __name__ == '__main__':
	j=Student('Jai')
	j.display()
		