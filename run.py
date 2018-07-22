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

# app_info = {
#             "logged": False,
#             # "username": "",
#             # "allusers": "",
#             # "register": "",         # ???
#             "check_active": "",     # Pass class for check button
#             "register_active": "",  # Pass class for register button
#             "route": "index",            # Which is the current page
#             "game": False           # Is there a current game active True/False
#             }

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

    def __init__(self, username, is_logged, total_points, games_played, route="index"):
        self.username = username
        self.is_logged = is_logged
        self.total_points = total_points
        self.games_played = games_played
        self.number_of_games = 0
        self.points_best_game = 0
        self.date_best_game = "01/01/2000"
        self.game = ""
        self.points_this_game = 0   # Should this belong to User or Game
        self.session = 1
        self.current_route = ""
        self.app_info = {
                    "logged": is_logged,
                    # "username": "",
                    # "allusers": "",
                    # "register": "",         # ???
                    # "check_active": "",     # Pass class for check button
                    # "register_active": "",  # Pass class for register button
                    "route": route,            # Which is the current page
                    "game": False           # Is there a current game active True/False
                    }

        User.logged_users += 1  # Keep track of how many users are logged in

        def addLoggedUser(self):
            ''' Add a logged in user to the dictionary of logged in users. '''
            global loggedUsers
            loggedUsers[self.username] = self

        if self.username:
            addLoggedUser(self)

    #  Might add a method to remove the logged in user during log out

defaultUser = User("", False, 0, [], "index")

# login required decorator -- from a tutorial and adapted
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in first')
            return redirect(url_for("index"))
    return wrap

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

''' I WILL DEAL WITH THIS WHEN I CREATE THE GAME CLASS
def global_game_reset():
    global current_game
    global current_riddle
    global all_riddles
    global riddle_counter
    global attempt
    global points
    global gained_points
    global wrong_answers
    global answer

    current_game = []
    current_riddle = 0
    all_riddles = []
    riddle_counter = 0
    attempt = 1
    points = 10
    gained_points = 0
    wrong_answers =[]
    answer = ""
'''

