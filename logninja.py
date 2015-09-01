import click
import sqlite3
import datetime

@click.group()
def logninja():
    pass

def connect_db():
    ''' Connects to temp.db and returns its cursor '''
    conn = sqlite3.connect('temp.db', detect_types=sqlite3.PARSE_DECLTYPES)
    curs = conn.cursor()
    return conn, curs

@click.command()
def initdb():
    conn, curs = connect_db()
    curs.execute('''CREATE TABLE movies(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT NOT NULL, 
                    date DATETIME,
                    rating INTEGER
                    )''')
    conn.commit()
    conn.close()


@click.command('add')
@click.argument('title')
@click.argument('rating')
def addmovie(title, rating):
    conn, curs = connect_db()
    curs.execute('''INSERT INTO movies (title, date, rating) values (?,?,?)''', (title, datetime.datetime.now(), rating))
    conn.commit()
    conn.close()

logninja.add_command(initdb)
logninja.add_command(addmovie)

