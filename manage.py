import os
from app import create_app,db
from app.models import User,Role
from flask_script import Shell,Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app('default') # create a default app which is development
manager = Manager(app) 		# create a manager instance 
migrate = Migrate(app,db)	# create a migrate instance

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()