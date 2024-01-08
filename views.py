from threading import Thread
from models import get_queries
from services.data_service import tidy_data
from flask import Blueprint, render_template, jsonify, send_from_directory


views = Blueprint(__name__, 'views')


# Start the Flask development server
@views.route('/')
def index():
    """
        landing page
    """
    return render_template('home.html')


@views.route('/tabular.json')
def serve_query(filename):
    """
        function will be used to create a route to the
        static folder to enable the serving of json file
    """
    return send_from_directory('static', filename)


@views.route("/graph")
def bar_graph():
    """Display a Bar Graph Visualization Using D3.js.

    This route renders a web page displaying a bar graph visualization, typically used to represent
    data in a graphical format. The bar graph is created and enhanced with D3.js, a powerful JavaScript
    library for data visualization.

    Returns:
        HTML: An HTML page containing the bar graph visualization created with D3.js.

    """
    return render_template("bar_graph.html")


@views.route("/tabular")
def tabular():
    """Display Tabular Data Using Tabulator.js.

        This route renders a web page displaying tabular data in a structured table format. Tabulator.js is used
        to enhance the table's functionality and appearance. The HTML template for the tabular data is rendered and
        displayed to the user.

    Returns:
        HTML: An HTML page containing the tabular data enhanced with Tabulator.js.
    """
    return render_template("tabular.html")


@views.route("/temp")
def temp():
    """"
    End point will be used in conjuction with react js on the front end
    """
    
    tp = get_queries()
    query = tp.average_genre_reviews()
    table = tp.fully_joined_data()
    return jsonify(tidy_data(query, table).structure_query_results())


@views.route('/reviews')
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