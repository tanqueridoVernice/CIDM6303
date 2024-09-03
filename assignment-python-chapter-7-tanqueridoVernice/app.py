# Watching the short videos at codewithmosh.com is very important for
# understanding this chapter
# Vernice Tanquerido

# Chapter 7.1 Classes
# Nothing to code. Know the following:
# Class is a blueprint for creating new objects
# Object is instance of a class

# Chapter 7.2 Creating Classes
print("\nChapter 7.2 Creating Classes")
# Start coding here...
print("\nChapter 7.2 Creating Classes")


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, int))

# Chapter 7.3 Constructors
print("\nChapter 7.3 Constructors")
# We have to change the class name through this activity because
# Classes with the same name cannot exist in the same app.py


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


# an object is a variable of type class
# create an object named 'point' from a class named Point()
# This is called "instantiating an object"
point = Point3(1, 2)
point.draw()

# Chapter 7.4 Class vs. instance attributes
print("\nChapter 7.4 vs Instance attributes")


class Point4:
    # class attribute
    default_color = "red"

    def __init__(self, x, y):
        # instance attributes
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


# class attributes are accessible even without instantiating an object
Point4.default_color = "yellow"

point = Point4(1, 2)
print(point.default_color)
print(Point4.default_color)
point.draw()

# instantiate another object of class Point()
another = Point4(3, 4)
print(another.default_color)
another.draw()


# Chapter 7.5 Class vs. Instance Methods
print("\nChapter 7.5 Class vs Instance Methods")


class Point5:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


# Class methods can be run even without instantiating an object
point = Point5.zero()
point.draw()

# Chapter 7.6 Magic methods
print("\nChapter 7.6 Magic Methods")
# Remember that 'magic methods' are methods that begin
# with two underscores and end with two underscores


class Point6:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point6(1, 2)
print(str(point))

# Chapter 7.12
print("\Chapter 7.12 Inheritance")
# The Mammal and Fish classes inherit the eat() method from the Animal class and inherit an instance attribute 'age' from the Animal class
# Terms to know.
# Animal: Patent class or base class
# Mammal and Fish: Child class or subclass


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)

f = Fish()
f.eat()
f.age = 3
print(f.age)
