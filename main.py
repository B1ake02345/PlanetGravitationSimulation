from gravitationalAttraction import *
import pygame,sys

BLACK = (0,0,0)
WIDTH,HEIGHT = 1000,1000
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def update(attractor,movers):
	WINDOW.fill(BLACK)
	attractor.attract(movers)
	attractor.draw(WINDOW)
	for mover in movers:
		mover.draw(WINDOW)
	pygame.display.update()

def main():
	movers = [Mover(random.randint(50,950),random.randint(50,950),random.randint(5,20)) for i in range(1)]
	attractor = Attractor(500,500,30)
	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				movers.append(Mover(mx,my,random.randint(5,20)))

		update(attractor,movers)


if __name__ == "__main__":
	main()