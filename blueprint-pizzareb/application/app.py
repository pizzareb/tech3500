from flask import Flask
# Import the Blueprint object from the homepage package
from application.bp.homepage import homepage

app = Flask(__name__)

# Register the Blueprint to the Flask app
# The url_prefix is optional, but for a homepage, we usually register it at the root.
app.register_blueprint(homepage)

if __name__ == '__main__':
    # This block is for running the app directly during development
    app.run(debug=True)
