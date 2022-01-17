from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

# défini le model de la db Sqlite, avec 2 colonnes : id primary, et nom de l'argonaute

class Argonaute(Base):
    __tablename__ = "argonautes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)