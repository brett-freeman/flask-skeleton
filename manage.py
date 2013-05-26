from app import application as app
from flask.ext.script import Manager
from flask.ext.alembic import ManageMigrations

manager = Manager(app)
manager.add_command("migrate", ManageMigrations())

if __name__ == "__main__":
    manager.run()