class Universe:
	def __init__(self, w, h):
		self.width=w
		self.height=h

#	def __str__(self):
#		# string representation when you call str() on the object
#		# gets called when you call print() on the object
#		pass	
#
#	def __get__(self):
#		# gets called when you try to access indexes (object[3])
#		pass
#
	def build_grid(self):
		self.grid = [[col for col in range(self.width)] for row in range(self.height)]
