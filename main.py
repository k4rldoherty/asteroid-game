import pygame 
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
	clock = pygame.time.Clock()
	
	dt = 0
	
	drawable = pygame.sprite.Group()
	updateable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Asteroid.containers = (asteroids, updateable, drawable)
	Shot.containers = (shots, updateable, drawable)
	AsteroidField.containers = updateable
	asteroid_field = AsteroidField()
	
	Player.containers = (updateable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")
		for d in drawable:
			d.draw(screen)
		
		for u in updateable:
			u.update(dt)
		
		for a in asteroids:
			# checks for colisions
			if a.is_collision(player): 
				print("Game Over!")
				sys.exit()
			
			for b in shots:
				if b.is_collision(a):
					a.split()
					b.kill()
		
		pygame.display.flip()
		
		# Limits FPS to 60
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
