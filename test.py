import folder_creator
import unittest


class Test_suite(unittest.TestCase):

    def setUp(self):
        self.creator = folder_creator.Folder_creator("martin.carufel@dental-wings.com", '18,Mac&Amo')

    def test_folder_selector(self):

        self.creator.select_parent_folder()
        print(self.creator.parent_folder)
        self.assertIsInstance(self.creator.parent_folder, str)


    def test_folder_creation(self):
        self.creator.create_subfolder(self.creator.select_parent_folder()   )
        print("folder created")

    def test_http_get(self):
        self.creator.tr_section_http_request(2, 11362)
        self.assertIsInstance(self.creator.rjson, list)
        print(self.creator.rjson)

    def test_create_folder_list(self):
        self.creator.tr_section_http_request(2, 11362)
        self.creator.create_folder_list()
        self.assertIsInstance(self.creator.subfolders, list)
        print(self.creator.subfolders)
