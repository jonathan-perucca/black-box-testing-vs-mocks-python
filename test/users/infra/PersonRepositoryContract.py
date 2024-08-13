import unittest
from abc import ABC, abstractmethod

from project.users.domain.Person import Person, PersonStatus
from project.users.domain.PersonRepository import PersonRepository


class PersonRepositoryContract(ABC, unittest.TestCase):
    @abstractmethod
    def repository(self) -> PersonRepository:
        raise NotImplementedError("Need repository definition")

    def setUp(self):
        self.repo: PersonRepository = self.repository
        self.repo.remove_all()

    def test_should_save_person(self):
        self.repo.save(Person(
            name = 'John',
            age = 44,
            status = PersonStatus.ACTIVE
        ))

        self.assertEqual(
            first = 1,
            second = self.repo.count_active(),
        )

    def test_should_count_only_active_person(self):
        self.repo.save(Person(
            name = 'John',
            age = 44,
            status = PersonStatus.ACTIVE
        ))
        self.repo.save(Person(
            name = 'John',
            age = 44,
            status = PersonStatus.INACTIVE
        ))

        self.assertEqual(
            first = self.repo.count_active(),
            second = 1,
        )