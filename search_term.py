#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import platform
import os
import dev_forum_db

if len(sys.argv) != 2:
  print ('python search_term.py serch-word')
  exit()

if platform.system() == 'Windows':
    search_term = sys.argv[1].decode('cp932')
else:
    search_term = sys.argv[1]

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dev_forum_db.sqlite')
dev_forum_db.connect(db_path)
ret = dev_forum_db.serach_forum(search_term)
for r in ret:
    print r['url'], r['title']
