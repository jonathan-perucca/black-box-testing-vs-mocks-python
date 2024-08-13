from project.users.domain.Person import Person, PersonStatus
from project.users.domain.PersonRepository import PersonRepository


class InMemoryPersonRepository(PersonRepository):
    def __init__(self):
        self.persons = []

    def save(self, person: Person) -> None:
        self.persons.append(person)

    def count_active(self) -> int:
        return len([person for person in self.persons if person.status == PersonStatus.ACTIVE])

    def remove_all(self) -> None:
        self.persons = []