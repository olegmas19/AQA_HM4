import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    pnonenumber: str
    dateOfBirth: []
    subject: str
    hobbies1: str
    hobbies2: str
    hobbies3: str
    attachment: str
    address: str
    state: str
    city: str


ivan = User(
    first_name='Иван',
    last_name='Иванов',
    email='Ivan@mail.ru',
    pnonenumber='9999999999',
    dateOfBirth=['29', 'February', '1992'],
    subject='History',
    hobbies1='Sports',
    hobbies2='Reading',
    hobbies3='Music',
    attachment='IMG_1332.JPEG',
    address='Солнечная ул., д. 12 кв.137',
    state='Haryana',
    city='Karnal',
)
