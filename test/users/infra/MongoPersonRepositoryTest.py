from project.users.infra.repository.MongoPersonRepository import MongoPersonRepository
from test.users.infra.PersonRepositoryContract import PersonRepositoryContract


class MongoPersonRepositoryTest(PersonRepositoryContract):
    @property
    def repository(self):
        return MongoPersonRepository(db = 'integration_test')
