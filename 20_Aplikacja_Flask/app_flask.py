# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tagname


def get_tags(session):
    return session.query(Tag).all()


def create_tag(name, session):
    try:
        tag = Tag(tagname=name)
        session.add(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True

def remove_tag(name, session):
    tag = session.query(Tag).filter_by(tagname=name).one()
    session.delete(tag)
    session.commit()

@app.route('/')
def hello():
    return render_template('app.html', data=get_tags(db.session),
                           tytul="Notatka", no_error=True)


@app.route('/add_tag')
def add():
    args = request.args
    no_error = create_tag(args["name"], db.session)
    if no_error:
        tytul = "Dodano notatkę"
    else:
        tytul = "Taka notatka już istnieje"

    return render_template('app.html', data=get_tags(db.session),
                           no_error=no_error,
                           tytul=tytul)


@app.route('/remove_tag')
def remove():
    args = request.args
    remove_tag(args["values"], db.session)
    no_error = True
    if no_error:
        tytul = "Usunieto notatkę"
    return render_template('app.html', data=get_tags(db.session),
                           no_error=no_error,
                           tytul=tytul)