import unittest
import os

from views import app, db
from models import User
from config import basedir

TEST_DB='test.db'

class Users(unittest.TestCase):
	def setUp(self):
		app.config['TESTING']=True
		app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+\
			os.path.join(basedir,TEST_DB)
		self.app=app.test_client()
		db.create_all()

	def tearDown(self):
		db.drop_all()		

	def test_users_can_register(self):
		new_user=User("sgadkaree","sgadkaree@yahoo.com","sgadkaree")
		db.session.add(new_user)
		db.session.commit()
		test=db.session.query(User).all()
		for t in test:
			t.name
		assert t.name=="sgadkaree"


if __name__=='__main__':
	unittest.main()