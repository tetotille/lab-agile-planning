from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Counter(BaseModel):
    value: int = 0

counter = Counter()

@app.post("/increment")
def increment(amount: int = 1):
    counter.value += amount
    return {"counter": counter.value}

@app.get("/counter")
def get_counter():
    return {"counter": counter.value}
