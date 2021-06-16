from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from web_app.models import db
from web_app.models import Users

users_app = Blueprint("users_app", __name__, url_prefix="/users")


@users_app.route("/", endpoint="list")
def list_users():
    users = Users.query.all()
    return render_template("users/index.html", users=users)


@users_app.route("/<int:user_id>/", endpoint="details")
def get_user(user_id):
    user = Users.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"Product #{user_id} doesn't exist.")
    # return jsonify(product_id=product_id, name=product_name)
    return render_template(
        "users/details.html",
        user=user,
    )


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def user_add():
    if request.method == "GET":
        return render_template("users/add.html")

    user_name = request.form.get("user-name")
    if not user_name:
        raise BadRequest("Field product-name is required!")

    user = Users(name=user_name)
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Could not save user with name {user_name!r}")

    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
