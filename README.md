Jandgeo_Project
===============

Repository for Jandgeo Development

To developers
-------------

The programming language for the implementation of the project is mainly Python 2.7 (3.3 has huge changes which causes
some issues on Django and other libraries).

The local server program "client" is implemented with Django 1.6 web development framework.

The data gathering program "dataManager" is implemented with Python 2.7.

Instruction
-----------

1. Start Raspberry Pi by pluging in the power cord.
2. (optional) if the prompt asks for username and password, enter "pi" for username and "raspberry" for password (default).
3. go to home directory by typing "cd ~"
4. type "python ~/dataManager/dataManager.py&"
5. type "~/client/manage.py runserver [-ip] [-port]&" "[ ]" are optional, default is localserver 127.0.0.1:8000
6. type "java 'Jscore Polling Software.jar'&"

Now open your browser on a machine that shared the same network as the Raspberry Pi and visit localhost (127.0.0.1:8000),
the login page will show up, click login without username and password, the data UI will show up.
