#!/usr/bin/python3
"""This module connects to SQLalchemy and contains class State."""

from sqlalchemy import (create_engine, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
