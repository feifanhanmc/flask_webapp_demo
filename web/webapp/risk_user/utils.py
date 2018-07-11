#-*- coding:utf-8 -*-
from webapp.database import MYDB

def utils_create_table(sql):
    sql = '''CREATE TABLE IF NOT EXISTS risk_user(
                       url VARCHAR(200) NOT NULL,
                       username VARCHAR(40) NOT NULL,
                       count int NOT NULL,
                       starttime TIMESTAMP NOT NULL,
                       endtime TIMESTAMP NOT NULL,
                       PRIMARY KEY ( url, username )
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    db = MYDB()
    try:
        db.create_table(sql)
        return True
    except Exception,e:
        print e
    return False

def utils_show_urls():
    sql = '''select distinct url from risk_user'''
    db = MYDB()
    try:
        return db.select(sql)
    except Exception,e:
        print e
    return False

def utils_show_risk_user(url):
    sql = "select username,count,starttime,endtime from risk_user where url = %s order by count desc" % (url)
    db = MYDB()
    try:
        res = [[r[0], r[1], str(r[2]), str(r[3])] for r in db.select(sql)]
        return res
    except Exception,e:
        print e
    return False

def utils_upload_file():
    return False