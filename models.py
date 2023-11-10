#!/usr/bin/env python
from config import env_vars
from mysql.connector import connect


class get_queries():

    def __init__(self):
        """Initialize a Database Connection.

            This method creates a connection to a MySQL database by using the provided
            environmental variables for the database host, user, password, and database name.
            It sets up the database connection pipeline for use in subsequent database operations.

        Returns:
            None
        """
        self._pipeline = connect(
            host=env_vars.db_host,
            user=env_vars.db_user,
            password=env_vars.db_password,
            database=env_vars.db_database
        )

    def average_genre_reviews(self):
        """Retrieve Average Genre Reviews for Visualization.

            This method sends a SQL query to the connected MySQL database to obtain the average review
            ratings for each genre. It calculates the average rating, counts the number of votes per genre,
            and orders the results by descending average rating. The retrieved data is returned as a list
            of tuples, making it suitable for visualizations, such as d3.js bar graphs.

        Returns:
            list of tuples: Each tuple contains a genre, its corresponding average review rating, and the
            number of votes for that genre.
        """
        query = """SELECT genre,
                          ROUND(avg(rating),2) as 'average genre review',
                          count(series.genre) as 'number of votes'
                                    FROM series
                                    INNER JOIN reviews ON  series.id = reviews.series_id
                                    GROUP BY genre
                                    ORDER BY avg(rating) desc"""
        try:
            query_results = self._pipeline.cursor()
            query_results.execute(query)
            data = query_results.fetchall()
            return data
        except Exception as e:
            print(f"An error occurred: {e}")

    def fully_joined_data(self):
        """Retrieve Fully Joined Data for Tabular.js Table.

            This method sends a SQL query to the connected MySQL database to retrieve fully joined data
            from different tables. It combines information from the 'reviewer', 'reviews,' and 'series'
            tables, fetching reviewer names, series titles, release dates, genres, and review ratings.
            The results are ordered by series title and returned as a list of tuples. This data is
            used to populate a tabular.js table for user-friendly presentation.

        Returns:
            list of tuples: Each tuple contains details about a fully joined record, including
            reviewer name, series title, release date, genre, and review rating.
        """
        query = """SELECT
                       CONCAT(viewer.f_name, ' ', viewer.l_name) AS full_name,
                       series.title,
                       series.release_date,
                       series.genre,
                       reviews.rating
                FROM reviewer AS viewer JOIN reviews
                ON viewer.id = reviews.reviewer_id JOIN series ON
                series.id = reviews.series_id ORDER BY series.title;
            """
        try:
            query_results = self._pipeline.cursor()
            query_results.execute(query)
            data = query_results.fetchall()
            return data
        except Exception as e:
            print(f"An error occured:{e}")
