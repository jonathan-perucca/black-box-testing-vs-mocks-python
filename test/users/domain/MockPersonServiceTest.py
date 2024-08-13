import unittest
from unittest.mock import patch

from project.users.domain.Person import Person, PersonStatus
from project.users.domain.PersonRepository import PersonRepository
from project.users.domain.PersonService import PersonService


class MockPersonServiceTest(unittest.TestCase):
    def setUp(self):
        self.repository = PersonRepository()
        self.service = PersonService(self.repository)

    def test_should_save_active_persons(self):
        person_active = Person(
            name = "Alice",
            age = 30,
            status = PersonStatus.ACTIVE
        )

        with patch.object(self.repository, 'save') as mock_save:
            self.service.register_when_active(person_active)
            mock_save.assert_called_once_with(person_active)

    def test_should_not_save_inactive_person(self):
        person_inactive = Person(
            name = "Wesley",
            age = 20,
            status = PersonStatus.INACTIVE,
        )

        with patch.object(self.repository, 'save') as mock_save:
            self.service.register_when_active(person_inactive)
            mock_save.assert_not_called()

