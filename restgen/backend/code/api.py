import flask
from flask_restless import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
CORS(app)


class Mapa(db.Model):
    coordenada = db.Column(db.Unicode)
    nombre = db.Column(db.Unicode)
    id = db.Column(db.Integer,primary_key=True)
    



# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Mapa, methods=['GET', 'POST', 'DELETE','PUT'])


# start the flask loop
if __name__ == '__main__':
  app.run(host='0.0.0.0',threaded=True)