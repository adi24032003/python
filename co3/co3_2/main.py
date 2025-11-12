from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter

from graphics.threedgraphics.cuboid import *
cb_a = area
cb_p = perimeter

from graphics.threedgraphics.sphere import *
sp_a = area
sp_p = perimeter

# --- 2D Figures ---
print("Rectangle area:", rect_area(10, 5))
print("Rectangle perimeter:", rect_perimeter(10, 5))
print("Circle area:", circle_area(7))
print("Circle perimeter:", circle_perimeter(7))

# --- 3D Figures ---
print("Cuboid area:", cb_a(2, 3, 4))
print("Cuboid perimeter:", cb_p(2, 3, 4))

print("Sphere area:", sp_a(5))
print("Sphere perimeter:", sp_p(5))
