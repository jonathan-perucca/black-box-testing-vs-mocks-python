from project.users.domain.Person import Person


class PersonRepository:
    def save(self, person: Person) -> None:
        raise NotImplementedError()

    def count_active(self) -> int:
        raise NotImplementedError()

    def remove_all(self) -> None:
        raise NotImplementedError()