#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
.. module:: database
    :platform: Unix
    :synopsis: the module that contains the database schema of Dragonfire.

.. moduleauthor:: Mehmet Mert Yıldıran <mert.yildiran@bil.omu.edu.tr>
"""

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func


Base = declarative_base()


class User(Base):
    """Schema of `users` table.
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    gender = Column(Boolean, nullable=False)
    birth_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Fact(Base):
    """Schema of `facts` table.
    """

    __tablename__ = 'facts'
    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    verbtense = Column(String(255), nullable=False)
    clause = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'), default=0)
    user = relationship(User)
    counter = Column(Integer, default=1)


class Notification(Base):
    """Schema of `notifications` table.
    """

    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    title = Column(String(63), nullable=False)
    message = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    capitalize = Column(Boolean, default=False)


# Create an engine that stores data in the local directory's dragonfire.db file.
engine = create_engine('sqlite:///dragonfire.db')

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)
