"""Define the User model"""
import uuid
import dataclasses

@dataclasses.dataclass
class User:
    user_id: str
    name: str
    last_name: str
    gov_id: str
    email: str
    company: str


    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
