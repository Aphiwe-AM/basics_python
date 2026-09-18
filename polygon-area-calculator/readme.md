# Polygon Area Calculator

An object-oriented Python program built as part of the **freeCodeCamp Scientific Computing with Python** certification. This project uses class inheritance to model and calculate properties of Rectangles and Squares.

## 🚀 Features

- **Rectangle Class:** Set dimensions, calculate area, perimeter, and diagonal length.
- **Square Class:** Inherits from `Rectangle`, ensuring that width and height always stay equal using `super()`.
- **ASCII Art Generator:** Generate an ASCII text-based picture using `*` symbols if dimensions are under 50 units.
- **Shape Packing Calculator:** Calculate exactly how many times a smaller shape can fit inside a larger shape without rotation.

## 🛠️ Usage Example

```python
from shape_calculator import Rectangle, Square

# Create a rectangle
rect = Rectangle(15, 10)
print(rect.get_area())       # Output: 150
print(rect.get_perimeter())  # Output: 50

# Create a square
sq = Square(5)
print(sq.get_diagonal())     # Output: 7.0710678118654755

# Calculate how many squares fit inside the rectangle
print(rect.get_amount_inside(sq))  # Output: 6

# Draw the square
print(sq.get_picture())
# Output:
# *****
# *****
# *****
# *****
# *****
```

## 📝 Testing

This project is fully compliant with the automated freeCodeCamp test suite. Run your unit tests using:
```bash
python main.py
```
