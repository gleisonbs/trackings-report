import sqlite3
from sqlite3 import Error
import schema

class Database:
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

if __name__ == '__main__':
    print(schema.tables['actions'])
    db = Database()
    db.create_connection(r'BlipReports.db')
