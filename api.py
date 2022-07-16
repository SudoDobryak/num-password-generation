from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}


if __name__ == '__main__':
    uvicorn.run("api:app", port=8000, host="127.0.0.1", reload=True)