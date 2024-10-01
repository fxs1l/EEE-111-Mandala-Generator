import PIL.Image, PIL.ImageDraw
from math import sin, cos, pi

class Mandala:
    def __init__(self, size, bgcolor):
        """ Initializes the Mandala class

        Args:
            size (two-float tuple): image dimensions of the mandala in pixels
            bgcolor (three-float tuple): RGB representation of the background color of the canvas
        """
        self.size = size # two integer tuple
        self.bgcolor = bgcolor# three integer tuple + 8bit RGB
        self.canvas = PIL.Image.new(mode="RGB", size=self.size, color=self.bgcolor) # Image Object
        self.draw = PIL.ImageDraw.Draw(self.canvas)# ImageDraw object
    
    def show(self):
        """ Displays the Mandala"""
        self.canvas.show()
    
    def save(self, filename):
        """ Saves the mandala as a PNG image

        Args:
            filename (string): filepath of the name
        """
        self.canvas.save(fp=filename, format='PNG')
    
    def rotate_point(self, point, pivot, angle):
        """ Rotates a point about a pivot by an angle

        Args:
            point (two-float tuple): xy coordinate of the point to be rotated
            pivot (two-float tuple): xy coordinate of the pivot point
            angle (float): angle of rotation in degrees

        Returns:
            (two-float tuple): xy coordinate of the rotated point
        """
        angle *= pi/180 # angle in radians
        
        # rotate the points using trig functions
        new_point_x = (point[0]-pivot[0]) * cos(angle) - (point[1]-pivot[1]) * sin(-angle) + pivot[0]
        new_point_y = (point[0]-pivot[0]) * sin(-angle) + (point[1]-pivot[1]) * cos(angle) + pivot[1]
        
        return new_point_x, new_point_y

    def draw_triangle(self, center, side_length, rotation, color):
        """ Draws a polygon (equilateral triangle) centered around a given point

        Args:
            center (two-float tuple): centroid of the triangle and acts as the pivot point of the triangle
            side_length (float): length of one side of the triangle
            rotation (float): angle of rotation in degrees
            color (three-int tuple): RGB representation of the color
        """
        # determine the points of the triangle assuming no rotation
        half_height = side_length * 1.73 / 4 # 1.73 is an approximation of sqrt(3)
        half_side = 0.5 * side_length
        a = (center[0] - half_side, center[1] + half_height)
        b = (center[0] + half_side, center[1] + half_height) 
        c = (center[0], center[1] - half_height)
        points = [a, b, c]

        # rotate the points and draw the lines connecting them
        for i in range(len(points)):
            end_idx = (i+1) % len(points) 
            fp = self.rotate_point(points[i], center, rotation)
            np = self.rotate_point(points[end_idx], center, rotation)
            start = (round(fp[0]), round(fp[1]))
            end = (round(np[0]), round(np[1]))
            self.draw.line([start,end], fill=color, width=1)
    
    def draw_arrowhead(self, pivot, rotation, color, size=1):
        """ Draws an arrowhead element with a pivot around its butt

        Args:
            pivot (two-float tuple): xy coordinate of the pivot point and serves as the back of the arrowhead
            rotation (float): angle of rotation in degrees
            color (three-int tuple): RGB representation of the color
            size (int, optional): scaling factor. defaults to 1.
        """
        length = 10* size
        height = 20* size
        end_arrow = 1/3 * length

        # first imagine the arrowhead as pointing to the right 
        # length coords
        back = (pivot[0], pivot[1])
        front = (pivot[0]+length, pivot[1])
        # tip of the "wings" coords  
        up =  (pivot[0]-end_arrow, pivot[1]-height)
        down = (pivot[0]-end_arrow, pivot[1]+height)
        
        points = [back, front, up, down]
        # perform rotations
        for i in range(len(points)):
            points[i] = self.rotate_point(points[i], pivot, rotation+90) # add 90 degrees to make it upright

        # draw the lines
        self.draw.line([points[0], points[1]], fill=color, width=2) 
        self.draw.line([points[2], points[1]], fill=color, width=2)
        self.draw.line([points[3], points[1]], fill=color, width=2)
        self.draw.line([points[0], points[2]], fill=color, width=2)
        self.draw.line([points[0], points[3]], fill=color, width=2)
