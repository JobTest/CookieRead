1. Скачиваем и устанавливаем 'Python' версией 3.4.3 ( https://www.python.org/download/releases/3.4.0/ )
   Если версия будет ниже третей - тогда зашифрованые поля будут неправильно читаться...
   
2. Сюда-же поверх скачиваем и устанавливаем 'ActivePython' той же версии ( http://www.activestate.com/activepython )
   В этом пакете содержиться основной модуль 'win32' который требуется для библиотеки 'win32crypt', чтобы декодировать шифр...

Работоспособность этого модуля успешно была протестирована на Windows-системе
=============================================================================

3. Нам будут нужны 2-рабочих (постоянных) url-адресса чтобы открыть SQLite-файл с куками И SQL-запросы:
* [для Chrome в Windows](http://) `C:\Users\Саша\AppData\Local\Google\Chrome\User Data\Default\Cookies`

                         SELECT host_key,name,path,value,encrypted_value FROM cookies WHERE host_key='<...>' AND name='<...>'
                         
* [для FireFox в Windows](http://) `C:\Users\Саша\AppData\Roaming\Mozilla\Firefox\Profiles\cggg7az1.default\cookies.sqlite`

                          SELECT host,name,path,value FROM moz_cookies WHERE host='<...>' AND name='<...>'
                          
4. Запуск программы для выполнения выполняется из консоли:
* `D:\server\Python34>python.exe D:\server\www3\CookieRead\main\python\CookieFromChrome.py`
* `D:\server\Python34>python.exe D:\server\www3\CookieRead\main\python\CookieFromFirefox.py`

А в результате полученные данные (с кодом пользователя) можно сохранить в файл...


Начало работы
=============
* [doc.pb.ua](https://doc.pb.ua/)