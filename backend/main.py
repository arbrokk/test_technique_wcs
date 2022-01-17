from fastapi import FastAPI, Depends
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
from models import Argonaute

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class ArgonautesRequest(BaseModel):
    name: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_argonautes_list")
async def get_argonautes():
    # query la DB pour la liste des argonautes et return le json

    return {"message": "Hello World"}


@app.get("/add_argonaute")
async def add_argonaute(argonaute_request: ArgonautesRequest, db: Session = Depends(get_db)):
    argonaute = Argonaute()
    argonaute.name = argonaute_request
    db.add(argonaute)
    db.commit()
    
    return {"message": f"Created {argonaute}"}
