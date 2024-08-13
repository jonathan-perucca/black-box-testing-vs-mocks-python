from test.users.infra.InMemoryPersonRepository import InMemoryPersonRepository
from test.users.infra.PersonRepositoryContract import PersonRepositoryContract


class InMemoryPersonRepositoryTest(PersonRepositoryContract):
    @property
    def repository(self):
        return InMemoryPersonRepository()

