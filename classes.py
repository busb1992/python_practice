# enum class
from enum import Enum, unique, auto

@unique         # this wont let to asign same value to different names
class Peppers(Enum):
    Habanero = 1
    Jalapeno = 2
    Ghost = 3
    Reaper = 4
    Scorpion = auto()

print(Peppers.Habanero)
print(type(Peppers.Habanero))
print(repr(Peppers.Habanero))
print(Peppers.Habanero.name)
print(Peppers.Habanero.value)

print(Peppers.Scorpion.name)
print(Peppers.Scorpion.value)

# string class functiions

