
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Visitor, Base

engine = create_engine('sqlite:///visitors.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

#make instances of Visitor and commit to the Visitor database
Mike = Visitor(full_name='Mike Pence', age=25, date_of_visit='2019/8/29', time_of_visit='12:40', comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit', visitor_assistant='Sean')
#add Visitor to the sesion
session.add(Mike)
#issue changes to the database and commit them
session.commit()
Alice = Visitor(full_name='Alice Pence', age=19, date_of_visit='2019/9/5', time_of_visit='12:58', comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit', visitor_assistant='Sean')
session.add(Alice)
session.commit()



#query all visitor objects
# session.query(Visitor).all()
# session.query(Visitor).first()

#update the entries in database
#first find entry by id
# visitor_to_edit = session.query(Visitor).filter_by(id=1).one()
# visitor_to_edit.full_name = "Mike Spence"
# session.add(visitor_to_edit)
# session.commit()

#delete the entries in database
# visitor_to_delete = session.query(Visitor).filter_by(id=2).one()
# session.delete(visitor_to_delete)
# session.commit()





