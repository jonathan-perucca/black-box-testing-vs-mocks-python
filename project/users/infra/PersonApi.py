import random

from flask import jsonify

from app import app
from project.users.domain.Person import Person, PersonStatus
from project.users.domain.PersonService import PersonService
from project.users.infra.repository.MongoPersonRepository import MongoPersonRepository

person_service = PersonService(MongoPersonRepository())

@app.route('/save_person')
def save_person():
    counter = random.randint(1, 999999)
    person_service.register_when_active(Person(
        name = f"Talk-{counter}",
        age = random.randint(20, 55),
        status = PersonStatus.ACTIVE
    ))

    return jsonify(
        message = "ok",
    )