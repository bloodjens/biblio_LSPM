import mysql.connector as mysql


def connect():
    return Database.conn


class Database:
    conn = mysql.connect(host="127.0.0.1", user="root", password="", database="bibliotheque_lspm")

