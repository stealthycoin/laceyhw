####################################
### Kaleidoscope Powered elena makefile
####################################
SHELL := /bin/bash

#launches the test server address 127.0.0.1:8000
test:
	source /Users/tiny/Code/laceyhw/venv/bin/activate;\
	python /Users/tiny/Code/laceyhw/venv/elena/manage.py runserver

#destroys whole project. Probably don't want to use this unless starting over.
nuke:
	rm -rf dictionary.py dictionary.pyc /Users/tiny/Code/laceyhw/venv req.pip makefile .git *~
