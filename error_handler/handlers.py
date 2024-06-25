from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        response = {
            "error": "Not Found",
            "message": "The requested resource was not found on the server.",
        }
        return jsonify(response), 404

    @app.errorhandler(500)
    def internal_error(error):
        response = {
            "error": "Internal Server Error",
            "message": "An internal server error occurred.",
        }
        return jsonify(response), 500

    # Puedes agregar más manejadores de errores aquí
