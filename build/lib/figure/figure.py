from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    @abstractmethod
    def compute_perimeter(self) -> float|int:
        """
        Returns float of perimeter
        """
        pass

    @abstractmethod
    def compute_surface(self) -> float|int:
        """
        Returns float of surface
        """
        pass

class Triangle(PlaneFigure):
    def __init__(self, base: float, c1: float, c2: float, h: float):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self) -> float|int:
        return self.base + self.c1 + self.c2

    def compute_surface(self) -> float|int:
        return 0.5 * self.base * self.h

class Rectangle(PlaneFigure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def compute_perimeter(self) -> float|int:
        return 2 * (self.a + self.b)

    def compute_surface(self) -> float|int:
        return self.a * self.b

class Circle(PlaneFigure):
    def __init__(self, radius: float):
        self.radius = radius

    def compute_perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

    def compute_surface(self) -> float:
        return 3.14159 * (self.radius ** 2)
    
# triangle = Triangle(base=3, c1=4, c2=5, h=2)
# print(f"Perimeter of triangle: {triangle.compute_perimeter()}")
# print(f"Surface of triangle: {triangle.compute_surface()}")

# rectangle = Rectangle(a=4, b=6)
# print(f"Perimeter of rectangle: {rectangle.compute_perimeter()}")
# print(f"Surface of rectangle: {rectangle.compute_surface()}")

# for radius in range(3):
#     circle = Circle(radius=5)
#     print(f"Perimeter of circle with r of {radius}: {circle.compute_perimeter()}")
#     print(f"Surface of circle with r of {radius}: {circle.compute_surface()}")