from flask import Blueprint, request, jsonify
from app.models import Text
from app.services import UserService, TextService, EncryptService
from app.repositories import TextRepository

index = Blueprint("index", __name__)

username_saved = None
password_saved = None
user = None
user_data = None
user_services = UserService()


@index.route("/all_texts", methods=["GET"])
def all_texts():
    try:
        texts = TextRepository().all()
        return jsonify(texts)
    except Exception as e:
        return jsonify({"error": str(e)})


@index.route("/get_text/<id>", methods=["GET"])
def get_text(id):
    try:
        text = TextRepository().find(id)
        return jsonify(text)
    except Exception as e:
        return jsonify({"error": str(e)})


@index.route("/add_text", methods=["POST"])
def add_text():
    try:
        content = request.json["content"]
        language = request.json["language"]
        text = Text(content=content, language=language)
        TextRepository().save(text)
        return jsonify({"message": "Text added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@index.route("/delete_text/<id>", methods=["DELETE"])
def delete_text(id):
    try:
        text_to_delete = TextRepository().find(id)
        TextRepository().delete(text_to_delete)
        return jsonify({"message": "Text deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@index.route("/edit_text/<id>", methods=["PUT"])
def edit_text(id):
    try:
        text_to_edit = TextRepository().find(id)
        TextService().edit_content(text_to_edit, request.json["content"])
        return jsonify({"message": "Text edited successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@index.route("/encrypt_text", methods=["POST"])
def encrypt_text():
    try:
        text_id = request.json["text_id"]
        text = TextRepository().find(text_id)
        EncryptService().encrypt_content(text, request.json["key"])
        return jsonify({"message": "Text encrypted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@index.route("/decrypt_text", methods=["POST"])
def decrypt_text():
    try:
        text_id = request.json["text_id"]
        text = TextRepository().find(text_id)
        EncryptService().decrypt_content(text, request.json["key"])
        return jsonify({"message": "Text decrypted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------------------------------------------------------------------- #
#                rutas descartadas pero guardadas por las dudas                #
# ---------------------------------------------------------------------------- #

# @index.route("/")
# def init():
#     if username_saved != None and password_saved != None:
#         return redirect("/home")
#     else:
#         return render_template("init.html")


# @index.route("/register", methods=["POST"])
# def register():
#     firstname = request.form["firstname"]
#     lastname = request.form["lastname"]
#     phone = request.form["phone"]
#     address = request.form["address"]
#     city = request.form["city"]
#     country = request.form["country"]
#     user_data = UserData()
#     user_data.firstname = firstname
#     user_data.lastname = lastname
#     user_data.phone = phone
#     user_data.address = address
#     user_data.city = city
#     user_data.country = country
#     user = User(user_data)
#     user.email = request.form["email"]
#     user.username = request.form["new_username"]
#     user.password = request.form["new_password"]
#     try:
#         user_services.save(user)
#     except:
#         error = "User or email already exists"
#         flash(error)
#     return redirect("/")


# @index.route("/login", methods=["POST"])
# def login():
#     username = request.form["username"]
#     password = request.form["password"]
#     global user
#     global user_data
#     list_user = user_services.check_auth(username, password)
#     # list_user = User.find_by(username=username, password=password)
#     if list_user:
#         user = user_services.find_by_username(username)
#         user_data = UserData.query.filter_by(user_id=user.id).first()
#         if type(request.form.get("remember")) == str:
#             global username_saved
#             global password_saved
#             username_saved = username
#             password_saved = password
#         return redirect("/home")
#     else:
#         error = "Invalid credentials"
#         flash(error)
#         return redirect("/")


# @index.route("/admin")
# def admin():
#     return render_template("admin.html")


# @index.route("/encrypt", methods=["POST"])
# def encrypt():
#     text = Text(content=request.form["content"])
#     global user
#     print(user)

#     if user is not None:
#         text.user_id = user.id

#     if request.form["key"]:
#         key_form = request.form["key"]
#         key_form = key_form.encode()
#         key_form = base64.urlsafe_b64encode(key_form.ljust(32, b"\0"))
#         text.encrypt_content(key_form)
#     else:
#         text.encrypt_content()
#     text.save()

#     return redirect("/home")


# @index.route("/home")
# def home():
#     global user
#     if user is not None:
#         texts = Text.find_by(user_id=user.id)
#     if texts is None:
#         texts = []
#     else:
#         for text in texts:
#             print(type(text.key))
#     return render_template("index.html", texts=texts, user=user)


# @index.route("/decrypt", methods=["POST"])
# def decrypt():
#     text_id = int(request.form["text_id"])  # Convert text_id to an integer
#     decrypt_key = request.form["decrypt_key"]
#     decrypt_key = decrypt_key.encode()
#     decrypt_key = base64.urlsafe_b64encode(decrypt_key.ljust(32, b"\0"))

#     text = Text.find(text_id)
#     if text:
#         try:
#             text.decrypt_content(decrypt_key)
#             text.save()
#         except:
#             error = "Invalid key"
#             flash(error)
#         return redirect("/home")
#     else:
#         return redirect("/home")


# @index.route("/delete", methods=["POST"])
# def delete():
#     text_id = int(request.form["text_id"])
#     text = Text.find(text_id)
#     if text:
#         text.delete()
#         return redirect("/home")
#     else:
#         return redirect("/home")


# @index.route("/edit", methods=["POST"])
# def edit():
#     text_id = int(request.form["text_id"])
#     text = Text.find(text_id)
#     new_content = request.form["new_content"]
#     text.content = new_content
#     text.length = len(new_content)
#     text.save()
#     return redirect("/home")


# @index.route("/encrypt-again", methods=["POST"])
# def encrypt_again():
#     text_id = int(request.form["text_id"])
#     text = Text.find(text_id)
#     if text:
#         key = text.key
#         text.encrypt_content(key)
#         text.save()
#         return redirect("/home")
#     else:
#         return redirect("/home")


# @index.route("/logout")
# def logout():
#     global username_saved
#     global password_saved
#     global user
#     global user_data
#     username_saved = None
#     password_saved = None
#     user = None
#     user_data = None
#     return redirect("/")


# @index.route("/user_panel", methods=["GET", "POST"])
# def user_panel():
#     all_users = UserRepository().all()
#     return jsonify(all_users)


# @index.route("/profile")
# def profile():
#     global user
#     global user_data
#     print(user_data)
#     return render_template("profile.html", user=user, user_data=user_data)
