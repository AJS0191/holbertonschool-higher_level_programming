#!/usr/bin/python3
"""module containing that State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inherited from class BASE"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String(128), nullable = False)
