from flask import Flask
from config.settings import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    from app.routes import main
    app.register_blueprint(main.bp)

    # Initialize Rate Limiter
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["1000 per day", "100 per hour"], # Global limit
        storage_uri="memory://" # Simple in-memory storage for Vercel (per instance)
    )

    return app
