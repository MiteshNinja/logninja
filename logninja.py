import click
import sqlite3
import datetime

TABLES = [ 'movies', ]

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
@click.option('--date', '-d', help="YYYY:MM:DD HH:mm:ss" , default=datetime.datetime.now())
@click.argument('title')
@click.argument('rating')
def addmovie(title, rating, date):
    conn, curs = connect_db()
    curs.execute('''INSERT INTO movies (title, date, rating) values (?,?,?)''', (title, date , rating))
    conn.commit()
    conn.close()

@click.command('display')
def display_table():
    ''' Display information from table '''
    conn, curs = connect_db()
    i = 1
    for table in TABLES:
        print(i, ": ", table)
        i = i+1
    table = TABLES[int(input())-1]
    curs.execute('''SELECT * FROM %s''' % table)
    rows = curs.fetchall()
    col_names = [cn[0] for cn in curs.description]
    click.echo(col_names)
    for r in rows:
        click.echo(r)
    conn.close()


logninja.add_command(initdb)
logninja.add_command(addmovie)
logninja.add_command(display_table)
