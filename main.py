from db import DBClientPerson
from db import Session


session = Session()
client = DBClientPerson(session)
print(client.get_person_by_id(1))
client.add_person("ilyas", "Niyazov", True, 2, [4, 9])
print(client.get_person_by_id(1))
