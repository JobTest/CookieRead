__author__ = 'Саша'

import sqlite3
import win32crypt
import os

# URL: http://jecvay.com/2015/03/python-chrome-cookies.html
#
# SELECT host_key,name,value,encrypted_value FROM cookies WHERE value!='' OR encrypted_value!=''
#
# D:\server\Python34>python.exe D:\server\www3\CookieRead\main\python\CookieFromChrome.py
# {'SSID': 'AogltHd17CxQQ13k4'}

def get_chrome_cookies():
    #os.system('copy "C:\\Users\\Саша\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies" D:\\server\\www3\\python-chrome-cookies.txt')
    #conn = sqlite3.connect("D:\\server\\www3\\python-chrome-cookies.txt")
    conn = sqlite3.connect(r'C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\Cookies')
    ret_list = []
    ret_dict = {}
    for row in conn.execute("SELECT host_key,name,path,value,encrypted_value FROM cookies WHERE host_key='.doc.pb.ua' AND name='PDOC-AUTH'"):
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_list.append((row[1], ret[1]))
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    #os.system('del "D:\\server\\www3\\python-chrome-cookies.txt"')
    return ret_dict

print(get_chrome_cookies());