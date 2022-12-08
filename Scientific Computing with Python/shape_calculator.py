
class Rectangle:
    # initializes the object
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # sets the width of the rectangle
    def set_width(self, width):
        self.width = width

    # sets the height of the rectangle
    def set_height(self, height):
        self.height = height

    # returns the area
    def get_area(self):
        self.area = self.width * self.height
        return self.area

    #returns the perimeter
    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter

    # returns the diagonal
    def get_diagonal(self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return self.diagonal

    # returns a picture of the shape from *
    def get_picture(self):
        self.picture = []
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            self.picture.append("*" * self.width)
        return "\n".join(self.picture) + "\n"

    # calculates how many of a new shape can fit inside the original
    def get_amount_inside(self, shape):
        self.in_width = shape.width
        self.in_height = shape.height
        height_in = self.height // self.in_height
        width_in = self.width // self.in_width
        inside = height_in * width_in
        return inside

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side=0, ):
        Rectangle.__init__(self, width=0, height=0)
        self.side = side
        self.width = side
        self.height = side

    # changes the width and height
    def set_side(self, side):
        self.width = side
        self.height = side

    # sets the height and width to the same length
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    # returns the width of the square
    def __repr__(self):
        return f"Square(side={self.width})"
