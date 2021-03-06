import hashlib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Answer(BaseModel):
    code: str
    salt: str
    hash: str


class Item(BaseModel):
    lenght_code: int
    lenght_salt: int


somedata = {'code': '1labels', 'salt': '1sequences', 'hash': 'fwefqsdx'}
for_hash = somedata.get('code')
hash_object = hashlib.sha1(for_hash.encode()).hexdigest()
somedata['hash'] = hash_object


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


@app.post('/postapi')
def post(answer=Answer):
    return answer


if __name__ == '__main__':
    uvicorn.run("api:app", port=8000, host="127.0.0.1", reload=True)