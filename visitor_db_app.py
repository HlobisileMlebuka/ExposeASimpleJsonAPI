import sys
from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Visitor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
engine = create_engine('sqlite:///visitors.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/visitors')
def show_visitors():
  visitors = session.query(Visitor).all()
  return render_template('visitor.html', visitors=visitors)

#create a new book and save it in the database
@app.route('/visitors/new/', methods=['GET', 'POST'])
def new_visitor():
  if request.method == 'POST':
    new_visitor = Visitor(full_name = request.form['full_name'], age = request.form['age'], date_of_visit = request.form['date_of_visit'], time_of_visit = request.form['time_of_visit'], comments = request.form['comments'], visitor_assistant = request.form['visitor_assistant'])
    session.add(new_visitor)
    session.commit()
    return redirect(url_for('show_visitors'))
  else:
    return render_template('new_visitor.html')

#edit a visitor
@app.route('/visitors/<int:visitor_id>/edit/', methods = ['GET', 'POST'])
def edit_visitor(visitor_id):
  visitor_to_edit = session.query(Visitor).filter_by(id=visitor_id).one()
  if request.method == 'POST':
    if request.form['full_name']:
      visitor_to_edit.full_name = request.form['full_name']
      return redirect(url_for('show_visitors'))
  else:
    return render_template('edit_visitor.html', visitor=visitor_to_edit)

#delete a visitor
@app.route('/visitors/<int:visitor_id>/delete/', methods = ['GET', 'POST'])
def delete_visitor(visitor_id):
  visitor_to_delete =  session.query(Visitor).filter_by(id=visitor_id).one()
  if request.method == 'POST':
    session.delete(visitor_to_delete)
    session.commit()
    return redirect(url_for('show_visitors', visitor_id=visitor_id))
  else:
    return render_template('delete_visitor.html', visitor = visitor_to_delete)


if __name__ == '__main__':
  app.run(debug=True)




