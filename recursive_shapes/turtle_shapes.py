import turtle
import math
import seaborn as sns
import sys


def get_next_sets(trt, origin, init_hd, nsides, r):
    int_angle = 180*(nsides-2)/nsides
    turn_angle = 180-int_angle
    sets = []
    trt.penup()
    trt.goto(*origin)
    trt.seth(init_hd)
    trt.right(turn_angle/2)
    start_angle = trt.heading()
    
    #properties of next shape
    next_sides = nsides-1
    next_int_angle = 180*(next_sides-2)/next_sides
    next_turn_angle = 180-next_int_angle
    
    for i in range(nsides):
        trt.goto(*origin)
        trt.seth(start_angle + i*turn_angle)
        trt.fd(2*r)
        if nsides % 2 == 0:
            sets.append( (trt.pos(), trt.heading()) )
        else:
            sets.append( (trt.pos(), trt.heading() + next_turn_angle/2))
    return sets

def recursive_shapes( trtl, origin, heading=90, radius=100, nsides=6, circle=True ):
    trtl.penup()
    trtl.goto(*origin)
    #draw the circle
    x, y = trtl.pos()
    clr = cmap[nsides-3]
    
    trtl.color(clr, clr)
    trtl.sety(y - radius)
    trtl.pd()
    trtl.seth(0)
    if circle:
        trtl.circle(radius)
    trtl.penup()
    #draw the polygon
    trtl.goto(*origin)
    #calculate the internal angle of the polygon
    angle = 180*(nsides-2)/nsides
    #calculate the length of the polygon edges
    l = 2*radius*math.cos(math.radians((1/2)*180*(nsides-2)/nsides))
    trtl.seth(heading)
    trtl.fd(radius)
    trtl.right(180 - (angle/2))
    trtl.pd()
    for i in range(nsides):
        trtl.fd(l)
        trtl.right(180-angle)
    if nsides >= 4:
        next_sides = nsides - 1
        sets = get_next_sets(trtl, origin, heading, nsides, radius)
        for s in sets:
            recursive_shapes(trtl, s[0], s[1], radius, next_sides, circle)
            
            
if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
    except:
        print("Usage: python turtle.py radius nsides")
        sys.exit(1)
        
    origin = (0,0)
    heading = 90
    radius = float(sys.argv[1])
    nsides = int(sys.argv[2])
    assert nsides > 2
    t = turtle.Turtle()
    t.speed('fastest')

    cmap = {i:c for i, c in enumerate(sns.color_palette('nipy_spectral', nsides-2))}

    turtle.screensize(canvwidth=1000, canvheight=1000, bg='black')
    recursive_shapes(t, origin, heading, radius, nsides, circle=False)
    turtle.done()

    
