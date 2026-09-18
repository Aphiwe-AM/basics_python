from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    #set width method 
    def set_width(self,new_width: int) -> None:
        self._width = new_width

    def set_height(self, new_height) -> None:
        self._height = new_height

    def get_area(self) -> float:
        return self._width * self._height
    
    def get_perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def get_diagonal(self) -> float:
        return sqrt((self._width ** 2) + (self._height ** 2))
    
    def get_picture(self) -> str:
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self._height):
            picture += '*' * self._width + '\n'
        return picture
    
    def get_amount_inside(self, shape ) -> int:

        amount_width_fits = self._width // shape._width
        amount_height_fits = self._height // shape._height

        return amount_width_fits * amount_height_fits
    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"

class Square(Rectangle):
    def __init__(self, size):
        self._width = size
        self._height = size
    
    def __str__(self):
        return f'Square(side={self._width})'
    
    def set_width(self, new_width: float) -> None:
        self._width = new_width
        self._height = new_width
        
    def set_height(self, new_height: float) -> None:
        self._width = new_height
        self._height = new_height

    def set_side(self, side: float) -> None:
         self._width = side
         self._height = side




print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))

