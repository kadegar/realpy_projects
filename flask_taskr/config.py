#config.py

import os
basedir=os.path.abspath(os.path.dirname(__file__))

DATABASE='flasktaskr.db'
USERNAME='admin'
PASSWORD='admin'
CSRF_ENABLED=True
SECRET_KEY='secrets_secrets_dont_make_friends'

DATABASE_PATH=os.path.join(basedir,DATABASE)