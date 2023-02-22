from flask import Flask, render_template  # Import the Flask framework and render_template function
from flask_bootstrap import Bootstrap  # Import the Flask-Bootstrap extension

app = Flask(__name__)  # Create a new Flask web application
Bootstrap(app)  # Use the Flask-Bootstrap extension to initialize the application


@app.route('/')  # Define a route for the home page of the application
def index():
    return render_template('index.html', bootstrap=Bootstrap())
    # Render the HTML template 'index.html' and pass an instance of the Bootstrap class to the template context


if __name__ == '__main__':
    app.run(debug=True)  # Start the web application in debug mode if the script is run directly
