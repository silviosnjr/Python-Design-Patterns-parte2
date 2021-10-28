# -*- coding: utf-8 -*-
import MySQLdb

class Connection_factory(object):

    def get_connection(self):
        return MySQLdb.connect(host="db4free.net",
            user='edutech_alunos',
            passwd='Python_2021',
            db='edutech_python')