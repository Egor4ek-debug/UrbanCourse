# import math
#
# class Figure:
#     sides_count = 0
#
#     def __init__(self, color, *sides):
#         if len(sides) != self.sides_count:
#             sides = [1] * self.sides_count
#         self.__sides = list(sides)
#         self.__color = list(color)
#         self.filled = False
#
#     def get_color(self):
#         return self.__color
#
#     def __is_valid_color(self, r, g, b):
#         return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))
#
#     def set_color(self, r, g, b):
#         if self.__is_valid_color(r, g, b):
#             self.__color = [r, g, b]
#
#     def __is_valid_sides(self, *sides):
#         return all(isinstance(side, int) and side > 0 for side in sides)
#
#     def get_sides(self):
#         return self.__sides
#
#     def __len__(self):
#         return sum(self.__sides)
#
#     def set_sides(self, *new_sides):
#         if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
#             self.__sides = list(new_sides)
#
#
# class Circle(Figure):
#     sides_count = 1
#
#     def __init__(self, color, *sides):
#         super().__init__(color, *sides)
#         self.__radius = self.__calculate_radius()
#
#     def __calculate_radius(self):
#         return self.get_sides()[0] / (2 * math.pi)
#
#     def get_square(self):
#         return math.pi * self.__radius ** 2
#
#
# class Triangle(Figure):
#     sides_count = 3
#
#     def get_square(self):
#         a, b, c = self.get_sides()
#         s = (a + b + c) / 2
#         return math.sqrt(s * (s - a) * (s - b) * (s - c))
#
#
# class Cube(Figure):
#     sides_count = 12
#
#     def __init__(self, color, *sides):
#         if len(sides) != 1:
#             sides = [1] * self.sides_count
#         else:
#             sides = [sides[0]] * self.sides_count
#         super().__init__(color, *sides)
#
#     def get_volume(self):
#         side_length = self.get_sides()[0]
#         return side_length ** 3
#
#
# circle1 = Circle((200, 200, 100), 10)
# cube1 = Cube((222, 35, 130), 6)
#
# circle1.set_color(55, 66, 77)
# print(circle1.get_color())
#
# cube1.set_color(300, 70, 15)
# print(cube1.get_color())
#
# cube1.set_sides(5, 3, 12, 4, 5)
# print(cube1.get_sides())
#
# circle1.set_sides(15)
# print(circle1.get_sides())
#
# print(len(circle1))
# print(cube1.get_volume())
import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.filled == True:
            print(f'Фигура уже закрашена, хоите поменять цвет на {[r, g, b]}?\n 1 - да, 2 - нет')
            answer = int(input())
            if answer == 2:
                print('Фигура не изменила цвет')
                return
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__([side], color)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *([side] * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((123, 51, 21), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(61, 22, 41)
print(triangle1.get_color())
triangle1.set_color(1, 1, 1)
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
triangle1.set_sides(31, 2, 51, 2)
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(len(triangle1))

# Проверка объёма (куба):
print(cube1.get_volume())
