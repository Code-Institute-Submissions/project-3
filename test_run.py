# import os
# import json
# import datetime
import unittest
import run              # The code that we are testing
from run import app   #, app_info, global_game_reset, current_game
# from flask import Flask, url_for, session

class TestFlaskRoutes(unittest.TestCase):
    '''
    Test suite for run.py
    Testing the Flask routing
    '''

    @classmethod
    def setUpClass(cls): #Create a file at the start of this group of tests
        print("\nsetUpClass - TestFlaskRoutes")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass - TestFlaskRoutes")

    def test_index(self):
        """ Test routing for HOME page """
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_index route -- PASS")



if __name__ == "__main__":
    unittest.main()