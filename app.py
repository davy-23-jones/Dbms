from flask import Flask, render_template, url_for 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# class Customer(db.model):
#     id = db.column(db.Integer, primary_key=True)
#     name = db.column(db.String(20), nullable=False)
#     username = db.column(db.String(20), nullable=False)
#     email = db.column(db.String(20), nubllable=False)
#     password = db.column(db.String(20), nullable=False)

#     def __repr__(self) -> str:
#         return f"Customer('{self.ussername}', '{self.email}')"
    
# class Movie(db.model):
#     ticket_no = db.column(db.Integer, nullable=False)
#     Director = db.column(db.String(20), nullable=False)
#     Cast = db.column(db.string(50), nullable=False)
#     Duration = db.column(db.Integer, nullable=False)
#     Rating = db.column(db.Integer, nullable=False)
#     Moviename = db.column(db.String(20), nullable=False)

#     def __repr__(self) -> str:
#         return f"Movie('{self.ticket_no}, {self.Cast}, {self.Director} {self.Duration}, {self.Moviename}, {self.Moviename}')"

# class Show(db.model):
#     StartTime = db.column(db.Integer, nullable=False)
#     EndTime = db.column(db.Integer, nullable=False)
#     Showid = db.column(db.Integer, nullable=False)
#     Language = db.column(db.String(10), nullable=False)

#     def __repr__(self) -> str:
#         return f"Show('{self.Showid}, {self.EndTime}, {self.StartTime}, {self.Language}')"

# class Booking(db.model):
#     BookingDate = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
#     ticket_no = db.column(db.Intger, nullable=False)
#     id = db.column(db.Integer, nullable=False)

#     def __repr__(self) -> str:
#         return f"Booking('{self.BookingDate}, {self.id}, {self.ticket_no}')"

# class Tickets(db.model):
#     Show_date = db.column(db.DateTime, nullable=False)
#     Price = db.column(db.Integer, nullable=False)
#     ticket_no = db.column(db.Integer, nullable=False)
#     id = db.column(db.Integer, nullable=False)
#     seat = db.column(db.Integer, nullable=False)

#     def __repr__(self) -> str:
#         return f"Tickets('{self.id}, {self.Price}, {self.seat}, {self.Show_date}, {self.ticket_no}')"




@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/booked")
def booked():
    return render_template("booked.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/moviegrid")
def moviegrid():
    return render_template("moviegrid.html")

@app.route("/movie1")
def movie1():
    return render_template("movie1.html")

@app.route("/movie2")
def movie2():
    return render_template("movie2.html")

@app.route("/movie3")
def movie3():
    return render_template("movie3.html")

@app.route("/movie4")
def movie4():
    return render_template("movie4.html")

@app.route("/movie5")
def movie5():
    return render_template("movie5.html")

@app.route("/movie6")
def movie6():
    return render_template("movie6.html")

@app.route("/movie7")
def movie7():
    return render_template("movie7.html")

@app.route("/movie8")
def movie8():
    return render_template("movie8.html")

@app.route("/movie9")
def movie9():
    return render_template("movie9.html")

@app.route("/movie10")
def movie10():
    return render_template("movie10.html")



if __name__ == "__main__":
    app.run(debug=True)
