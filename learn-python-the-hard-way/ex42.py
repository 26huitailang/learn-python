## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ?? Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ?? Dag has-a name
        self.name = name

## ?? Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ?? Cat has-a name
        self.name = name

## ?? Person is-a object
class Person(object):

    def __init__(self, name):
        ## ?? Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ?? Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ?? Employee has-a salary
        self.salary = salary

## ?? is-a
class Fish(object):
    pass

## ?? is-a
class Salmon(Fish):
    pass

## ?? is-a
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ?? is-a
satan = Cat("Satan")

## ?? is-a
mary = Person("Mary")

## ?? Mary has-a pet is-a Cat which has-a name is satan
mary.pet = satan

## ?? Frank is-a Employee who has-a salary 120000
frank = Employee("Frank", 120000)

## ?? Frank is-a Employee who has-a salary 120000 has-a pet which has-a name is rover
frank.pet = rover

## ?? flipper is-a fish
flipper = Fish()

## ?? is-a
crouse = Salmon()

## ?? is-a
harry = Halibut()