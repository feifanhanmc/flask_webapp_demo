#-*- coding: utf-8 -*-
import MySQLdb
from config import mysql_config


class MYDB():
    def __init__(self):
        self.conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=mysql_config['user'],
                passwd=mysql_config['pwd'],
                db=mysql_config['db'],
                charset='utf8')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self, sql):
        self.cursor.execute(sql)
        self.close()

    def select(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.close()
        return res

    def insert(self, table_name, data_headers, data):
        '''
        :param data_headers(list of data_name(str)) 、 data(list of list)
        for example:
            data_headers = ['username', 'pwd']
            data = [['hmc', '123'],
                    ['admin', 'admin'],
                    ['root', 'root']] 
        '''
        columc_num = len(data_headers)
        
        #拼接sqli语句
        sqli = 'INSERT INTO ' + table_name + '('
        datatype = '('
        for i in range(columc_num):
            if not i:
                sqli = sqli + data_headers[i]
                datatype += '%s'
            else:
                sqli = sqli + ', '  + data_headers[i]
                datatype += ', %s' 
        datatype += ')'
        sqli = sqli + ')' + ' VALUES ' + datatype
        
        #存储数据
        flag = True
        for d in data:
            t = []
            for i in range(columc_num):
                t.append(d[i])
            try:
                self.cursor.execute(sqli, tuple(t))
                self.conn.commit()
            except Exception,e :
                # print '存储失败，错误原因 :', e
                flag = False
                self.conn.rollback()
        if flag:
            if len(data):
                print '存储成功，共存储' + str(len(data)) + '条数据'
        self.close()
