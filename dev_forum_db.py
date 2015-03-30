# -*- coding: utf-8 -*-
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

#import logging
#logger = logging.getLogger('peewee')
#logger.setLevel(logging.DEBUG)
#logger.addHandler(logging.StreamHandler())

database_proxy = Proxy()  # Create a proxy for our db.

class KeyDataTable(Model):
    key = TextField(primary_key=True)
    data = TextField()

    class Meta:
        database = database_proxy

class ForumTable(Model):
    """
    """
    page = TextField(primary_key=True)
    title = TextField()
    contents = TextField()

    class Meta:
        database = database_proxy

def connect(path):
    """
    データベースへの接続
    @param path sqliteのパス
    """
    db = SqliteExtDatabase(path)
    database_proxy.initialize(db)
    database_proxy.create_tables([KeyDataTable, ForumTable], True)


def update_keydata(key, data):
    try:
        keydata = KeyDataTable.get(
            (KeyDataTable.key == key)
        )
        keydata.data = data
        keydata.save()
    except KeyDataTable.DoesNotExist:
        KeyDataTable.create(key=key, data=data)


def get_keydata(key):
    try:
        keydata = KeyDataTable.get(
            (KeyDataTable.key == key)
        )
        return keydata.data
    except KeyDataTable.DoesNotExist:
        return None


def clear_forum():
    ForumTable.delete().execute()

def add_forum_page(page, title, contents):
    ForumTable.create(page = page, title = title, contents = contents)

def serach_forum(term):
    term = '%' + term + '%'
    query = ForumTable.select().where(ForumTable.contents ** term)
    ret = []
    for row in query:
        ret.append({'url' : row.page, 'title' : row.title})
    return ret
