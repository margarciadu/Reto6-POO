from ShapePackage import Point, Line
from ShapePackage import Rectangle, Square
from ShapePackage import EquilateralTriangle, IsoscelesTriangle, ScaleneTriangle, TriRectangle

# Línea
p1 = Point(0, 0)
p2 = Point(3, 4)
line = Line(p1, p2)
print(f"Length of line: {line.compute_length():.2f}")
print(f"Slope of line: {line.compute_slope():.2f}")

# Rectángulo
rect_vertices = [Point(0, 0), Point(0, 4), Point(3, 4), Point(3, 0)]
rect_edges = [Line(rect_vertices[i], rect_vertices[(i + 1) % 4]) for i in range(4)]
rectangle = Rectangle(rect_vertices, rect_edges)
print(f"Rectangle area: {rectangle.compute_area()}")
print(f"Rectangle perimeter: {rectangle.compute_perimeter()}")

# Cuadrado
square_vertices = [Point(0, 0), Point(0, 3), Point(3, 3), Point(3, 0)]
square_edges = [Line(square_vertices[i], square_vertices[(i + 1) % 4]) for i in range(4)]
square = Square(square_vertices, square_edges)
print(f"Square area: {square.compute_area()}")
print(f"Square perimeter: {square.compute_perimeter()}")

# Triángulos
tri_vertices = [Point(0, 0), Point(4, 0), Point(2, 3)]
tri_edges = [Line(tri_vertices[i], tri_vertices[(i + 1) % 3]) for i in range(3)]
angles = [60, 60, 60]

equilateral = EquilateralTriangle(tri_vertices, tri_edges)
print(f"Equilateral Triangle area: {equilateral.compute_area()}")

isosceles = IsoscelesTriangle(tri_vertices, tri_edges, angles)
print(f"Isosceles Triangle area: {isosceles.compute_area()}")

scalene = ScaleneTriangle(tri_vertices, tri_edges, angles)
print(f"Scalene Triangle area: {scalene.compute_area()}")

tri_rect = TriRectangle(tri_vertices, tri_edges, [90, 45, 45])
print(f"Right Triangle area: {tri_rect.compute_area()}")