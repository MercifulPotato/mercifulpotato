from model import Person


def test_person_age():
    person: Person = Person.Person('Albert Einstien', 'Alby', 1987)
    assert person.get_age() == 42
