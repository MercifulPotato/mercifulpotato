from dataclasses import dataclass


@dataclass
class Person:
    legal_name: str
    preferred_name: str
    year_of_birth: int

    def __init__(self, legal_name: str, preferred_name: str, year_of_birth: int):
        self.legal_name = legal_name
        self.preferred_name = preferred_name
        self.year_of_birth = year_of_birth

    def get_age(self, current_year: int) -> int:
        return current_year - self.year_of_birth
