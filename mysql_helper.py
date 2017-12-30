import MySQLdb

from mtime.settings import DATABASE

class mysql_connection_wrapper(object):
    def __init__(self, db_args=None):
        if db_args is None:
            db_args = DATABASE
        self.connect = MySQLdb.connect(user=db_args['user'],
                                       passwd=db_args['password'],
                                       db=db_args['db'],
                                       charset='utf8')
        self.cursor = self.connect.cursor()

    def insert_row(self, info_list):
        sql_pat = 'insert star_info value({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'
        sql = sql_pat.format(*tuple(info_list))
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print 'Saved information of {}'.format(info_list[0])
        except MySQLdb.Error as e:
            self.connect.rollback()
            print '{} while saving information of {}'.format(repr(e), info_list[0])

    def close_connect(self):
        self.connect.close()
