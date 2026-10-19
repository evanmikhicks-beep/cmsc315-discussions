"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# 1:
# Create a parent class.

class Electronic:
    """A base class supporting a variety of types of electronics in a storefront"""

    STOREFRONT = "H Labs"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"The {self.name} costs: ${self.price:.2f}."

# 2:
# Create a child class that inherits from the parent class.

class Drone(Electronic):

    ORIGIN = "Assembled locally"

    def __init__(self, name, price, weight, propulsion, battery):
        super().__init__(name, price)
        self.weight = weight    #weight is measured in grams
        self.propulsion = propulsion
        self.battery = battery    #battery capacity is measured in watt-hours

    def estimate_flight_hours(self): #a simplified model of flight-hour calculation
        if self.propulsion == "quadcopter":
            return self.battery * 0.33 / self.weight
        elif self.propulsion == "single rotor":
            return self.battery * 0.5 / self.weight
        else:
            return "Unknown endurance"

    def get_details(self):
        return (
            super().get_details()
            + f"\nThis drone weighs {self.weight} grams, "
            + f"has a {self.propulsion} propulsion system, "
            + f"a battery capacity of {self.battery} watt-hours, "
            + f"and an endurance of {self.estimate_flight_hours()} hours."
        )

# 3:
# Create a function that demonstrates class namespaces and instance namespaces.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    smallQuadcopter = Drone("Small Quadcopter", 52.80, 15, "quadcopter", 45)
    proFilmDrone = Drone("Professional Camera Drone", 499.99, 50, "single rotor", 250)

    print("Origin of our drones for sale: " + Drone.ORIGIN)
    print("Origin of the small quadcopter: " + smallQuadcopter.ORIGIN)

    smallQuadcopter.inventoryAmount = 10 #one attribute is added to an object after creation

    print(smallQuadcopter.__dict__) #printing the instance namespace of smallQuadcopter
    print(proFilmDrone.__dict__) #printing the instance namespace of the pro film drone

    print("Details about Drone class namespace: ", Drone.__dict__)

# 4:
# Demonstrate deep and shallow copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    resistor = Electronic("Resistor", 0.30) #creating a resistor object priced at $0.30
    resistor.ratings = [0.2, 0.4] #resistance in ohms, nested mutable data

    newResistor = copy(resistor) #creating a shallow copy of a resistor
    anotherResistor = deepcopy(resistor) #creating a deep copy of a resistor

    resistor.ratings.append(0.06) #modification of the original object's nested data

    print("original resistor: ", resistor.__dict__)
    print("Shallow copy: ", newResistor.__dict__)
    print("Deep copy: ", anotherResistor.__dict__)

    #The shallow copy shares the nested list of the original, while the deep copy has independent data that was not modified



# 5:
# Complete the main function.

def main():
    print("=== Unit 1 OOP Assignment ===")


    someBattery = Electronic("Battery", 22.50) #creating one object from the parent class
    microDrone = Drone("Micro Drone", 105.50, 5, "quadcopter", 15) #creating one object from the child class

    print(someBattery.get_details())
    print(microDrone.get_details()) #a method call which demonstrates inheritance

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()