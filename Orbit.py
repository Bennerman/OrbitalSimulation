import math
import pygame


dt = 0.1



G = .00001 #6.674 * (10 ** -11)
rv = [0,0]
rhat = [0,0]
Fv = [0,0]


class MassObject:
    def __init__(self, name, mass, radius, position, momentum, force):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.momentum = momentum
        self.force = force

    def updatePosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position

    def getMomentum(self):
        return self.momentum


sun = MassObject("Sun", 10000000, .5, [300,300], [0,1000000], 0)
earth = MassObject("Earth", 0.0005, .05, [200,400], [0,.0004], 0)


def gravForce(obj1, obj2):
    rv[0] = obj1.position[0] - obj2.position[0]
    rv[1] = obj1.position[1] - obj2.position[1]

    r = math.sqrt(rv[0]**2 + rv[1]**2)
    rhat[0] = rv[0] / r
    rhat[1] = rv[1] / r
    Fv[0] = (-1 * G) * ((obj2.mass * obj1.mass)/(abs(r)**2)) * rhat[0]
    Fv[1] = (-1 * G) * ((obj2.mass * obj1.mass)/(abs(r)**2)) * rhat[1]

    return Fv




def main():
    pygame.init()
    screen_size = 600
    screen = pygame.display.set_mode((screen_size, screen_size))
    gameExit = False
    while(not gameExit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
        
       

    
        sun.force = gravForce(sun, earth) 
        earth.force = gravForce(earth, sun)
        #print(earth.position[0])
        #print(earth.for)

        sun.momentum[0] = sun.momentum[0] + (sun.force[0] * dt)
        sun.momentum[1] = sun.momentum[1] + (sun.force[1] * dt)
        earth.momentum[0] = earth.momentum[0] + (earth.force[0] * dt)
        earth.momentum[1] = earth.momentum[1] + (earth.force[1] * dt)

        sun.position[0] = sun.position[0] + (sun.momentum[0]/sun.mass) * dt
        sun.position[1] = sun.position[1] + (sun.momentum[1]/sun.mass) * dt

        earth.position[0] = earth.position[0] + (earth.momentum[0]/earth.mass) * dt
        earth.position[1] = earth.position[1] + (earth.momentum[1]/earth.mass) * dt

        pygame.draw.rect(screen, (0, 0, 255), (sun.position[0],sun.position[1],10,10))
        pygame.draw.rect(screen, (0, 0, 255), (earth.position[0],earth.position[1],10,10))
        pygame.display.update()
        screen.fill((0, 0, 0))
        
        

main()











