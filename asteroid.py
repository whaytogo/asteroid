import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw (self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            x, y = self.position
            spawn_angle = random.uniform(20,50)
            
            # setting velocity for children
            velocity1 = self.velocity.rotate(spawn_angle)
            velocity2 = self.velocity.rotate(-spawn_angle)

            # calculating radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # spawning the children
            first_child = Asteroid(x, y,new_radius)
            second_child = Asteroid(x,y,new_radius)
            
            # velocity for spawns
            first_child.velocity = velocity1 * 1.2
            second_child.velocity = velocity2 * 1.2



