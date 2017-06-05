class Scale(object):
	def __init__(self, x_position, y_position, size):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size   



class Snake(object):
	def __init__(self):
		head = Scale(50,50,10) #(x,y,size)
		self.scales = []
		self.scales.append(head)

	def move(self, direction):
		pass

	def eat(self):
		pass

	def grow(self):
		pass

