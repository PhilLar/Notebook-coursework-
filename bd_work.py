import sqlite3

def create_bd(bd_name):
    conn = sqlite3.connect('notebook.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE {} (
    name text,
    sname text,
    num text,
    bdate text
    )""".format(bd_name))
    conn.commit()
    #c.close()

def delete_bd(bd_name):
    conn = sqlite3.connect('notebook.db')
    c = conn.cursor()
    c.execute("DROP TABLE {}".format(bd_name))
    conn.commit()

def bd_list():
    conn = sqlite3.connect('notebook.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master \
WHERE type='table'")
    l = c.fetchall()
    return l
    # for i in l:
    #     print(i[0])
