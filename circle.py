from math import sqrt

class circle:
    pass

def create(radius):
    c=circle()
    c.r=radius
    return c
    
def circle_area(c):
    return (22/7) * c.r**2
    
def circle_perimeter(c):
    return 2 * (22/7) * c.r
    
def info(c):
    return f'Circle <{c.r}>'

def draw(c):
    print(f'{info(c)}')

def test_circle(radius):
    c=create(radius)
    print(draw(c))
    print(f'Area={circle_area(c) }')
    print(f'Perimeter={circle_perimeter(c)}')

test_circle(4)    