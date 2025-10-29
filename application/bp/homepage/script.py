import flask

from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route('/')
def home():
    """Default route page (/) which renders homepage.html."""
    return render_template('homepage.html')

@homepage.route('/about')
def about():
    """About route page (/about) which renders about.html."""
    return render_template('about.html')