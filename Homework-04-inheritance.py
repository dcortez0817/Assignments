class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print('...')

#1. Implement the Cat class by inheriting from the Pet class. Make sure to use 
#   superclass methods wherever possible. In addition, add a lose_life method to the Cat class.

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    def talk(self):
        print('meow!')
    def lose_life(self):
        if lives > 0:
            lives = lives - 1
        else:
            is_alive = False

#2. Assume these commands are entered in order. What would Python output?
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)
print(f.a)
# prints what 4

print(b.a)
# prints 3

print(f.garply())
# This won't run because the function 'garply' calls on the function 'baz', and the 'Foo'
# class contains the 'garply' method but not the 'baz' method. Since 'baz' is a method   
# used in the 'Bar' class and the 'Bar' class inherits the methods from Foo, the 'Bar' 
# class will run 'garply' but Foo won't because 'baz' isn't a method used the 'Foo' class.

print(b.garply())
# prints 3

b.a = 9
print(b.garply())
# prints 9

f.baz = lambda val: val * val
print(f.garply())
# prints 16