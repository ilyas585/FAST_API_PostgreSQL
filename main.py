from db import DBClientPerson
from db.session import Session

session = Session()
client = DBClientPerson(session)
# print(client.get_person_by_id(1))
# client.add_person("ilyas", "Niyazov", True, None, [3, 9])
# print(client.get_person_by_id(1))
# client.add_person("Biyaslan", "Mokaev", False)
# client.add_person("Ivan", "Ivanov", True, None, [5, 6, 7])

print(client.get_persons_by_kid_id(7))
