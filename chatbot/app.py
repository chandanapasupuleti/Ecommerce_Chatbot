from flask import Flask
from routes import root

# Create a Flask app instance
app = Flask(__name__)
app.register_blueprint(root)
# The app is already initialized when we import routes.py
if __name__ == "__main__":
    # Run the Flask app in debug mode for development
    app.config["PROPAGATE_EXCEPTIONS"] = True  # Propagate errors to the browser for debugging
    app.run(debug=True)