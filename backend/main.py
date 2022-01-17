from fastapi import FastAPI, Request, Depends
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
from models import Argonaute

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

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
async def get_argonautes(db: Session = Depends(get_db)):
    # query la DB pour la liste des argonautes et return le json
    db.query(Argonaute).all()
    return {"message": "Hello World"}


@app.get("/add_argonaute/{name}")
async def add_argonaute(name: str, db: Session = Depends(get_db)):

    if db.query(Argonaute.name).filter_by(name=name.lower()).first():
        return {"message": f"{name.lower()} already exists"}
    else:
        argonaute = Argonaute()
        argonaute.name = name.lower()
        db.add(argonaute)
        db.commit()
        return {"message": f"Created {argonaute.name}"}
