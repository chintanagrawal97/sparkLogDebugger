import sqlite3
from sqlite3 import Error
from flaskblog.models import User

def select_all_users(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_post(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM post")
    rows = cur.fetchall()

    for row in rows:
        print(row)

def show_all_tables(conn):

    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type ='table' ")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
    
def delete_user(conn,id):

    cur = conn.cursor()
    cur.execute(f"DELETE FROM user WHERE id={id}")

def delete_post(conn,id):

    cur = conn.cursor()
    cur.execute(f"DELETE FROM post WHERE user_id={id}")


def main():
    database = r"/Users/achintan/Desktop/10-Password-Reset-Email/flaskblog/site.db"

    # create a database connection
    conn = create_connection(database)
    # with conn:
    #     print('Lets see all tables ')
    #     show_all_tables(conn)

    #     print("1. Query all users")
    #     select_all_users(conn)

    #     print('Delete form table')
    #     delete_user(conn,1)

    #     print("1. Query all remaining users")
    #     select_all_users(conn)

    #     print("Select all post")
    #     select_all_post(conn)
        
    #     print('Delete form table')
    #     delete_post(conn,1)

    #     print("Select all remianing post")
    #     select_all_post(conn)
        

# main()  

chintan = User.query.filter_by(username='achintan')
print(chintan)

