import mysql_bbs.bbs_dao

mysql_bbs.bbs_dao.create(('106', 'who', 'who contents', 'apple'))
mysql_bbs.bbs_dao.update(('where contents', '106'))
mysql_bbs.bbs_dao.read('106')
mysql_bbs.bbs_dao.all()
