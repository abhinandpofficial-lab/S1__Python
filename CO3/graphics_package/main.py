from graphics.rectangle import area as ra,perimeter as rp
from graphics.circle import area as ca,circumference as cp
from graphics.graphics_3d.cuboid import surface_area as sa,volume as cv
from graphics.graphics_3d.sphere import surface_area as suar,volume as vol
print("Rectangle area:",ra(10,5))
print("Rectangle perimeter:",rp(10,5))
print("\n Circle Area:",ca(7))
print("circle perimeter:",cp(7))
print("\n Cuboid Area:",sa(2,3,4))
print("cuboid perimeter:",cv(2,3,4))
print("\n sphere Area:",suar(5))
print("sphere perimeter:",vol(5))

