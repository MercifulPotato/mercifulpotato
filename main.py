from datetime import datetime

from model import Person

person: Person = Person.Person("Albert Einstein", "Alby", 1987)
print(f"{person.preferred_name} is about {person.get_age(datetime.utcnow().year)} years old.")
