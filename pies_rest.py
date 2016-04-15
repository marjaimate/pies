import sqlite3
from flask import g
from flask import Flask
from flask_restful import Resource, Api

DATABASE = 'pies.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app = Flask(__name__)
api = Api(app)

# Define the resources here
# ...

# Add resources
api.add_resource(PieList, '/pies')
api.add_resource(Pie, '/pies/<pie_id>')

if __name__ == '__main__':
    app.run(debug=True)
