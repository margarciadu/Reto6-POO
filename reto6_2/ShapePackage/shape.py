import math 
from math import degrees, acos

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, start: Point, end: Point):
        if start.x == end.x and start.y == end.y:
            raise ValueError("A line cannot have the same start and end point")
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
        self.points = []
    
    def compute_length(self):
        return ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5
    
    def compute_slope(self):
        dx = self.end.x - self.start.x
        if dx == 0:
            return float('inf')  # Vertical line
        return (self.end.y - self.start.y) / dx
    
    def compute_horizontal_cross(self):
        return self.start.y * self.end.y < 0
    
    def compute_vertical_cross(self):
        return self.start.x * self.end.x < 0
    
    def discretize_line(self, n: int):
        if n < 2:
            raise ValueError("n must be at least 2 to discretize a line")
        self.points = [
            Point(
                self.start.x + i * (self.end.x - self.start.x) / (n - 1),
                self.start.y + i * (self.end.y - self.start.y) / (n - 1)
            ) for i in range(n)
        ]
    
class Shape:
    def __init__(self, is_regular: bool, edge: list["Line"], vertice: list["Point"], inner_angles: list[float]):
        if len(edge) < 3 or len(vertice) < 3 or len(inner_angles) < 3:
            raise ValueError("A shape must have at least 3 edges, vertices, and inner angles")
        self.is_regular = is_regular
        self.edge = edge
        self.vertices = vertice
        self.inner_angels = inner_angles

    def compute_area(self) -> float:
        raise NotImplementedError("Area computation must be implemented in subclasses")
    
    def compute_perimeter(self) -> float:
        return sum(line.compute_length() for line in self.edge)
    
    def compute_inner_angels(self) -> float:
        return sum(self.inner_angels)
    
class Rectangle(Shape):
    def __init__(self, vertices: list["Point"], edges: list["Line"]):
        if len(vertices) != 4 or len(edges) != 4:
            raise ValueError("Rectangle must have exactly 4 vertices and 4 edges")
        angles = [90, 90, 90, 90]
        super().__init__(is_regular=False, edge=edges, vertice=vertices, inner_angles=angles)
        self.width = edges[0].compute_length()
        self.height = edges[1].compute_length()
        
    def compute_area(self) -> float:
        return self.width * self.height
        
    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)
        
    def compute_inner_angels(self) -> float:
        return sum(self.inner_angels)
        
    def diagonal_length(self) -> float:
        return (self.width**2 + self.height**2)**0.5
        
class Square(Rectangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"]):
        if len(edges) != 4:
            raise ValueError("Square must have 4 edges")
        lengths = [edge.compute_length() for edge in edges]
        if not all(abs(lengths[0] - l) < 1e-6 for l in lengths):
            raise ValueError("All sides of a square must be equal in length")
        super().__init__(vertices, edges)
        self.side = lengths[0]
        
    def compute_area(self) -> float:
        return self.side ** 2
    
    def compute_perimeter(self) -> float:
        return 4 * self.side
    
    def compute_angles(self) -> float:
        return 360
    
class Triangle(Shape):
    def __init__(self, is_regular: bool, vertices: list["Point"], edges: list["Line"], inner_angles: list[float]):
        if len(vertices) != 3 or len(edges) != 3 or len(inner_angles) != 3:
            raise ValueError("Triangle must have 3 vertices, 3 edges, and 3 inner angles")
        if abs(sum(inner_angles) - 180) > 1e-5:
            raise ValueError("Sum of inner angles in a triangle must be 180 degrees")
        super().__init__(is_regular, edges, vertices, inner_angles)
        self.side1 = edges[0].compute_length()
        self.side2 = edges[1].compute_length()      
        self.side3 = edges[2].compute_length()
        self.angle1 = inner_angles[0]
        self.angle2 = inner_angles[1]
        self.angle3 = inner_angles[2]
        
    def compute_area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        area_squared = s * (s - self.side1) * (s - self.side2) * (s - self.side3)
        if area_squared < 0:
            raise ValueError("Invalid triangle dimensions")
        return area_squared ** 0.5
    
    def compute_perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3
    
    def compute_inner_angles(self) -> float:
        return self.angle1 + self.angle2 + self.angle3
    
    def is_acute(self) -> bool:
        return self.angle1 < 90 and self.angle2 < 90 and self.angle3 < 90
    
    def is_obtuse(self) -> bool:
        return self.angle1 > 90 or self.angle2 > 90 or self.angle3 > 90
    
    def is_right(self) -> bool:
        return self.angle1 == 90 or self.angle2 == 90 or self.angle3 == 90
    
    def triangle_type(self) -> str:
        if self.is_acute():
            return "Acute Triangle"
        elif self.is_obtuse():
            return "Obtuse Triangle"
        elif self.is_right():
            return "Right Triangle"
        else:
            return "Unknown Triangle Type"
        
class IsoscelesTriangle(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"], inner_angles: list[float]):
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=inner_angles)
        if not self.equal_sides():
            raise ValueError("An isosceles triangle must have at least two equal sides")
        
    def equal_sides(self) -> bool:
        return self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3
    
    def compute_area(self):
        if self.side1 == self.side2:
            equal_side = self.side1
            base = self.side3
        elif self.side2 == self.side3:
            equal_side = self.side2
            base = self.side1
        else:
            equal_side = self.side1
            base = self.side2
        area_squared = (base / 4) * (4 * equal_side**2 - base**2)
        if area_squared < 0:
            raise ValueError("Invalid side lengths for an isosceles triangle")
        return area_squared**0.5
    
class EquilateralTriangle(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"]):
        lengths = [edge.compute_length() for edge in edges]
        if not all(abs(lengths[0] - l) < 1e-6 for l in lengths):
            raise ValueError("All sides of an equilateral triangle must be equal")
        inner_angles = [60, 60, 60]
        super().__init__(is_regular=True, vertices=vertices, edges=edges, inner_angles=inner_angles)
        self.side = lengths[0]
        
    def height(self) -> float:
        return (self.side * (3**0.5)) / 2
    
    def compute_area(self) -> float:
        return (self.height() * self.side) / 2
    
class ScaleneTriangle(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"], inner_angles: list[float]):
        lengths = [edge.compute_length() for edge in edges]
        if lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[0] == lengths[2]:
            raise ValueError("No sides should be equal in a scalene triangle")
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=inner_angles)
        
    def compute_area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
class TriRectangle(Triangle):
    def __init__(self, vertices: list["Point"], edges: list["Line"], inner_angles: list[float]):
        if 90 not in inner_angles:
            raise ValueError("A right triangle must have one 90-degree angle")
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=inner_angles)
        
    def compute_area(self) -> float:
        if self.angle1 == 90:
            return (self.side2 * self.side3) / 2
        elif self.angle2 == 90:
            return (self.side1 * self.side3) / 2
        else:
            return (self.side1 * self.side2) / 2
