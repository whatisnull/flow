# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-4.
"""
import MySQLdb

def main():
    pass
    conn = MySQLdb.connect(host="192.168.1.110", port=3306, user="worker", passwd="1qaz#EDC", db="flow", charset='utf8',
                    use_unicode=True)

    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("show tables")
    print cursor.fetchall()

    for i in range(0,100):
        if i<10:
            k = '0%d'%i
        else:
            k = i
        print k
        sql = 'insert ignore into flow_dict (sign, fid, create_time) values(%s, %s, now());'
        cursor.execute(sql, [k, 0])

if __name__ == '__main__':
    main()