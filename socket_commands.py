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
    img_url = params['img_url']
    entry_id = params['entry_id']
    name = params['name']
    sur_name = params['surname']
    position = params['position']
    group = params['group']
    start_ts = params['start_ts']
    end_ts = params['end_ts']
    comment = params['comment']
    con = db_conn()
    con.set_character_set('utf8')
    cur = con.cursor()
    cur.execute("INSERT INTO employees VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (img_url,
                                                                                                         entry_id, name,
                                                                                                         sur_name,
                                                                                                         position,
                                                                                                         group,
                                                                                                         start_ts,
                                                                                                         end_ts,
                                                                                                         comment))


def update_employee(params):
    name = params['name']
    entry_id = params['entry_id']
    img_url = params['img_url']
    group = params['group']
    position = params['position']
    start_ts = params['start_ts']
    end_ts = params['end_ts']
