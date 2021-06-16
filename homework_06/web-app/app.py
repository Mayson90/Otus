from flask import Flask, render_template
from flask_migrate import Migrate, upgrade

from web_app.models import db
from web_app.views.users import users_app

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(users_app)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.cli.command("Create all tables using metadata.create_all")
def create_all_tables():
    print("Hello flask command")

    with app.app_context():
        upgrade()


if __name__ == '__main__':
    app.run(debug=True)
