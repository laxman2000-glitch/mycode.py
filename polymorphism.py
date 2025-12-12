#polymorphism with example with same method 
class Car:
    def move(self):
        print("Car is driving")

class Aeroplane:
    def move(self):
        print("Aeroplane is flying")

class Ship:
    def move(self):
        print("Ship is sailing")

def start(obj):
    obj.move()

start(Car())
start(Aeroplane())
start(Ship())

#polymorphism with same operator (operator overloading)

print(10 + 20)       # addition
print("hi" + "bye")  # concatenation
print([1,2] + [3,4]) # list merge
