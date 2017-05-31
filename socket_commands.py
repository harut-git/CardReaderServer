import re

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
                                                                                                               entry_id,
                                                                                                               name,
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


def listen_reader(params):
    read_file = open("current.txt", "r")
    read_id = read_file.read()
    read_id = re.sub('[a-z]', '', read_id)
    print read_id
    if not check_if_emp_exists(read_id):
        response = {'command': "add_employee",
                    'params': {
                        'entry_id': read_id
                    }}
        return response
    else:
        response = {'command': "employee_exists",
                    'params': {
                        'entry_id': read_id
                    }}
        return response
