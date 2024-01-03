from model import question_anwser, summary_pipline
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class TextIn(BaseModel):
    question: str
    context: str

class AritcleIn(BaseModel):
    ARTICLE: str

@app.get("/")
def read_root():
    return {"Hello": "Claris"}
 
@app.post("/answer")
def answer(payload: TextIn):
    return question_anwser(payload.question, payload.context)

@app.post("/summary")
def summary(payload: AritcleIn):
    return summary_pipline(payload.ARTICLE)
