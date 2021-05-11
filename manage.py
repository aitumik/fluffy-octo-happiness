import os
from app import create_app,db
from app.models import User,Product,Post
from flask_script import Shell,Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Product=Product,Post=Post)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def make_fixtures():
    from app.fake import posts,users
    users(count=20)
    posts()

if __name__ == "__main__":
    manager.run()