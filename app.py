#!/usr/bin/env python
import os
from flask import Flask, render_template
from threading import Thread
from models import get_queries
from services.data_service import tidy_data

# configure the url path where flask can serve static files
app = Flask(__name__, static_url_path='/static')


# Register the blueprint
#app.register_blueprint(views, url_prefix='/views')

# app secret key
app.secret_key = os.getenv('APP_SECRET')


# Start the Flask development server
@app.route('/')
def index():
    """
        landing page
    """
    return "hello"


@app.route("/bar_graph")
def bar_graph():
    """Display a Bar Graph Visualization Using D3.js.

    This route renders a web page displaying a bar graph visualization, typically used to represent
    data in a graphical format. The bar graph is created and enhanced with D3.js, a powerful JavaScript
    library for data visualization.

    Returns:
        HTML: An HTML page containing the bar graph visualization created with D3.js.

    """
    return render_template("bar_graph.html")


@app.route("/tabular")
def tabular():
    """Display Tabular Data Using Tabulator.js.

        This route renders a web page displaying tabular data in a structured table format. Tabulator.js is used
        to enhance the table's functionality and appearance. The HTML template for the tabular data is rendered and
        displayed to the user.

    Returns:
        HTML: An HTML page containing the tabular data enhanced with Tabulator.js.
    """
    return render_template("tabular.html")


@app.route('/home')
def home():
    """Display the Main App Page in the Flask Application.

    This route serves as the main page of the Flask application. It initializes a connection
    to the database, retrieves data, and uses multithreading to perform data processing tasks concurrently.
    The route then renders the 'index.html' template to provide the main user interface.

    Returns:
        HTML: An HTML page representing the main app page of the Flask application.
    """

    temp = get_queries()
    query = temp.average_genre_reviews()
    table = temp.fully_joined_data()

    tidy_data_instance = tidy_data(query, table)

    tidy_data_thread = Thread(target=tidy_data_instance.clean_data)
    tidy_data_thread.start()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
