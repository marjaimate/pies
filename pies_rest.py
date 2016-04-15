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

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#
# DB query example usage:
#
# Query a list of results:
#
# for cat in query_db('select * from cats'):
#     print cat['name'], 'has the id', cat['id']
#
# Single result:
#
# cat = query_db('select * from cats where name = ?', [the_catname], one=True)
# if cat is None:
#     print 'No such cat'
# else:
#     print the_catname, 'has the id', cat['cat_id']


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
