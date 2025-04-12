class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Other is another vector
    def __add__(self, other):
        # Return a new vector with the sum of the x and y components
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"


vec1 = Vector(1, 2)
vec2 = Vector(3, 4)
vec3 = vec1 + vec2
print(vec1)
print(vec2)
print(vec3)
