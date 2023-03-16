import json
import glob
import os, re
import itertools
import sys

MY_PATH = os.environ.get("VISITOR_APP_PATH")
visitor_files = glob.glob(f"{MY_PATH}/*.json")


class Visitor:
    def __init__(
        self,
        full_name,
        age,
        date_of_visit,
        time_of_visit,
        comments,
        visitor_assistant,
        id=None,
    ):

        self.id = id
        self.full_name = full_name
        self.age = age
        self.date_of_visit = date_of_visit
        self.time_of_visit = time_of_visit
        self.comments = comments
        self.visitor_assistant = visitor_assistant

    def generate_id(self):

        """generate an id, relative to the last recorded id"""
        visitor_id_list = []
        files_in_directory = os.listdir(MY_PATH)
        for file_name in files_in_directory:
            if re.findall(r"((?<=visitor_)\d(?=\.json))", file_name):
                pattern = re.findall(r"((?<=visitor_)\d(?=\.json))", file_name)
                visitor_id_list.append(pattern)
        # flatten visitor_id_list
        visitor_id = list(itertools.chain.from_iterable(visitor_id_list))
        last_recorded_id = max(visitor_id, key=lambda x: int(x))
        id = int(last_recorded_id) + 1

        return id

    def save(self):

        """ "generates an id for the visitor, if there is none, then dumps the visitor as a json file"""

        self.id = self.id or self.generate_id()

        visitor_dictionary = {
            "full_name": self.full_name,
            "age": self.age,
            "date_of_visit": self.date_of_visit,
            "time_of_visit": self.time_of_visit,
            "comments": self.comments,
            "visitor_assistant": self.visitor_assistant,
            "id": self.id,
        }

        with open(f"{MY_PATH}/visitor_{self.id}.json", "w+") as dumped_data_file:
            json.dump(visitor_dictionary, dumped_data_file)

    def delete(self, id):
        try:
            visitor_file = f"{MY_PATH}/visitor_{id}.json"
            os.remove(visitor_file)
            print(f"File {visitor_file} deleted successfully.")
        except FileNotFoundError:
            print(f"File {visitor_file} not found or already deleted")


def delete_all():
    for file in visitor_files:
        os.remove(file)


def load(visitor_id):
    """loads file using id and returns an instance of visitor"""
    visitor_file = f"{MY_PATH}/visitor_{visitor_id}.json"
    with open(visitor_file, "r") as loaded_data_file:
        visitor_details = json.load(loaded_data_file)

    return Visitor(**visitor_details)


def load_all():
    visitor_files = glob.glob(f"{MY_PATH}/*.json")
    visitors = []
    for visitor in visitor_files:
        with open(visitor, "r") as f:
            visitor_obj = json.load(f)
            visitors.append(visitor_obj)
    visitor_array = json.dumps(visitors, indent=4)
    return visitor_array
