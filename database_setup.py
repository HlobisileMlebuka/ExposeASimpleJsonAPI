import sys

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

#create declaritive_base instance
Base = declarative_base()

class Visitor(Base):

    __tablename__ = 'visitor'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    date_of_visit = Column(String, nullable=False)
    time_of_visit = Column(String(250), nullable=False)     
    comments = Column(String(500), nullable=False)
    visitor_assistant = Column(String(250), nullable=False)

    # @property
    # def serialize(self):
    #     return {
    #         'id' = self.id
    #         "full_name" = self.full_name
    #         'date_of_visit' = self.date_of_visit
    #         'time_of_visit' = self.time_of_visit
    #         'comments' = self.comments
    #         'visitor_assistant'= self.visitor_assistant
    #     }

engine = create_engine('sqlite:///visitors.db')
Base.metadata.create_all(engine)

