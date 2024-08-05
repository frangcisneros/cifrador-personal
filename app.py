from app import create_app, db
from flask import Flask
from app.routes.index import index
from app.models import Text, TextHistory, Role, User, UserData
import os
from app.services import roles


app = create_app()
app.secret_key = os.environ.get("SECRET_KEY")


# register the blueprint
app.register_blueprint(index)

with app.app_context():
    # Create tables
    db.create_all()
    # TODO: NO SE SI LAS ESTOY LLAMANDO CONSTANTEMENTE TENGO QUE BUSCAR LA FORMA DE LLAMARLAS UNA SOLA VEZ
    roles.create_admin_role()
    roles.create_user_role()
    roles.create_admin_user()


# https://flask.palletsprojects.com/en/3.0.x/appcontext/
app.app_context().push()

if __name__ == "__main__":

    """
    Server Startup
    Ref: https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.run
    Ref: Book Flask Web Development Page 9
    """
    app.run(host="0.0.0.0", port=5000)
