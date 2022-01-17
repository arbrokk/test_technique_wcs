from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Argonaute(Base):
    __tablename__ = "argonautes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)