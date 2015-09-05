__author__ = 'Саша'

import sys
import sqlite3
import win32crypt
from pywin32_testutil import str2bytes # py3k-friendly helper

# LINK: http://www.ftium4.com/chrome-cookies-encrypted-value-python.html

outFile_path = r'chrome_cookies.txt';
sql_file     = r'C:\Users\Саша\AppData\Local\Google\Chrome\User Data\Default\Cookies';

sql_exe      = "SELECT host_key,name,value,encrypted_value FROM cookies WHERE host_key='.google.com' AND name='SSID'";
conn         = sqlite3.connect(sql_file)
for row in conn.execute(sql_exe):
    pwdHash = str(row[3])
    try:
        blob     = win32crypt.CryptProtectData(str2bytes("data"), "My", None, None, None, 0)
        got_data = win32crypt.CryptUnprotectData(pwdHash, None, None, None, 0)
        print(blob)
        #ret      = win32crypt.CryptUnprotectData(blob, None, None, None, 0)
        print (pwdHash)
    except:
        print ('Fail to decrypt chrome cookies')
        sys.exit(-1)
    #with open(outFile_path, 'a+') as outFile:
    #    outFile.write('host_key: {0:<20} name: {1:<20} value: {2} \n\n'.format(row[0].encode('gbk'), row[1].encode('gbk'), pwdHash.encode('gbk')) ) #,ret[1].encode('gbk')
conn.close()

print ('All Chrome cookies saved to:\n' + outFile_path)