# Python code with a class

class Dog:
  """
  A simple class to represent a dog.
  """

  def __init__(self, name, breed):
    """
    Initializes a Dog object.

    Args:
      name: The name of the dog.
      breed: The breed of the dog.
    """
    self.name = name
    self.breed = breed

  def bark(self):
    """
    Returns the sound of the dog barking.
    """
    return "Woof!"

  def get_description(self):
    """
    Returns a description of the dog.
    """
    return f"{self.name} is a {self.breed}."

# Create a new Dog object
my_dog = Dog("Buddy", "Golden Retriever")

# Print the dog's information
print(my_dog.get_description())  # Output: Buddy is a Golden Retriever.
print(my_dog.bark())  # Output: Woof!
 
