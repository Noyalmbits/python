
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
r1=rectangle(10,5)
r2=rectangle(8,6)
print("rectangle 1:")
print("area:",r1.area())
print("perimeter:",r1.perimeter())
print("\nrectangle 2:")
print("area:",r2.area())
print("perimeter:",r2.perimeter())
if r1.area()>r2.area():
	print("\nrectangle 1 has greter area")
elif r1.area()<r2.area():
	print("\n rectangle 2 has greater area")
else:
	print("\n both rectangle have equal area")
