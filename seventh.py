#Coding
# Object Creation and Usage in Python

class person:
    # A class to represent a person.

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

        def greet(self):
            #Method to diaplay a greeting message.
            return f"Hello, my name is {self.name}, I'm {self.age} years old and I live in {self.city}."
        
        def update_age(self, new_age):
            # Method to update the age of the person.
            self.age = new_age
            return f"{self.name}'s age has been updated to {self.age}."
        
        def move_city(self, new_city):
            #Method to update the city of residence.
            self.city = new_city
            return f"{self.name} has moved to {self.city}."
        
        # Main function to create and interact with objects.
        def main():
            # Create objects of the person class 

            person1 = person("Alice", 25, "New York")
            person2 = person("Bob", 30, "Los Angeles")

            # Display initial information about the objects 
            print("Intial object Information:")
            print(person1.greet())
            print(person2.greet())

            # Update the attributes of the objects
            print("\nUpdating Attributes:")
            print(person1.update_age(26))
            print(person2.move_city("San Francisco"))

            # Display updated information
            print("\nUpdated Object Information:")
            print(person1.greet())
            print(person2.greet())

            # Create another object and interact with it
            print("\nCreating and Interacting with Another Object:")
            person3 = person("Charlie", 35, "Chicago")
            print(person3.greet())
            print(person3.update_age(36))
            print(person3.move_city("Boston"))
            print(person3.greet())

            # Entry point of the program
        if __name__ == "__main__":
            main()