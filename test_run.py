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
        print("\n===============================\nsetUpClass - TestFlaskRoutes\n===============================\n")

    @classmethod
    def tearDownClass(cls):
        print("\n===============================\ntearDownClass - TestFlaskRoutes\n===============================\n")

    def test_index(self):
        """ Test routing for HOME page """
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_index route -- PASS")



     # Test Page Contents
    def test_index_page_loads(self):
        """ Test HOME page loads correctly"""
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b"Description" in response.data)
        print("test_index_page_loads route -- PASS")




class TestOtherFunctions(unittest.TestCase):
    '''
    Test suite for run.py
    Testing other Functions
    '''
    def test_add(self):
        '''
        test a testing add method to check that set up is ok
        '''
        answer = run.add(10, 3)
        self.assertEqual(answer, 13, "Failed")
        self.assertEqual(run.add(10, 3), 13, "Failed: add positive to positive")
        self.assertEqual(run.add(0, 3), 3, "Failed: add 0 to positive")
        self.assertEqual(run.add(0, -5), -5, "Failed: add 0 to negative")
        self.assertEqual(run.add(-7, -5), -12, "Failed: add negative to negative")
        self.assertEqual(run.add(7, -5), 2, "Failed: add positive to negative, positive answer")
        self.assertEqual(run.add(7, -9), -2, "Failed: add positive to negative, negative answer")
        self.assertEqual(run.add(0, 0), 0, "Failed: add 0 to 0")
        print("test_add -- PASS")


    def test_read_from_file(self):
            # Try to create a file

            # Try to Read from file

            # Try to delete File

            # Assert




            empty = {
                "user":"test_user",
                # "user":"user1",
                "number_of_games":5,
                "date_best_game":"",    # Currently has fixed date 1/4/2018
                "points_best_game":29,
                "total_user_points":50,
                "games_played":[]}      # Currently has fixed date 1/4/2018
            run.gained_points = 30
            run.user_data = empty
            run.store_game_info()

if __name__ == "__main__":
    unittest.main()