from model import Person


def test_person_age():
    person: Person = Person.Person("Albert Einstein", "Alby", 1879)
    assert person.get_age(2020) == 141
