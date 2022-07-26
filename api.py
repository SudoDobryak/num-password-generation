import hashlib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


class Answer(BaseModel):
    code: str
    salt: str
    hash: str


class Item(BaseModel):
    lenght_code: int
    lenght_salt: int


def generate_password(length):
    chars = list('+-/*!&$#?=w@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    return pasw


def hash_func(data):
    hash_object = hashlib.sha1(data.encode()).hexdigest()
    return hash_object


somedata = {'code': '1labels', 'salt': '1sequences', 'hash': 'fwefqsdx'}




#@app.get('/getapi')
#def get():
#    return somedata


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items/")
async def read_item(skip, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }

'''
Тут необходимо принимать на входе объект Item, в нем параметры длины пароля и "соли".
Answer это модель которая будет ответом(response_model), её в параметрах функции post не нужно указывать.
'''
@app.post('/postapi', response_model=Answer)
def post(item: Item):
    # Генерируем код, соль и хэш
    # В качестве параметров берем значения из объекта item, который наша функция принимает в качестве параметра
    code = generate_password(item.lenght_code)
    salt = hash_func(generate_password(item.lenght_salt))
    
    # Хэш из строки код + соль 
    hash = hash_func(code + salt)
    
    # Создаем объект класса Answer
    answer = Answer(code=code, salt=salt, hash=hash)

    # Возвращаем объект
    # FastAPI вернет его в виде JSON
    return answer


if __name__ == '__main__':
    uvicorn.run("api:app", port=8000, host="127.0.0.1", reload=True)