import math,pygame,random

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (50, 168, 82)
BLUE = (89, 177, 222)
PINK = (224, 92, 169)
YELLOW = (247, 192, 62)
colours = [GREEN,BLUE,PINK,YELLOW]

class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def multi(self,val):
		self.x*=val
		self.y*=val

	def div(self,val):
		self.x/=val
		self.x/=val

	def add(self,vector):
		self.x+=vector.x
		self.y+=vector.y

	def sub(self,vector):
		self.x-=vector.x
		self.y-=vector.y

	def set(self,x,y):
		self.x = x
		self.y = y

	def get_magnitude(self):
		return ((self.x)**2 + (self.y)**2)**0.5

class Attractor:
	def __init__(self,x,y,m):
		self.pos = Vector(x,y)
		self.mass = m
		self.G = 10
		self.width = 50
		self.height = 50

	def attract(self,movers):
		for mover in movers:
			distance = ((mover.pos.x - self.pos.x)**2 + (mover.pos.y - self.pos.y)**2)**0.5
			distanceSq = distance**2
			strength = self.G*((mover.mass*self.mass)/distanceSq)
			direction = Vector((self.pos.x-mover.pos.x)/distance,(self.pos.y-mover.pos.y)/distance)

			#direction.multi(strength)
			mover.apply_force(direction)

	def draw(self,window):
		rect = pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)
		rect.center = (self.pos.x,self.pos.y)
		pygame.draw.ellipse(window,RED,rect)

class Mover:
	def __init__(self,x,y,m):
		self.pos = Vector(x,y)
		random_y = random.randint(5,20)
		random_x = random.randint(5,20)
		self.vel = Vector(random.choice([-random_x,random_x]),random.choice([-random_y,random_y]))
		self.mass = m
		self.width = 25
		self.height = 25
		self.colour = random.choice(colours)

	def apply_force(self,direction):
		self.vel.add(direction)

	def draw(self,window):
		self.pos.add(self.vel)
		rect = pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)
		rect.center = (self.pos.x,self.pos.y)
		pygame.draw.ellipse(window,self.colour,rect)