''' DO I NEED THIS?
def logout_reset_app_info():
    # global app_info
    # app_info["logged"] = False
    # app_info["username"] = "You are now logged out"
    # app_info["allusers"] = ""
    # app_info["game"] = False
    # global_game_reset()
    pass
'''

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

    # print("request.method is: {}".format((request.method)))
    # global app_info
    
    # global attempt      #Needed only for debugging
    try:
        if request.method == 'POST':
            # return "You have Cancelled the login process."
            
            # app_info["allusers"] = read_from_file("users.txt")
            if 'register' in request.form:
                # thisUser = copy.deepcopy(defaultUser)
                # thisUser.app_info["route"] = "register"
                # app_info ={}
                # app_info["check_active"] = ""
                # app_info["register_active"] = "btn-deactivated"
                # print(app_info)

                # tempUser = User(name, True, 0, [])
                # vars()[name] = copy.deepcopy(tempUser)
                # loggedUsers[name] = copy.deepcopy(tempUser)
                # return vars()[name]



                # return "I am trying to register a new user."
                return redirect(url_for('register'))
                '''
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
    
    # app_info["route"] = "index"

    message = ""

    thisUser = defaultUser

    # return render_template("index.html", app_info=app_info, attempt=attempt)
    # return render_template("index.html", app_info=app_info, thisUser=thisUser)
    # return render_template("index.html", app_info=app_info, thisUser=thisUser, message=message)
    return render_template("index.html", thisUser=thisUser, message=message)


@app.route('/login', methods=['GET','POST'])
def login():
    # global app_info
    # global loggedUsers
    thisUser=""

    if request.method == 'POST':
        username = request.form['username']
        # app_info["allusers"] = read_from_file("users.txt")
        allusers = json.loads(read_from_file("users.json"))
        
        if username == "":
            allusers = ""
            message = "Please enter your username to log in."
            # return redirect(url_for('index', app_info=app_info, thisUser=defaultUser, message=message))
            # return render_template('index.html', app_info=app_info, thisUser="", username="", message=message)
            return render_template('index.html', thisUser=defaultUser, username="", message=message)
        elif username in allusers.keys():  #User already registered
            print("User {} is registered".format(username)) #Debug
            # Is user already logged in?
            if username in loggedUsers.keys():
                message = username + " is already logged in. Do you want to proceed? If you proceed the previous session will be destroyed."
                # return render_template("proceed_login.html", app_info=app_info, thisUser="", username=username, message=message)
                return render_template("proceed_login.html", thisUser=defaultUser, username=username, message=message)
            else: # User is not logged in yet
                print("User {} is now loggedin.".format(username)) #Debug
                x = createUser(username)
                loggedUsers[username].total_user_points = allusers[username]['total_user_points']
                loggedUsers[username].games_played = allusers[username]['games_played']
                loggedUsers[username].points_best_game = allusers[username]['points_best_game']
                loggedUsers[username].number_of_games = allusers[username]['number_of_games']
                loggedUsers[username].date_best_game = allusers[username]['date_best_game']
                session['logged_in'] = True
                # return render_template("index.html", app_info=app_info, thisUser=loggedUsers[username], username="", message="")
                return render_template("index.html", thisUser=loggedUsers[username], username="", message="")
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
    # return render_template("index.html", app_info=app_info, thisUser=loggedUsers[username], message="")
    return render_template("index.html", thisUser=loggedUsers[username], message="")

@app.route('/register', methods=['GET','POST'])
def register():
    # global app_info
    thisUser = copy.deepcopy(defaultUser)
    # thisUser.app_info["route"] = "register"
    app_info = {}
    app_info["check_active"] = ""
    app_info["register_active"] = "btn-deactivated btn-hide"
    attr=""
   
    if request.method == 'POST':
        
        username = request.form['username']
        allusers = json.loads(read_from_file("users.json"))
        
        # username = request.form['username']
        
        if 'check' in request.form:
            # app_info["username"] = request.form['username']
            # username = request.form['username']
            # allusers = read_from_file("users.txt")
            # allusers = json.loads(read_from_file("users.json"))

            # Check that username is not empty
            if username == "":
                app_info["register"] = ""
                # app_info["register_active"] = "btn-deactivated btn-hide"
                # app_info["check_active"] = ""
                username_feedback = "Please type in a username and check its availability."
            elif username in allusers:
                app_info["register"] = ""
                # app_info["register_active"] = "btn-deactivated btn-hide"
                # app_info["check_active"] = ""
                username_feedback = "Username already exist. Please try another one."
            else:
                app_info["register"] = "register"
                app_info["register_active"] = ""
                app_info["check_active"] = "btn-deactivated btn-hide"
                username_feedback = "Username available. Please click the register button."
                attr="required"
            return render_template("register.html",app_info=app_info, username_feedback=username_feedback, thisUser=thisUser, attr=attr)

        if 'register' in request.form:
            username = request.form['username']
            if username == "":
                app_info["register"] = ""
                # app_info["register_active"] = "btn-deactivated btn-hide"
                # app_info["check_active"] = ""
                username_feedback = "Please type in a username and check its availability."
                return render_template("register.html",app_info=app_info, username_feedback=username_feedback, thisUser=thisUser)
            elif username in allusers:
                app_info["register"] = ""
                # app_info["register_active"] = "btn-deactivated btn-hide"
                # app_info["check_active"] = ""
                username_feedback = "Username already exist. Please try another one."
                return render_template("register.html",app_info=app_info, username_feedback=username_feedback, thisUser=thisUser)
            else:
                allusers[username] = {"username": username, "games_played": [], "date_best_game": "", "number_of_games": 0, "points_best_game": 0, "total_user_points": 0}

                with open("data/users.json", "w") as outfile:
                    json.dump(allusers, outfile, sort_keys=True, indent=4)

                return "Will redirect to users template."


                #     addusernames.write(username + "\n")
                #     app_info["allusers"] += (app_info["username"])
                #     app_info["logged"] = True
                #     session['logged_in'] = True
                # return redirect(url_for('user'))

        
    # app_info["register"] = "register"
    # app_info["allusers"]=""
    username_feedback="Enter a valid username."
    return render_template("register.html", app_info=app_info, thisUser=thisUser)

    # return "I have reached the register route."


    '''
    app_info["register_active"] = "btn-deactivated btn-hide"
    if request.method == 'POST':
        app_info["username"] = request.form['username']
        app_info["allusers"] = read_from_file("users.txt")
        if 'check' in request.form:
            # Check that username is not empty
            if app_info["username"] == "":
                app_info["register"] = ""
                app_info["register_active"] = "btn-deactivated btn-hide"
                app_info["check_active"] = ""
                username_feedback = "Please type in a username."
            elif app_info["username"] in app_info["allusers"]:
                app_info["register"] = ""
                app_info["register_active"] = "btn-deactivated btn-hide"
                app_info["check_active"] = ""
                username_feedback = "username already exist try another one"
            else:
                app_info["register"] = "register"
                app_info["register_active"] = ""
                app_info["check_active"] = "btn-deactivated btn-hide"
                username_feedback = "Username available. Please click the register button."
            return render_template("register.html",app_info=app_info, username_feedback=username_feedback)
            
        if 'register' in request.form:
            if app_info["username"] == "":
                app_info["register"] = ""
                app_info["register_active"] = "btn-deactivated btn-hide"
                app_info["check_active"] = ""
                username_feedback = "Please type in a username and check its availability."
                return render_template("register.html",app_info=app_info, username_feedback=username_feedback)
            else:
                with open("data/users.txt", "a") as addusernames:
                    addusernames.write(app_info["username"] + "\n")
                    app_info["allusers"] += (app_info["username"])
                    app_info["logged"] = True
                    session['logged_in'] = True
                return redirect(url_for('user'))

    app_info["register"] = "register"
    app_info["allusers"]=""
    username_feedback="Enter a valid username."
    return render_template("register.html", app_info=app_info)
    '''

@app.route('/logout/<currentUser>/<sessionNo>', methods=['GET', 'POST'])
# @app.route('/logout/<currentUser>', methods=['GET', 'POST'])
@login_required
def logout(currentUser, sessionNo):
# def logout(currentUser):
    print("LOGOUT")
    print("currentUser: {}".format(currentUser))
    print("session: {}".format(sessionNo))
    # return "Reached the logout routing. {}".format(currentUser)
    if request.method == 'POST':    #RESET
    # #     logout_reset_app_info()

        try:
            thisUser = loggedUsers[currentUser]
        except Exception as e:
            return "This session has expired. {} has been logged out from somewhere else.".format(e)
        
        try:
            if int(sessionNo) == thisUser.session:
                # Store info in JSON
                # allusers = json.loads(read_from_file("users.json"))
                # playing_user = allusers[thisUser.username]
                ''' I do not think I need to save anything here as data is being saved at the end of each game. '''
                
                # Prepare to delete instances
                # IF GAME OBJECT EXIST DELETE, OTHERWISE DO NOTHING
                if game == "":
                    pass
                else:
                    del thisUser.game

                del thisUser
                del loggedUsers[currentUser]
                session.pop('logged_in', None)

                return redirect(url_for("index"))
            else:
                message = "This session has been disabled. You were logged out from somewhere else."
                # return redirect(url_for('index', thisUser=defaultUser, message=message))
                return render_template("index.html", thisUser=defaultUser, message=message)

        except Exception as e:
            message="Something wrong happened. Please login again."
            # return redirect(url_for('index', thisUser=defaultUser, message=message))
            return render_template("index.html", thisUser=defaultUser, message=message)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 8080)), debug=True)