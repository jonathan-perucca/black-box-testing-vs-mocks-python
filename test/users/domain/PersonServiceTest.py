import unittest

from project.users.domain.Person import Person, PersonStatus
from project.users.domain.PersonService import PersonService
from test.users.infra.InMemoryPersonRepository import InMemoryPersonRepository

# mock
# no mock - in memory
class PersonServiceTest(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryPersonRepository()
        self.service = PersonService(self.repository)

    def test_should_save_active_persons(self):
        person_active = Person(
            name = "John",
            age = 18,
            status = PersonStatus.ACTIVE,
        )

        self.service.register_when_active(person_active)

        self.assertEqual(
            first = self.repository.count_active(),
            second = 1
        )

    def test_should_not_save_inactive_person(self):
        person_inactive = Person(
            name = "Wesley",
            age = 20,
            status = PersonStatus.INACTIVE,
        )

        self.service.register_when_active(person_inactive)

        self.assertEqual(
            first = self.repository.count_active(),
            second = 0
        )