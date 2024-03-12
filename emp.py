class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Your name is: {self.name}" # return use krte bcz in methods ko generally print nhi krate ek dosri file mai import krate hai 
    
    def __repr__(self):
        return f"Hello {self.name}"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
        # return len(self.name)
    def __call__(self):
        print(f"{self.name} is a good boy")