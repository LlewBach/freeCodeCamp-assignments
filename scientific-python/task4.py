class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, val):
        self.width = val

    def set_height(self, val):
        self.height = val
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        star_string = ''
        for i in range(self.height):
            star_string += f"{'*' * self.width}\n"
        return star_string
    
    def get_amount_inside(self, obj):
        obj_width = obj.width
        obj_height = obj.height
        width_multiple = self.width // obj_width
        height_multiple = self.height // obj_height
        return width_multiple * height_multiple
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, val):
        self.width = val
        self.height = val
    
    def set_height(self, val):
        self.width = val
        self.height = val

# TESTING ===============================

rect = Rectangle(7, 3)
print("width", rect.width)
print("height", rect.height)
print(rect.get_picture())