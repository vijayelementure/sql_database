
import random
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    texts= 0


app = FastAPI()


@app.post("/sendingdata")
def send_data(text: Item):
    print(text.texts)
    return {"status": 200}