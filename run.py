import os
import json
import ast
import random
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps  #decorators for requires login

app = Flask(__name__)
"""For this project I do not need high security.
For better security the secret_key should be completely random to make it very difficult to guess.
Ideally use a random key generator.
The key should be placed in a separate configuration file which would then be imported. 
I do not consider security to be an issue for this particular project considering the purpose.
"""

app.secret_key = "Not a secure key"  # Needed for sessions to work properly
loggedUsers = {}
allRiddles = []

class User(object):
    ''' This is the prototype of a logged user. There will be an instance
        for each logged user. '''

    logged_users = 0

    def __init__(self, username, is_logged, total_points, games_played):
        self.username = username
        self.is_logged = is_logged
        self.total_points = total_points
        self.games_played = games_played
        self.game = ""
        self.points_this_game = 0   # Should this belong to User or Game
        self.session = 1
        self.current_route = ""

        User.logged_user += 1  # Keep track of how many users are logged in

        def addLoggedUser(self):
            ''' Add a logged in user to the dictionary of logged in users. '''
            global loggedUsers
            loggedUsers[self.username] = self

        addLoggedUser(self)

    #  Might add a method to remove the logged in user during log out


    





def add(x,y):           #This is a testing function -- Will be removed at that end.
    """Add Function"""
    return x + y

@app.route('/', methods=['GET','POST'])
def index():
    # num1 = 100
    # num2 = 56
    # ans = add(num1, num2)
    # return "Description: It is working. Answer is {}".format(ans)

    # return render_template("index.html", app_info=app_info, attempt=attempt)
    return render_template("index.html", app_info="")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 8080)), debug=True)