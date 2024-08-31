import pygame
from constants import *
from player import Player
from asteroidfield import *

def main():
	pygame.init()

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	game_clock = pygame.time.Clock()
	dt = 0


	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#groups
	asteroids = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	updatables = pygame.sprite.Group()

	Player.containers = (drawables, updatables)
	AsteroidField.containers = updatables
	Asteroid.containers = (asteroids, drawables, updatables)

	player = Player(x,y)
	asteroid_field = AsteroidField()

	while True: 

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")

		
		for drawable in drawables:
			drawable.draw(screen)


		for updatable in updatables:
			updatable.update(dt)

		pygame.display.flip()

		dt = game_clock.tick(60) / 1000




  
if __name__ == "__main__":
	main()

