from flask import Blueprint, render_template, request, redirect
from app.models.text import Text
from cryptography.fernet import Fernet
import hashlib
import base64

index = Blueprint("index", __name__)


@index.route("/")
def home():
    texts = Text.all()
    for text in texts:
        print(type(text.key))
    return render_template("index.html", texts=texts)


@index.route("/encrypt", methods=["POST"])
def encrypt():
    text = Text(content=request.form["content"])

    if request.form["key"]:
        key_form = request.form["key"]
        key_form = key_form.encode()
        key_form = base64.urlsafe_b64encode(key_form.ljust(32, b"\0"))
        text.encrypt_content(key_form)
    else:
        text.encrypt_content()
    text.save()

    return redirect("/")


@index.route("/decrypt", methods=["POST"])
def decrypt():
    text_id = int(request.form["text_id"])  # Convert text_id to an integer
    decrypt_key = request.form["decrypt_key"]
    decrypt_key = decrypt_key.encode()
    decrypt_key = base64.urlsafe_b64encode(decrypt_key.ljust(32, b"\0"))

    text = Text.find(text_id)
    if text:
        text.decrypt_content(decrypt_key)
        text.save()
        return redirect("/")
    else:
        return redirect("/")


@index.route("/encrypt-again", methods=["POST"])
def encrypt_again():
    text_id = int(request.form["text_id"])
    text = Text.find(text_id)
    if text:
        key = text.key
        text.encrypt_content(key)
        text.save()
        return redirect("/")
    else:
        return redirect("/")
