# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

class Animal:
    def __init__(self, name, gender, color):
        self.name = name
        self.gender = gender
        self.color = color
    def speed(self, distance, time):
        self.distance = distance
        self.time = time
        return self.distance/self.time
    def show(self):
        print(f"Animal Name: {self.name}",'\n'f"Gender: {self.gender}",'\n'f"Color: {self.color}")
        
class Cat(Animal):
    def __init__(self, name, gender, color,sound, food):
        super().__init__(name,gender,color)
        self.sound = sound
        self.food = food
    def speed(self, distance, time):
        return 10 * super().speed(distance,time)
    def child(self,son, daughter):
        self.son = son
        self.daughter = daughter
        print(f"Child Son: {self.son}",'\n'f"Child Daughter: {self.daughter}")
    def show(self):
        print(f"Animal Name: {self.name}",'\n'f"Gender: {self.gender}",'\n'f"Color: {self.color}",'\n'f"Sound: {self.sound}",'\n'f"Food: {self.food}")
    
a = Animal("Dog","Male","White")
a.show()    
print(f"Speed: {a.speed(35,5)} m/s")
print()
c = Cat("Catty","Female","Brown","Moew","Meat")
c.show()
print(f"Speed: {c.speed(35,5)} m/s")
c.child(2,3)