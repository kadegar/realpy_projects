# db_create.py

from views import db
from models import FTasks
from datetime import date

db.create_all()

#db.session.add(FTasks("Learn Python",date(2014,6,3),10,1))
#db.session.add(FTasks("Finish this tutorial",date(2014,5,1),10,1))

db.session.commit()