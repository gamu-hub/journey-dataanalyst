class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    # Method 1: Bark
    def bark(self):
        return(f"{self.name} is barking")
    
    # Method 2: Run speed
    def run_speed(self):
        return (self.weight / self.age * 10)

    # Method 3 : Fight
    def fight(self, other_dog):

        # Calculate fighting scores
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return(f"{self.name} is the winner")
        else:
            return(f"{other_dog.name} is the winner")

dog1 = Dog("Bibi", 3, 20)
dog2 = Dog("Sawnnu", 5, 20)
dog3 = Dog("Kulfi", 7,17)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))

    
