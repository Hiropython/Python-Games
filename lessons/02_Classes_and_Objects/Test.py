class Person:
    """Person represents a person in our system."""

     # This is the initializer, it gets run when we create a new object
    def __init__(self, name: str,last_name, age: int):
        """Initializes a new Person object."""
        self.name = name
        self.age = age
        self.last_name= last_name
        
    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        print(f"Hello, my name is {self.name} {self.last_name} and I am {self.age} years old. {message}")
        
        
class Parent(Person):
    """Parent represents a parent in our system."""

    def __init__(self, name: str, last_name, age: int, spouse=None):
        """Initializes a new Parent object."""
        super().__init__(name,last_name, age) # Call Person.__init__ to initialize the name and age attributes
        self.children = []
        
        # Set our spose but also set the spouse's spouse to us
        if spouse:
            self.spouse = spouse
            spouse.spouse = self
        
        self.spouse = None

    def add_child(self, child: Person):
        """Adds a child to the parent's list of children."""
        self.children.append(child)
        
        

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        
        super().say_hello(message)
        if self.spouse:
            print(f"My spouse is {self.spouse.name} {self.spouse.last_name}")
            
        print(f"I have {len(self.children)} children.")

        if len(self.children) > 0:
            print("Their names are:")
            for child in self.children:
                print(f"  {child.name} {child.last_name} {child.age}")
                
    def print_fam(self):
        print(f"{self.spouse.name} {dad.last_name}, {self.children[0].name} {self.children[0].last_name}, {self.children[1].name} {self.children[1].last_name}")            
class Child(Person):
    """Child represents a child in our system."""

    def __init__(self, name: str, last_name,age: int, parents: list):
        """Initializes a new Child object."""
        super().__init__(name, last_name,age)  # Call Person.__init__ to initialize the name and age attributes
        self.parents = parents
        for parent in parents:
            parent.add_child(self)

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        super().say_hello(message)
        print(f"My parents are {', '.join([f"{parent.name } {parent.last_name}" for parent in self.parents])}")
        
        
# Now lets make a family
mom = Parent("Alice","Boberson", 35)
dad = Parent("Bob","Boberson", 40, mom)

charlie = Child("Charlie","Boberson", 10, [mom, dad])
dahlia = Child("Dahlia", "Boberson", 8, [mom, dad])

# Connect the children to the parents

dad.add_child(charlie)
dad.add_child(dahlia)


mom.say_hello("Hello!") # Call the say_hello method of the mom object
print()
dahlia.say_hello("Yo!")
mom.print_fam()