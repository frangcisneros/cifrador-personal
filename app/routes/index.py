from flask import Blueprint, request, jsonify
from app.models import Text
from app.services import UserService, TextService, EncryptService
from app.repositories import TextRepository

index = Blueprint("index", __name__)

# TODO: Seprarar las rutas hacia resources y mapping, aca esta todo mezclado

username_saved = None
password_saved = None
user = None
user_data = None
user_services = UserService()


@index.route("/all_texts", methods=["GET"])
def all_texts():
    texts = TextRepository().all()
    return jsonify(texts)


@index.route("/get_text/<id>", methods=["GET"])
def get_text(id):
    text = TextRepository().find(id)
    return jsonify(text)


@index.route("/add_text", methods=["POST"])
def add_text():
    content = (
        request.json.get("content", "default_content")
        if request.json
        else "default_content"
    )
    language = (
        request.json["language"]
        if request.json and "language" in request.json
        else "default_language"
    )
    text = Text(content=content, language=language)
    TextRepository().save(text)
    return jsonify({"message": "Text added successfully"})


@index.route("/delete_text/<id>", methods=["DELETE"])
def delete_text(id):
    text_to_delete = TextRepository().find(id)
    TextRepository().delete(text_to_delete)
    return jsonify({"message": "Text deleted successfully"})


@index.route("/edit_text/<id>", methods=["PUT"])
def edit_text(id):
    text_to_edit = TextRepository().find(id)
    if (
        request.json is not None
        and isinstance(request.json, dict)
        and request.json.get("content")
    ):
        TextService().edit_content(text_to_edit, request.json["content"])
    elif request.json is None:
        return jsonify({"message": "Invalid request data. No JSON data provided"}), 400
    else:
        return (
            jsonify({"message": "Invalid request data. 'content' field is missing"}),
            400,
        )
    return jsonify({"message": "Text edited successfully"})


@index.route("/encrypt_text", methods=["POST"])
def encrypt_text():
    if request.json is not None and "text_id" in request.json and "key" in request.json:
        text_id = request.json["text_id"]
        text = TextRepository().find(text_id)
        EncryptService().encrypt_content(text, request.json["key"])
        return jsonify({"message": "Text encrypted successfully"})
    else:
        return jsonify({"message": "Invalid request data"}), 400


@index.route("/decrypt_text", methods=["POST"])
def decrypt_text():
    if request.json is not None and "text_id" in request.json and "key" in request.json:
        text_id = request.json["text_id"]
        text = TextRepository().find(text_id)
        EncryptService().decrypt_content(text, request.json["key"])
        return jsonify({"message": "Text decrypted successfully"})
    else:
        return jsonify({"message": "Invalid request data"}), 400
