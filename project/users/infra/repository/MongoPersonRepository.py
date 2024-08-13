from pymongo import MongoClient

from project.users.domain.Person import Person
from project.users.domain.PersonRepository import PersonRepository


class MongoPersonRepository(PersonRepository):
    def __init__(self, db_uri = 'mongodb://localhost:27017/', db = 'test'):
        self.client = MongoClient(db_uri)
        self.db = self.client[db]
        self.collection = self.db['users']

    def save(self, person: Person) -> None:
        self.collection.insert_one({
            'name': person.name,
            'age': person.age,
            'status': person.status.name,
        })

    def count_active(self) -> int:
        return self.collection.count_documents({'status': 'ACTIVE'})

    def remove_all(self):
        self.collection.drop()