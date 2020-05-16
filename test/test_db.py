import asyncio
from random import randrange

import motor.motor_asyncio
from models import User

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27027')
db = client['admin']
collection = db['User']


def cteate_collection():
    pass




def test_insert_toDB(user:User):
    async def create_document():
        document = user.__dict__
        await db['test_collection'].insert_one(document)
        # print('result %s' % repr(result.inserted_id))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_document())




def test_get():
    async def get_all_from_coll(col):
        cursor = db[col].find()
        ret = []
        for document in await cursor.to_list(length=5):
            ret.append(document)
        return ret

    loop = asyncio.get_event_loop()
    ls = loop.run_until_complete(get_all_from_coll('User'))
    return ls


def custom_filter(field, param):
    async def __await_get__():
        cursor = db['User'].find({field:param})
        ret = []
        for document in await cursor.to_list(length=5000000):
            ret.append(document)
        return ret
    loop = asyncio.get_event_loop()
    ls = loop.run_until_complete(__await_get__())
    return ls

print(test_get())
print(custom_filter('age', 23))
cityes = [
    "New York.",
    "Los Angeles.",
    "Chicago.",
    "Houston.",
    "Phoenix.",
    "Philadelphia.",
    "San Antonio.",
    "San Diego."
]

def gen_users():
    for i in range(200):
        current=User(f"worker {i}", randrange(18, 65, 1), cityes[randrange(0, len(cityes), 1)])
        test_insert_toDB(current)
