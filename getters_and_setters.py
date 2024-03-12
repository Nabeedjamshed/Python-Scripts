# by using getter and setter ksi bhi function ki return value ko ek object ki property ki tanha use krskte hai or usse set bhi krskte hai

class Myclass:
    def __init__(self, value):
        self.value = value
    def printdata(self):
        print(f"Value is {self.value}")

    @property # --> Getters (@property lgane se mehod property bnjata hai then object isse ek property ki tanha use krskta)
    def ten_value(self):  #ten_value ek method hai or usse like ek property ki tanha print krarhe . lga kr due to getter and setter. getter and setter is not a property it is method jo hidden hai but ye user ko aese dikhaega jese ye ek property hai.
        return 10 * self.value
    
    @ten_value.setter # ---> Setters  
    def ten_value(self, newval):
        self.value = newval / 10

a = Myclass(10)
a.ten_value = 67   #ten_value is a method but it is print like a property.
print(a.ten_value)
a.printdata()

# attribute is also called property and method is called function

# In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of 
# the property hidden(means function hidden hai wo just ek property ki tanha use horha). This can be useful for encapsulation and data validation.