from enum import Enum

class PersonStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

class Person:
    def __init__(self, name: str, age: int, status: PersonStatus):
        self.name = name
        self.age = age
        self.status = status