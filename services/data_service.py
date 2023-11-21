#!/usr/bin/env python
import json
import logging
import os


class DataCleaningError(Exception):
    pass


class tidy_data():

    def __init__(self, query, tabular):
        self.clean_up_query = query
        self.tabular = tabular
        self.query = None
        self.struct_data = None

    def clean_data(self):
        """_summary_:

        """
        try:
            self.structure_query_results()
            self.convert_query_to_json(query=self.query, name='reviews.json')

            self.convert_to_tabular()
            self.convert_query_to_json(query=self.struct_data, name="tabular.json")

        except Exception as e:
            logging.error(f"An error has in data service file:{e} ")

    def structure_query_results(self):
        """_summary_: Helper function
                the function will be used to structure the data in a json format
                that will be suitable for d3
        """
        json_list = []
        for i in self.clean_up_query:

            dict_to_json = dict()
            dict_to_json['genera'] = i[0]
            dict_to_json['rating'] = str(i[1])
            dict_to_json['votes'] = i[2]
            json_list.append(dict_to_json)
        self.query = json_list

    def convert_to_tabular(self):

        json_list = []
        for i in self.tabular:
            dict_to_json = dict()
            dict_to_json['reviewer'] = i[0]
            dict_to_json['title'] = i[1]
            dict_to_json['release date'] = i[2]
            dict_to_json['genre'] = i[3]
            dict_to_json['rating'] = str(i[4])
            json_list.append(dict_to_json)
        self.struct_data = json_list

    def convert_query_to_json(self, query, name):
        """_summary_:
            the function will accept a list of dictionaries the will be
            returned from structured query results function
        Args:
            query (list): list of dictionaries
        """
        try:
            path = os.path.join(os.getcwd(), 'static')
            with open(os.path.join(path, name), 'w') as fp:
                json.dump(query, fp=fp, indent=2)
        except Exception as e:
            logging.error(f"An error occurred during JSON conversion:{e}")
            raise DataCleaningError("Error occurred during JSON conversion")
