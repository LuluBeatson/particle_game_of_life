import pygame
import random
import math

# Graphics Variables ##############################
W = 600
H = 600
BORDER = 0
FG = pygame.Color('white')
BG = pygame.Color('black')

# Define Classes ##################################
class Particle:

	def __init__(self, x, y, vx, vy, m, r, q, colour):
		self.x = x # position
		self.y = y
		self.vx = vx # velocity
		self.vy = vy
		self.m = m # mass
		self.r = r # radius
		self.q = q # charge
		self.colour = colour


	def show(self):
		global screen

		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.r)


	def get_forces(self, objects):
		Fx = 0
		Fy = 0
		for p2 in objects:
			if p2 is not self:
				_Fx, _Fy = F_e(self, p2)
				Fx += _Fx
				Fy += _Fy
		return Fx, Fy

	# def collide_particles(self, objects):
	# 	for p2 in objects:
	# 		if dist(self, p2)<=self.r+particle.r:
				


	def update(self):

		pygame.draw.circle(screen, BG, (int(self.x), int(self.y)), self.r)

		# Bounce if wall colision:
		if (int(self.y) <= BORDER + self.r) or (int(self.y) >= H - BORDER - self.r):
			self.vy = -self.vy
		if (int(self.x) <= BORDER + self.r) or (int(self.x) >= W - BORDER - self.r):
			self.vx = -self.vx

		# Add particle interactions:
		Fx, Fy = self.get_forces(objects)
		self.vx += Fx/m
		self.vy += Fy/m

		# motion:
		self.x += self.vx
		self.y += self.vy

		self.show()

		


# Define physics #############################
C_e = 10

def dist(p1, p2):
	return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

def sq_dist(p1, p2):
	return (p1.x-p2.x)**2 + (p1.y-p2.y)**2

def F_e(p1, p2): # Electric force between two particles
	F = C_e * p1.q * p2.q / sq_dist(p1, p2)
	Fx = F * (p1.x - p2.x) / dist(p1, p2)
	Fy = F * (p1.y - p2.y) / dist(p1, p2)
	return Fx, Fy

# def F_e_tot(p1): # Total of Electric forces exerted on a single particle
# 	Fx = 0
# 	Fy = 0
# 	for p2 in objects:
# 		if objects.index(p2) != objects.index(p1):
# 			_Fx, _Fy = F_e(p1, p2)
# 			Fx += _Fx
# 			Fy += _Fy


# Create Objects ##############################

# Testing:
N=100
r=5
q=1
m=1
# objects = [Particle(random.randint(BORDER+r+1, W-BORDER-r-1), random.randint(BORDER+r+1, H-BORDER-r-1), random.randint(0,100)/100, random.randint(0,100)/100, m, r, random.randint(0,100)/100, colour=pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))) for i in range(N)]
# particle1 = Particle(200, 300, 0.1, 0, 5, 5, 1, pygame.Color('red'))
# particle2 = Particle(400, 300, 0, 0, 5, 5, -1, pygame.Color('blue'))
# objects = [particle1, particle2]

positive_particles = [Particle(random.randint(BORDER+r+1, W-BORDER-r-1), random.randint(BORDER+r+1, H-BORDER-r-1), random.randint(0,100)/100, random.randint(0,100)/100, m, r, 1, colour=pygame.Color('red')) for i in range(50)]
negative_particles = [Particle(random.randint(BORDER+r+1, W-BORDER-r-1), random.randint(BORDER+r+1, H-BORDER-r-1), random.randint(0,100)/100, random.randint(0,100)/100, m, r, -1, colour=pygame.Color('blue')) for i in range(50)]
objects = positive_particles + negative_particles

# Main scenario ################################
pygame.init()

screen = pygame.display.set_mode((W, H))
pygame.draw.rect(screen, FG, pygame.Rect((0,0), (W, BORDER)))
pygame.draw.rect(screen, FG, pygame.Rect((0,0), (BORDER, H)))
pygame.draw.rect(screen, FG, pygame.Rect((0,H-BORDER), (W, H)))
pygame.draw.rect(screen, FG, pygame.Rect((W-BORDER,0), (W, H)))

for particle in objects:
	particle.show()

while True:
	e = pygame.event.poll()
	if e.type == pygame.QUIT:
		break

	pygame.display.flip()

	for particle in objects:
		particle.update()

pygame.quit()