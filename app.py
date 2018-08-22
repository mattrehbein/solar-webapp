from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solar.db'
db = SQLAlchemy(app)

# MODEL
class Solar(db.Model):
  __tablename__ = 'comm_solar_table'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)

# ROUTES
@app.route("/")
def hello():
  return "This will be a cool site about solar gardens."

@app.route("/solar-gardens/")
def list():
  gardens = Solar.query.all()
  return render_template("list.html", gardens=gardens)

@app.route("/solar-gardens/<index>/")
def show(index):
  garden = Solar.query.filter_by(index=index).first()
  return render_template("show.html", garden=garden)

if __name__ == '__main__':
  app.run(debug=True)

