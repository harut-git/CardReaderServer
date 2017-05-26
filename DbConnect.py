import MySQLdb as mdb


def db_conn():
    con = mdb.connect('166.62.28.93', 'ghubo', '12365479', 'ghubas')
    return con
