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


# app_info = {
            # "logged": False,
            # # "username": "",
            # # "allusers": "",
            # # "register": "",         # ???
            # "check_active": "",     # Pass class for check button
            # "register_active": "",  # Pass class for register button
            # "route": "index",            # Which is the current page
            # "game": False           # Is there a current game active True/False
            # }

"""
# I do not think I need this
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

allRiddles = json.loads(read_from_file("riddles.json"))
# print(allRiddles)

# Generate list of all riddles available

class User(object):
    ''' This is the prototype of a logged user. There will be an instance
        for each logged user. '''

    logged_users = 0

    def __init__(self, username, is_logged, total_points, games_played, route="index"):
        self.username = username
        self.is_logged = is_logged
        self.total_user_points = total_points
        self.games_played = games_played
        self.number_of_games = 0
        self.points_best_game = 0
        self.date_best_game = "01/01/2000"
        self.game_on = False           # Is there a current game active True/False
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
                    "route": route #,            # Which is the current page
                    # "game": False           # Is there a current game active True/False NEED TO BE ACCESSED BEFORE.
                    }

        User.logged_users += 1  # Keep track of how many users are logged in

        def addLoggedUser(self):
            ''' Add a logged in user to the dictionary of logged in users. '''
            global loggedUsers
            loggedUsers[self.username] = self

        if self.username:
            addLoggedUser(self)

    #  Might add a method to remove the logged in user during log out

class Game(object):
    ''' This is the prototype of a game. When an instance is created it will be owned
        by a logged in user. If the user logs out or the game finishes the game instance
        will be destroyed. '''
    
    def __init__(self):
        self.game = False              # Is it game on? Needed for logic in game function.
        self.riddles_sequence = []
        self.current_riddle_index = 0  # Are these doing the same thing?
        self.riddle_counter = 0        # Are these doing the same thing?
        self.current_game = []         # List of images selected
        self.current_riddle = 0
        self.attempt = 1
        self.points = 10
        self.most_recent_answer = ""
        self.wrong_answers = []


        def generate_riddle_sequence(self):
            global allRiddles
            for x in range(0, 10): #To select 10 random riddles
                repeat = True
                while repeat:
                    choose_game = random.choice(allRiddles)
                    if choose_game not in self.riddles_sequence:
                        repeat = False
                # Build a list of lists already sorted the way I want it
                item = []
                item.append(choose_game['id'])
                item.append(choose_game['source'])
                item.append(choose_game['answer'])
                # self.riddles_sequence.append(choose_game['source'])
                self.riddles_sequence.append(item)
            # for item in self.riddles_sequence:
            #     print(item)

        generate_riddle_sequence(self)

""" NOT NEEDED I CREATE THE GAME SORTED FROM THE START.
    def sort_current_riddle(self, data):
        ''' Sort the data so that it is always in the order:
            id, source, answer. '''
        self.current_game = [0, 0, 0]
        for currentRiddle in data: # Select a riddle
            if currentRiddle[0] == "id":
                self.current_game[0] = currentRiddle[1]
            elif currentRiddle[0] == "source":
                self.current_game[1] = currentRiddle[1]
            elif currentRiddle[0] == "answer":
                self.current_game[2] = ''.join(list(currentRiddle[1]))  
        """



# Create a game from class to test it
# x = Game()        
                

defaultUser = User("default", False, 0, [], "index")



''' Experiment for code to be used in Game Class
def generate_riddle_sequence():
    global allRiddles
    selected_games = []
    print("\n==============\nSelection of 10 games\n================\n")
    for x in range(0, 10): #To select 10 random riddles
        repeat = True
        while repeat:
            choose_game = random.choice(allRiddles)
            if choose_game not in selected_games:
                repeat = False
        print(choose_game['id'])
        selected_games.append(choose_game['source'])
    print(selected_games)

generate_riddle_sequence()
'''




def createUser(name):
    # global loggedUsers
    tempUser = User(name, True, 0, [])
    vars()[name] = copy.deepcopy(tempUser)
    loggedUsers[name] = copy.deepcopy(tempUser)
    return vars()[name]

''' I WILL DEAL WITH THIS WHEN I CREATE THE GAME CLASS
    I do not need this as when an instance is created it will
    be created with default values and a new selection of 
    10 random riddles.
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

def fill_best_individual_games():
    # global best_individual_games
    store = json.loads(read_from_file("hof_individual.json"))["best_individual_games"]
    # return ast.literal_eval(store) # Turn string to dictionary
    return store

    # store=""
    # with open("data/hof_individual.json", "r") as readdata:
    #     store = readdata.read()  # Read as a string
    # store = ast.literal_eval(store) # Turn string to dictionary
    # best_individual_games = store["best_individual_games"]

def fill_best_all_games():
    store = json.loads(read_from_file("hof_all_games.json"))["best_all_games"]
    return store


    # global best_all_games
    # store=""
    # with open("data/hof_all_games.json", "r") as readdata:
    #     store = readdata.read()  # Read as a string
    # store = ast.literal_eval(store) # Turn string to dictionary
    # best_all_games = store["best_all_games"]

def add(x,y):           #This is a testing function -- Will be removed at that end.
    """Add Function - Testing purposes"""
    return x + y

# @app.route('/', defaults={'thisUser': defaultUser}, methods=['GET','POST'])
@app.route('/<currentUser>', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def index(currentUser=defaultUser.username):
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

    # thisUser = defaultUser
    thisUser=loggedUsers[currentUser]
    thisUser.app_info['route'] = "index"

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
    print("LOGOUT")
    print("currentUser: {}".format(currentUser))
    print("session: {}".format(sessionNo))
    # return "Reached the logout routing. {}".format(currentUser)
    if request.method == 'POST':    #RESET
    # #     logout_reset_app_info()
        print("Reached POST of logout.")

        try:
            thisUser = loggedUsers[currentUser]
            print("Load thisUser.")
        except Exception as e:
            return "This session has expired. {} has been logged out from somewhere else.".format(e)
        
        try:
            if int(sessionNo) == thisUser.session:
                print("Session is OK")
                # Store info in JSON
                # allusers = json.loads(read_from_file("users.json"))
                # playing_user = allusers[thisUser.username]
                ''' I do not think I need to save anything here as data is being saved at the end of each game. '''
                
                # Prepare to delete instances
                # IF GAME OBJECT EXIST DELETE, OTHERWISE DO NOTHING
                if thisUser.game == "":
                    pass
                else:
                    # del thisUser.game
                    thisUser.game = ""
                    print("delete game.")

                del thisUser
                print("delete thisUser")
                del loggedUsers[currentUser]
                print("delete loggedUsers[currentUser]")
                print(loggedUsers)
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

@app.route('/user/<currentUser>', methods=['GET', 'POST'])
@app.route('/user', methods=['GET', 'POST'])
@login_required
def user(currentUser=defaultUser.username):
    thisUser=loggedUsers[currentUser]
    thisUser.app_info['route'] = "user"
    # global app_info
    # global user_data
    # global current_game
    # global current_riddle
    # global all_riddles
    # global riddle_counter
    # global gained_points
    # global attempt      #Needed only for debugging
    
    # user_data_json = json.loads(read_from_file("user_game_data_json.json"), object_hook=json_tuple_helper_function)
    
    # user_data = find_loggedin_user(user_data_json)
    
    # if app_info["game"] == False:  # RESET
    #     current_game = []
    #     current_riddle = 0
    #     all_riddles = []
    #     riddle_counter = 0
        
    # fill_best_individual_games()
    # fill_best_all_games()
        
    # app_info["route"] = "user"
    # return render_template("user.html", app_info=app_info, user_data=user_data, attempt=attempt, gained_points=gained_points)
    return render_template("user.html", thisUser=thisUser)
    return "Reached User page."


@app.route('/halloffame/<currentUser>')
@app.route('/halloffame')
def halloffame(currentUser=defaultUser.username):
    # global app_info
    # global best_individual_games
    # global best_all_games
    thisUser=loggedUsers[currentUser]
    thisUser.app_info['route'] = "halloffame"
    #I will return the following here
    best_individual_games = fill_best_individual_games()
    best_all_games = fill_best_all_games()
    # best_all_games = ""
    
    # app_info["route"] = "halloffame"
    return render_template("halloffame.html", thisUser=thisUser, best_individual_games=best_individual_games, best_all_games=best_all_games)

@app.route('/about/<currentUser>')
@app.route('/about')
# @app.route('/about', defaults={'thisUser': defaultUser})
def about(currentUser=defaultUser.username):
    
    thisUser=loggedUsers[currentUser]
    thisUser.app_info['route'] = "about"

    return render_template("about.html", thisUser=thisUser)

@app.route('/contact/<currentUser>')
@app.route('/contact')
def contact(currentUser=defaultUser.username):
    # global app_info
    # app_info["route"] = "contact"
    thisUser=loggedUsers[currentUser]
    thisUser.app_info['route'] = "contact"
    return render_template("contact.html", thisUser=thisUser)


@app.route('/game/<currentUser>', methods=['GET', 'POST'])
@app.route('/game', methods=['GET', 'POST'])
@login_required
def game(currentUser=defaultUser.username):
    # global app_info
    # global all_riddles
    # global current_game
    # global current_riddle
    # global riddle_counter
    # global attempt
    # global points
    # global gained_points
    # global wrong_answers
    # global answer
    
    thisUser=loggedUsers[currentUser]
    thisUser.app_info['route'] = "game"  # I will need this to control the menu
    # app_info["route"] = "game"  # I will need this to control the menu
    
    # if app_info["game"] == False:
    #     app_info["game"] = True  # Game On
    #     all_riddles = json.loads(read_from_file("riddles.json"))
    if thisUser.game_on == False:
        print("Is game active? {}.".format(thisUser.game_on))
        thisUser.game_on = True  # Game On
        print("Game turned on.")
        print("Is game active? {}.".format(thisUser.game_on))
        # all_riddles = json.loads(read_from_file("riddles.json"))
        
        # for x in range(0, 10):  # Select 10 images at random
        #     repeat = True
        #     while repeat:
        #         choose_game=random.choice(all_riddles)
        #         if choose_game.items() not in current_game:
        #             repeat = False
        #     current_game.append(choose_game.items())
        

        # CREATE A GAME
        thisUser.game = Game()

        # current_riddle = sort_current_riddle(current_game[riddle_counter])
            
    # if request.method == 'POST':
    #     if 'play' in request.form:
    #         points = 10
    #         attempt = 1

        # elif 'answer_btn' in request.form:
                                # Check Answer
            # if attempt == 1:
            #     answer = request.form['answer_text']
                
                                    # Clean the answer
                                    # If there are multiple spaces or other white characters in between the words
                # temp =[]                    # Clean answer
                # temp = answer.split()
                # answer=""
                # for item in temp:
                #     answer += item + " "
                    
                # answer = answer.strip()         # Strip trailing spaces
                
                # if answer.lower() == current_riddle[2].lower(): # answer correct
                #     gained_points += 10
                #     wrong_answers = []
                #     attemp = 1                  # First attempt of
                #     riddle_counter += 1         # Next Riddle
                #     if riddle_counter > len(current_game)-1:    # If that was last riddle then
                                            # store_game_info()
                        # return redirect(url_for('game_over'))   # GAME OVER
                                        # Trigger next riddle
                    # current_riddle = sort_current_riddle(current_game[riddle_counter]) 
            
                # else:                           # Otherwise answer is wrong
                #     if len(answer) == 0:        #if no answer is given
                #         wrong_answers.append("-")
                #     else:
                #         wrong_answers.append(answer)
                #     attempt = 2                 # This is your next attempt
                #     points = 6                  # Set correct number of points

            # elif attempt == 2:
                
                                    # Get all words and concatenate them
                # answer = ""
                # index = ""
                # local_answer = current_riddle[2].split()
                # for ndx, each_word in enumerate(local_answer):
                #     index = 'answer_text' + str(ndx+1)
                #     answer += (request.form[index].strip() + " ") #Strip any typed white spaces
                    
                # temp =[]                        # Clean answer
                # temp = answer.split()
                # answer=""
                # for item in temp:
                #     answer += item + " "
                # answer = answer.strip()         # Strip trailing spaces
                
                # if answer.lower() == current_riddle[2].lower(): # Answer correct
                #     gained_points += 6          # Gain points
                #     attempt = 1                 # Reset attempt
                #     points = 10
                #     wrong_answers = []

                    # riddle_counter += 1
                    # if riddle_counter > len(current_game)-1:
                                                # store_game_info()
                        # return redirect(url_for('game_over'))

                    # current_riddle = sort_current_riddle(current_game[riddle_counter])
                
                # else:                           # Otherwise answer is wrong
                                        # wrong_answers.append(answer)
                    # if len(answer) == 0:                #if no answer is given
                    #     wrong_answers.append("-")
                    # else:
                    #     wrong_answers.append(answer)
                    # attempt = 3                 # This is your next attempt
                    # points = 2                  # Set correct number of points
                
            # elif attempt == 3:
            #     answer = ""
            #     index = ""
            #     local_answer = current_riddle[2].split()
                
                # for ndx, each_word in enumerate(local_answer):
                #     index = 'answer_text' + str(ndx+1)
                #     answer += (request.form[index].strip() + " ") #Strip any typed white spaces
                    
                                    # answer = answer[0:-1]      # Strip final space
                # temp =[]                    # Clean answer
                # temp = answer.split()
                # answer=""
                # for item in temp:
                #     answer += item + " "
                # answer = answer.strip()         # Strip trailing spaces
                
                # if answer.lower() == current_riddle[2].lower():  # Answer correct
                #     gained_points += 2           # Gain points
                #     attempt = 1                  # Reset attempt
                #     points = 10
                #     wrong_answers = []           # Reset wrong answers

                    # riddle_counter += 1
                    # if riddle_counter > len(current_game)-1:
                                                # store_game_info()
                        # return redirect(url_for('game_over'))

                    # current_riddle = sort_current_riddle(current_game[riddle_counter])
                
                                    # Otherwise answer is wrong
                # else:
                #     attempt = 1                 # This is your next attempt
                #     points = 10                 # Set correct number of points
                #     wrong_answers = []           # Reset wrong answers
                #     riddle_counter += 1
                #     if riddle_counter > len(current_game)-1:
                                            # store_game_info()
                    #     return redirect(url_for('game_over'))
                    # current_riddle = sort_current_riddle(current_game[riddle_counter])

                                #This will happen if pass
                                # increase attempt
        # elif 'pass_btn' in request.form:
        #     if attempt == 1:
        #         wrong_answers = []
        #         wrong_answers = ["-"]
        #         attempt = 2
        #         points = 6
        #     elif attempt == 2:
        #         points = 2
        #         wrong_answers.append("-")
        #         attempt = 3
        #     elif attempt == 3:
        #         if riddle_counter > len(current_game)-1:
                                    # store_game_info()
    #                 return redirect(url_for('game_over'))
    #             current_riddle = sort_current_riddle(current_game[riddle_counter])
    #             points = 10
    #             attempt = 1
    #             riddle_counter += 1
    #             wrong_answers = []
                
    #             if riddle_counter > len(current_game)-1:     # Call next riddle
    #                 return redirect(url_for('game_over'))
    #             current_riddle = sort_current_riddle(current_game[riddle_counter])
                
    # return render_template("game.html", app_info=app_info, all_riddles=all_riddles, current_game=current_game, current_riddle=current_riddle, riddle_counter=riddle_counter+1, attempt=attempt, points=points, gained_points=gained_points, wrong_answers=wrong_answers)
    # return "This is the page for the game for user: {}".format(thisUser.username)
    return render_template("game.html", thisUser=thisUser, all_riddles="", current_game="", current_riddle="", riddle_counter=1, attempt=1, points=0, gained_points=0, wrong_answers="")


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 8080)), debug=True)