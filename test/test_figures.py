import pytest
from figure import Triangle, Rectangle, Circle

def test_triangle_perimeter():
    triangle = Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_perimeter() == 12  

def test_triangle_surface():
    triangle = Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_surface() == 3.0 

def test_rectangle_perimeter():
    rectangle = Rectangle(a=4, b=6)
    assert rectangle.compute_perimeter() == 20  

def test_rectangle_surface():
    rectangle = Rectangle(a=4, b=6)
    assert rectangle.compute_surface() == 24 

def test_circle_perimeter():
    circle = Circle(radius=5)
    assert circle.compute_perimeter() == pytest.approx(31.4159)  

def test_circle_surface():
    circle = Circle(radius=5)
    assert circle.compute_surface() == pytest.approx(78.53975)