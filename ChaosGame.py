#!/bin/env python3
# A simple chaos game implementation that draws a Sierpinsky Triangle

import pygame, time, random, math

class point:
    def __init__(self, pos, color):
        ## pos = (x, y)
        ## color = (r, g, b)
        self.pos = pos
        self.color = color


WIDTH = 640
HEIGHT = 480
pygame.init()
disp = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Chaos Game")
pane = pygame.Surface((WIDTH, HEIGHT))

#points = [(0, 0), (320, 480), (640, 0)]  # the points of the triangle
points = [  # the point objects that make up the boundary
        point((0, 0), (255, 0, 0)),
        point((320, 480), (0, 255, 0)),
        point((640, 0), (0, 0, 255))
        ]
dotSize = 0.1
# Randomly placed initial trace point
tp = point((random.randint(0, WIDTH),
           random.randint(0, HEIGHT)), 
           (255, 255, 255))

# draw the target points of the shape
for point in points:
    pygame.draw.circle(disp, point.color, point.pos, int(dotSize), 0)

while(True):
    
    targetPoint = points[random.randint(1, len(points)) - 1]
    tp.pos = [math.fabs((tp.pos[0]+targetPoint.pos[0])/2), math.fabs((tp.pos[1]+targetPoint.pos[1])/2)]
    
    # new color is that of the point we're moving towards
    tp.color = targetPoint.color
    # new tracepoint is halfway between current tp and targetPoint
    tp.pos = (math.fabs(tp.pos[0] + targetPoint.pos[0]/2),
              math.fabs(tp.pos[1] + targetPoint.pos[1]/2))
    
    # paint this new point on the screen
    # but also convert tracepoint to integer space
    # Divide by 2 because the "move halfway" above doesn't account
    # for the need to include negative directions
    dp = (int(tp.pos[0]/2), int(tp.pos[1]/2))
    print(tp.color)
    pygame.draw.circle(disp,  tp.color, dp, int(dotSize), 0)
    pygame.display.flip()
    #TODO: Read key inputs to close or pause program
#    time.sleep(0.1)

print("Program finished")


## some extra garbage from a prior implementation ##
#    color = (255, 255, 255) #  no need to reset color, it'll be overwritten by each point anyway
#    if (r == 1):
#        color = (255, 0, 0)
#        tp = [math.fabs((tp.pos[0]+targetPoint[r].pos[0])/2), math.fabs((tp.pos[1]+targetPoint.pos[1])/2)]
#    elif(r == 2):
#        color = (0, 255, 0)
#        tp = [math.fabs((tp.pos[0]+targetPoint.pos[0])/2), math.fabs((tp.pos[1]+targetPoint.pos[1])/2)]
#
#    elif(r == 3):
#        color = (0, 0, 255)
#        tp = [math.fabs((tp.pos[0]+targetPoint.pos[0])/2), math.fabs((tp.pos[1]+targetPoint.pos[1])/2)]
 
