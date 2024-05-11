from app import create_app
from flask import Flask
from routes.index import index

app = create_app()


# register the blueprint
app.register_blueprint(index)

# https://flask.palletsprojects.com/en/3.0.x/appcontext/
app.app_context().push()

if __name__ == "__main__":
    """
    Server Startup
    Ref: https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.run
    Ref: Book Flask Web Development Page 9
    """
    app.run(host="0.0.0.0", port=5000)
