#!/usr/bin/env python
import os


class env_vars():
    """Environment Variables Configuration for MySQL Database.

        The `env_vars` class is responsible for configuring environment variables used in connecting
        to a MySQL database. It retrieves and stores essential parameters for database connection,
        including the host, user, password, and database name. These variables are crucial for
        establishing a connection to the MySQL database and setting up the SQLAlchemy database URI.
    """

    # Use os.getenv to retrieve environment variables
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_database = os.getenv('DB_DATABASE')

    env_vars = os.getenv

    # Establish the database connection
    SQLALCHEMY_DATABASE_URI = f"""mysql://{env_vars('DB_USER')}:{env_vars('DB_PASSWORD')}@{env_vars('DB_HOST')}/{env_vars('DB_DATABASE')}"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
