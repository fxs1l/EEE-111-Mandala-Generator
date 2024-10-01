from sp2_mandala import *

if __name__ == '__main__':
    """ initialization """
    
    # colors to be used
    bg = (59, 66, 83)
    blue = (134, 192, 209) 
    orange = (225, 99, 96)
    
    # initialize the Mandala class
    m = Mandala((1000,1000), bg) 

    """ for-loops for drawing the patterns"""
    
    # main pattern
    center = 20
    for i in range(center):
        size = 20 
        m.draw_arrowhead((500,500), i*360/center, orange, size)
        m.draw_arrowhead((500,500), i*360/center, orange, size/2)
    
    # complementary pattern
    inner = 15
    for i in range(inner):
        angle = int(i*360/inner)
        angle_modif = int(i*360/(inner-7))
        m.draw_arrowhead((500,500), angle_modif, blue, size=4)
        m.draw_triangle((500,500), 1000, angle, blue)

    """ display and save the output""" 
    m.save("sp2_output.png")
    m.show()
