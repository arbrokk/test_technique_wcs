from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware

import json
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
from models import Argonaute

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello Wild Code School Tutor ;-)",
            "endpoints": "Check /docs pour avoir les endpoints"
            }


@app.get("/argonaute/list")
async def get_argonautes(db: Session = Depends(get_db)):
    # query la DB pour la liste des argonautes et le return le json
    query = db.query(Argonaute).all()
    dic = {}
    i = 0
    while i < len(query):
        dic[i] = {"name": query[i].name}
        i += 1

    return dic


@app.post("/argonaute/add")
async def add_argonaute(name: str, db: Session = Depends(get_db)):
    # vérifie que le nom ne se trouve pas en db (prévention doublons), sinon l'ajoute en db
    if db.query(Argonaute.name).filter_by(name=name.lower()).first():
        return {"message": f"{name.lower()} already exists"}
    else:
        argonaute = Argonaute()
        argonaute.name = name.lower()
        db.add(argonaute)
        db.commit()
        return {"message": f"Created {argonaute.name}"}


@app.post("/argonaute/del")
async def delete_argonaute(name: str, db: Session = Depends(get_db)):
    # vérifie que le nom se trouve  en db si oui le supprime
    query = db.query(Argonaute).filter_by(name=name.lower())
    if query.first():
        query.delete()
        db.commit()
        return {"message": f"Deleted {name}"}
    else:
        return {"message": f"{name.lower()} doesn't exist"}
