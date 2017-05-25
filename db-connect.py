import MySQLdb as mdb


def db_conn():
    con = mdb.connect('166.62.28.93', 'ghubo', '12365479', 'ghubas')

    cur = con.cursor()
    cur.execute("SELECT * FROM " 'dashboard_userid')
    ver = cur.fetchone()
    print ver[2]


db_conn()