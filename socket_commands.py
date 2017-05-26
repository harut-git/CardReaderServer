from DbConnect import db_conn


def check_if_emp_exists(read_id):
    con = db_conn()
    cur = con.cursor()
    cur.execute("SELECT * FROM employees WHERE entry_id = '%s'" % read_id)
    ver = cur.fetchall()
    con.close()
    if ver:
        return True
    else:
        return False




def add_employee(params):
    name = params['name']
    entry_id = params['entry_id']
    img_url = params['img_url']
    group = params['group']
    position = params['position']
    start_ts = params['start_ts']
    end_ts = params['end_ts']
    cur = db_conn()
    cur.execute("INSERT (%s, %s, %s, %s, %s, %s, %s) INTO ") % (
    name, entry_id, img_url, group, position, start_ts, end_ts)


def update_employee(params):
    name = params['name']
    entry_id = params['entry_id']
    img_url = params['img_url']
    group = params['group']
    position = params['position']
    start_ts = params['start_ts']
    end_ts = params['end_ts']
