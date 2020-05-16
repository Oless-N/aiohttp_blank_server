import asyncio
import datetime
import uuid

import motor.motor_asyncio
from setting import cfg
client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://{cfg["mongo"]["host"]}:{cfg["mongo"]["port"]}')
db = client[cfg["mongo"]["db_name"]]
collection = db['User']

async def insert_to_db(documents: dict):
    loop = asyncio.get_event_loop()
    if len(documents) > 1:
        loop.run_until_complete(await db['test_collection'].insert_one(documents[0]))
    elif len(documents) is 1:
        loop.run_until_complete(await db['test_collection'].insert_many(documents))
    else:
        raise ValueError('Bad Input Value Error less than 1')

def get_all_from_coll(collection:str):
    async def __await_get__(collection):
        cursor = db[collection].find()
        ret = []
        for document in await cursor.to_list(length=5000000):
            ret.append(document)
        return ret
    loop = asyncio.get_event_loop()
    ls = loop.run_until_complete(__await_get__(collection))
    return ls

async def __await_get__(field, param):
    cursor = db['User'].find({field:param})
    ret = []
    for document in await cursor.to_list(length=5000000):
        ret.append(document)
    return ret

def custom_filter(field, param):
    loop = asyncio.get_event_loop()
    ls = loop.run_until_complete(__await_get__(field, param))
    return ls

class User():
    def __init__(self, name: str, age: str, city: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.city = city
        self.created_date = datetime.datetime.now()

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, o):
        if self.name is o.name and self.age is o.age and self.city is o.city:
            return True
        else:
            return False

async def __await_insert__(user:User):
    await db[user.__class__.__name__].insert_one(user.__dict__)
