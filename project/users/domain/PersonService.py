from project.users.domain.Person import Person, PersonStatus
from project.users.domain.PersonRepository import PersonRepository


class PersonService:
    def __init__(self, person_repository: PersonRepository):
        self.personRepository = person_repository

    def register_when_active(self, person: Person):
        if person.status == PersonStatus.ACTIVE:
            self.personRepository.save(person)

    def find_actives_count(self):
        return self.personRepository.count_active()