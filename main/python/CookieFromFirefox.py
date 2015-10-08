__author__ = 'Саша'

import sqlite3
import win32crypt
import os

# URL: http://jecvay.com/2015/03/python-chrome-cookies.html
#
# SELECT host,name,value FROM moz_cookies WHERE value!=''
#
# D:\server\Python34>python.exe D:\server\www3\CookieRead\main\python\CookieFromFirefox.py
# [('PREF', 'ID=1111111111111111:TM=1437756741:LM=1437756741:V=1:S=3-Ambmug1B7JacIN'), ('PREF', 'ID=1111111111111111:FF=0:LD=ru:TM=1437789062:LM=1437789062:GM=1:V=1:S=F7fiQcQfJtP6f7rQ')]

def get_firefox_cookies():
    #os.system('copy "C:\\Users\\Саша\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies" D:\\server\\www3\\python-chrome-cookies.txt')
    #conn = sqlite3.connect("D:\\server\\www3\\python-chrome-cookies.txt")
    conn = sqlite3.connect(r'C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\wmune09s.default\cookies.sqlite')
    ret_list = []
    for row in conn.execute("SELECT host,name,path,value FROM moz_cookies WHERE host='.doc.pb.ua' AND name='PDOC-AUTH'"):
        ret_list.append((row[1], row[3]))
    conn.close()
    #os.system('del "D:\\server\\www3\\python-chrome-cookies.txt"')
    return ret_list

print(get_firefox_cookies());