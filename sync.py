#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import lxml.html
import cookielib
import re
import platform
import ConfigParser
import os
import dev_forum_db
import datetime

ini_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'application.ini')
conf = ConfigParser.SafeConfigParser()
conf.read(ini_path)
email = conf.get('user', 'email')
password = conf.get('user', 'pass')

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dev_forum_db.sqlite')
dev_forum_db.connect(db_path)
dev_forum_db.clear_forum()

url = 'https://developer.tokyometroapp.jp/users/sign_in'
values = {'user[email]' : email,
          'user[password]' : password}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
cj = cookielib.CookieJar()
opener = urllib2.build_opener()
opener.add_handler(urllib2.HTTPCookieProcessor(cj))
conn = opener.open(req)
cont = conn.read()
dom = lxml.html.fromstring(cont.decode('utf-8'))
contents = dom.xpath('//div[@class="alert alert-success"]')

if len(contents) == 0:
  print ('Permission error.')
  exit()

baseUrl = 'https://developer.tokyometroapp.jp'

def dumpPage(url):
  """
  各トピックをダンプする
  ※複数ページにまたがるトピックは最初の１ページしかみていないので注意。
  """
  req = urllib2.Request(url)
  conn = opener.open(req)
  cont = conn.read()
  dom = lxml.html.fromstring(cont.decode('utf-8'))
  titles = dom.xpath('//h2')
  contents = dom.xpath('//div[@class="contents col-md-12"]')
  text = ''
  for c in contents:
    text += c.text_content()
  dev_forum_db.add_forum_page(url, titles[0].text_content(), text)

def readListPage(url):
  req = urllib2.Request(url)
  conn = opener.open(req)
  cont = conn.read()

  dom = lxml.html.fromstring(cont)
  links = dom.xpath('//div[@class="subject"]/a')

  for l in links:
    if 'href' in l.attrib:
      dumpPage(baseUrl + l.attrib['href']);
  
  next = dom.xpath('//a[@class="next_page"]')
  for n in next:
    if 'href' in n.attrib:
      return (n.attrib['href']);
  return None

nextPage = '/forum/forums/1'
while nextPage:
  nextPage = readListPage(baseUrl+nextPage)

d = datetime.datetime.today()
dev_forum_db.update_keydata('FORUM_CHECK_DATE', d.strftime("%Y-%m-%d %H:%M:%S"))
