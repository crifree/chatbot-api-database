from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa e registra la blueprint
    from app.routes.chatbot import chatbot
    app.register_blueprint(chatbot, url_prefix='/api')

    return app
