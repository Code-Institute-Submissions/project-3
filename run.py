import os
import copy
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

app_info = {
            "logged": False,
            # "username": "",
            # "allusers": "",
            # "register": "",         # ???
            "check_active": "",     # Pass class for check button
            "register_active": "",  # Pass class for register button
            "route": "index",            # Which is the current page
            "game": False           # Is there a current game active True/False

            }

"""
class Visitor(object):
    ''' This is the protoypte of a visitor (not logged in). '''

    visitor = 0

    def __init__(self):
        self.app_info = {
                    "logged": False,
                    # "username": "",
                    # "allusers": "",
                    # "register": "",         # ???
                    "check_active": "",     # Pass class for check button
                    "register_active": "",  # Pass class for register button
                    "route": "index",            # Which is the current page
                    "game": False           # Is there a current game active True/False
                    }
                    

        User.logged_users += 1  # Keep track of how many users are logged in

        def addLoggedUser(self):
            ''' Add a logged in user to the dictionary of logged in users. '''
            global loggedUsers
            loggedUsers[self.username] = self

        addLoggedUser(self)
"""

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
        self.app_info = {
                    "logged": is_logged,
                    # "username": "",
                    # "allusers": "",
                    # "register": "",         # ???
                    "check_active": "",     # Pass class for check button
                    "register_active": "",  # Pass class for register button
                    "route": "index",            # Which is the current page
                    "game": False           # Is there a current game active True/False
                    }

        User.logged_users += 1  # Keep track of how many users are logged in

        def addLoggedUser(self):
            ''' Add a logged in user to the dictionary of logged in users. '''
            global loggedUsers
            loggedUsers[self.username] = self

        addLoggedUser(self)

    #  Might add a method to remove the logged in user during log out

defaultUser = User("default", False, 0, [])

def read_from_file(file_name):
    store=""
    file = "data/" + file_name
    with open(file, "r") as readdata:
        store = readdata.read()
    return store

def createUser(name):
    # global loggedUsers
    tempUser = User(name, True, 0, [])
    vars()[name] = copy.deepcopy(tempUser)
    loggedUsers[name] = copy.deepcopy(tempUser)
    return vars()[name]


def add(x,y):           #This is a testing function -- Will be removed at that end.
    """Add Function - Testing purposes"""
    return x + y

@app.route('/', methods=['GET','POST'])
def index():
    # num1 = 100
    # num2 = 56
    # ans = add(num1, num2)
    # return "Description: It is working. Answer is {}".format(ans)

    allusers = json.loads(read_from_file("users.json"))

    
    global app_info
    
    global attempt      #Needed only for debugging
    try:
        if request.method == 'POST':
            pass
            '''
            app_info["allusers"] = read_from_file("users.txt")
            if 'register' in request.form:
                app_info["logged"] = False
                app_info["username"] = ""
                app_info["allusers"] = ""
                app_info["register"] = ""
                app_info["check_active"] = ""
                app_info["register_active"] = "btn-deactivated"
                app_info["route"] = "register"
                return redirect(url_for('register'))
                '''    
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"
    
    app_info["route"] = "index"

    message = ""

    # thisUser = defaultUser

    # return render_template("index.html", app_info=app_info, attempt=attempt)
    # return render_template("index.html", app_info=app_info, thisUser=thisUser)
    return render_template("index.html", app_info=app_info, thisUser="", message=message)


@app.route('/login', methods=['GET','POST'])
def login():
    global app_info
    # global loggedUsers
    # thisUser=""

    if request.method == 'POST':
        username = request.form['username']
        # app_info["allusers"] = read_from_file("users.txt")
        allusers = json.loads(read_from_file("users.json"))
        
        if username == "":
            allusers = ""
            message = "Please enter your username to log in."
            # return redirect(url_for('index', app_info=app_info, thisUser=defaultUser, message=message))
            return render_template('index.html', app_info=app_info, thisUser="", username="", message=message)
        elif username in allusers.keys():  #User already registered
            print("User {} is registered".format(username)) #Debug
            # Is user already logged in?
            if username in loggedUsers.keys():
                message = username + " is already logged in. Do you want to proceed? If you proceed the previous session will be destroyed."
                return render_template("proceed_login.html", app_info=app_info, thisUser="", username=username, message=message)
            else: # User is not logge in yet
                print("User {} is now loggedin.".format(username)) #Debug
                x = createUser(username)
                loggedUsers[username].total_points = allusers[username]['total_points']
                loggedUsers[username].games_played = allusers[username]['results']
                return render_template("index.html", app_info=app_info, thisUser=loggedUsers[username], username="", message="")
        else:
            return "User has never registered."



            # app_info["logged"] = True
            # session['logged_in'] = True
            # return redirect(url_for('user'))
        # else:
        #     app_info["username"] = "That username does not exist. Please register first."
        #     app_info["logged"] = False
        #     return redirect(url_for('index'))
    
    return "What has happened? login route is present."  #Should never reach here

@app.route('/proceed_login/<username>', methods=['GET', 'POST'])
def proceed_login(username):
    loggedUsers[username].session+=1
    return render_template("index.html", app_info=app_info, thisUser=loggedUsers[username], message="")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 8080)), debug=True)