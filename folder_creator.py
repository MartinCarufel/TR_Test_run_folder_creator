from tkinter import filedialog
import os
import requests
import json

class Folder_creator:
    def __init__(self, user, password):
        self.USER = user
        self.PASSWORD = password
        self.head = {"Content-Type": "application/json"}
        self.rjson = None
        self.parent_folder = ""
        self.subfolders = []

    def select_parent_folder(self):
        self.parent_folder = filedialog.askdirectory()

    def tr_section_http_request(self, project, section_id):
        URL = "https://testrail.dwos.com/index.php?/api/v2/get_cases/{}&section_id={}".format(project, section_id)
        self.rjson = requests.get(URL, headers=self.head, auth=(self.USER, self.PASSWORD)).json()

    def create_folder_list(self):
        for tc in self.rjson:
            self.subfolders.append("{} {}".format(str(tc["id"]), tc["title"][3:]))

    def create_subfolder(self, parent_folder):
        for subfolder in self.subfolders:
            os.mkdir(parent_folder + "/" + subfolder)

    def ask_for_input(self, message):
        # print(message, " : ", end="")
        return input(message + " : ")




creator = Folder_creator("martin.carufel@dental-wings.com", '18,Mac&Amo')
creator.select_parent_folder()
project = creator.ask_for_input("Entrer le no de project (IOS =2)")
section_id = creator.ask_for_input("Entrer le no de section")
creator.tr_section_http_request(project, section_id)
creator.create_folder_list()
creator.create_subfolder(creator.parent_folder)



