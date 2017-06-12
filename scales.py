class Scale(object):
    def __init__(self, x_position, y_position, size=10):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size   

class Snake(object):
    def __init__(self):
        head = Scale(50,50,10) #(x,y,size)
        self.scales = []
        self.scales.append(head)
        self.x_direction = 1
        self.y_direction = 0 
        self.speed = 10

    def move(self): #move each scale ahead one.
        
        #Move every scale in the tail into the position in front of it.
        for index, scale in reversed(list(enumerate(self.scales))):
            if index >= 1:
                self.scales[index].x_position = self.scales[index-1].x_position
                self.scales[index].y_position = self.scales[index-1].y_position

        #Move head of snake into next position
        self.scales[0].x_position += self.speed * self.x_direction
        self.scales[0].y_position += self.speed * self.y_direction

    
          
    def can_eat(self, food): # i.e. collision
        if self.scales[0].x_position == food.x_position and self.scales[0].y_position == food.y_position:
        	return True
        else:
        	return False

    def eat(self,food): # add a scale
    
        #save tail end scale in temp var
        temp_scale_x = self.scales[len(self.scales)-1].x_position
        temp_scale_y = self.scales[len(self.scales)-1].y_position
        temp_scale_size = self.scales[len(self.scales)-1].size

        #move the snake
        self.move()

        #append the food to the temp location
        self.scales.append(Scale(temp_scale_x, temp_scale_y, temp_scale_size))
        #self.scales.append(temp_scale)

        '''for scale in self.scales:
            print (str(scale.x_position) + ", " + str(scale.y_position))
        '''




