from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database.db import db, migrate
from app.routes.article_routes import article_bp

# KALAU INGIN MIGRATION, UNCOMMENT BARIS DI BAWAH INI
# from app.models.post_model import PostModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(article_bp)

    @app.route('/')
    def health():
        return {"message": "running"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
