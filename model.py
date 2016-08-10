import MySQLdb
import config

host = config.mysql['host']
user = config.mysql['user']
password = config.mysql['password']
database = config.mysql['database']


def query(sql):
    db = MySQLdb.connect(host, user, password, database, charset='utf8', port=3306)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except Exception, e:
        print e
    res = cursor.fetchall()
    db.close()
    return res


def execute(sql):
    db = MySQLdb.connect(host, user, password, database, charset='utf8', port=3306)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except Exception, e:
        db.rollback()
        print e
    db.close()
