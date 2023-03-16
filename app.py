import requests
from flask import Flask, request, render_template, redirect, url_for
from part_1_data_layer import load, Visitor, load_all

app = Flask(__name__)


@app.route("/")
@app.route("/visitors/")
def show_visitors():
    visitors = load_all()
    return visitors


# create a new book and save it locally
@app.route("/visitors/new/", methods=["GET", "POST", "PUT"])
def new_visitor():
    if request.method == "POST":
        new_visitor = Visitor(
            full_name=request.form["full_name"],
            age=request.form["age"],
            date_of_visit=request.form["date_of_visit"],
            time_of_visit=request.form["time_of_visit"],
            comments=request.form["comments"],
            visitor_assistant=request.form["visitor_assistant"],
            id=request.form["id"],
        )

        new_visitor.save()
        return redirect(url_for("show_visitors"))
    else:
        return render_template("new_visitor.html")


# edit a visitor
@app.route(
    "/visitors/edit/<int:visitor_id>/",
    methods=["POST", "GET"],
)
def edit_visitor(visitor_id):
    visitor_to_edit = load(visitor_id)
    if request.method == "POST":
        visitor_to_edit.full_name = (request.form["full_name"],)
        visitor_to_edit.age = (request.form["age"],)
        visitor_to_edit.date_of_visit = (request.form["date_of_visit"],)
        visitor_to_edit.time_of_visit = (request.form["time_of_visit"],)
        visitor_to_edit.comments = (request.form["comments"],)
        visitor_to_edit.visitor_assistant = (request.form["visitor_assistant"],)
        visitor_to_edit.visitor_id = (request.form["id"],)
        visitor_to_edit.save()
        return redirect(url_for("show_visitors"))
    else:
        return render_template("edit_visitor.html", visitor=visitor_to_edit)


# delete a visitor
@app.route("/visitors/delete/<int:visitor_id>/", methods=["GET", "POST"])
def delete_visitor(visitor_id):
    if request.method == "GET":
        delete()
    return redirect(url_for("show_visitors"))


@app.route("/visitors/delete_all/", methods=["GET", "POST"])
def delete_all():
    load_all()
    return show_visitors()


if __name__ == "__main__":
    app.run(debug=True)
