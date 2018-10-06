import os
import copy
import json
import random
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps  #decorators for requires login
from flask_mail import Mail, Message

app = Flask(__name__)
    # Use the following to run LOCALLY will need the import
# app.config.from_pyfile('config.cfg')

    # Use the following to run from HEROKU - remove the import
app.config["MAIL_SERVER"] = os.getenv('MAIL_SERVER')
app.config["MAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')
app.config["MAIL_PORT"] = os.getenv('MAIL_PORT')
app.config["MAIL_USE_SSL"] = os.getenv('MAIL_USE_SSL')
app.config["MAIL_DEFAULT_SENDER"] = os.getenv('MAIL_DEFAULT_SENDER')

app.secret_key = "Not a secure key"  # Needed for sessions to work properly
mail = Mail(app)

loggedUsers = {}

# login_required decorator -- from a tutorial and adapted
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


# Generate list of all riddles available
allRiddles = json.loads(read_from_file("riddles.json"))


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
        self.current_route = route

        User.logged_users += 1  # Keep track of how many users are logged in

        def addLoggedUser(self):
            ''' Add a logged in user to the dictionary of logged in users. '''
            global loggedUsers
            loggedUsers[self.username] = self

        if self.username:
            addLoggedUser(self)


class Game(object):
    ''' This is the prototype of a game. When an instance is created it will be owned
        by a logged in user. If the user logs out or the game finishes the game instance
        will be destroyed. '''
    
    def __init__(self):
        self.riddles_sequence = []      # List of riddles [[id, url, ans], [..], ...]
        self.riddle_counter = -1        # Are these doing the same thing?
        self.current_riddle = []        # The current riddle [id, url, ans]
        self.attempt = 1
        self.points = 10                # Points gained for this attempt if WIN
        self.most_recent_answer = ""
        self.wrong_answers = []

        def generate_riddle_sequence(self):
            global allRiddles
            id_list = []
            for x in range(0, 10): #To select 10 random riddles
                repeat = True
                while repeat:
                    choose_game = random.choice(allRiddles)
                    if choose_game['id'] not in id_list:
                        repeat = False
                        id_list.append(choose_game['id'])

                item = []
                item.append(choose_game['id'])
                item.append(choose_game['source'])
                item.append(choose_game['answer'])
                self.riddles_sequence.append(item)

        def select_current_riddle(self):
            self.riddle_counter += 1
            self.current_riddle = self.riddles_sequence[self.riddle_counter]
            
        generate_riddle_sequence(self)
        select_current_riddle(self)


defaultUser = User("default", False, 0, [], "index")


def createUser(name):
    tempUser = User(name, True, 0, [])
    vars()[name] = copy.deepcopy(tempUser)
    loggedUsers[name] = copy.deepcopy(tempUser)
    return vars()[name]


def fill_best_individual_games():
    store = json.loads(read_from_file("hof_individual.json"))["best_individual_games"]
    return store


def fill_best_all_games():
    store = json.loads(read_from_file("hof_all_games.json"))["best_all_games"]
    return store


def store_game_info(username):
    thisUser = loggedUsers[username]
    thisUser.number_of_games += 1
    thisUser.total_user_points += thisUser.points_this_game
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    info = (today, thisUser.points_this_game)
    extract_games_played = thisUser.games_played
    thisUser.games_played.insert(0, info)

    if thisUser.points_this_game > thisUser.points_best_game:
        thisUser.points_best_game = thisUser.points_this_game
        thisUser.date_best_game = today  # Today's date
    
    allusers = json.loads(read_from_file("users.json"))
    
    allusers[username] = {"username": thisUser.username,
                            "games_played": thisUser.games_played,
                            "date_best_game": thisUser.date_best_game,
                            "number_of_games": thisUser.number_of_games,
                            "points_best_game": thisUser.points_best_game,
                            "total_user_points": thisUser.total_user_points}

    with open("data/users.json", "w") as outfile:
        json.dump(allusers, outfile, sort_keys=True, indent=4)

    # Update hof_individual.json
    insert_hof_info=[]
    insert_hof_info.append(today)
    insert_hof_info.append(username)
    insert_hof_info.append(thisUser.points_this_game)
    insert_in_hof_individual(insert_hof_info)

    # Update hof_all_games.json
    insert_all_games=[]
    insert_all_games.append(username)
    insert_all_games.append(thisUser.total_user_points)
    insert_all_games.append(thisUser.number_of_games)
    insert_in_hof_all_games(insert_all_games)

    thisUser.points_this_game = 0
    return


def insert_in_hof_individual(data):
    # global best_individual_games
    best_individual_games = fill_best_individual_games()
    # Get list of points from json - already sorted
    sorted_points = [] #Reverse order
    for item in best_individual_games:
        sorted_points.insert(0, item[3])
    
    # Add new points - only if it is more than at least the smallest number 
    if data[2] > min(sorted_points):
        sorted_points.insert(0, data[2])
        sorted_points.sort()
        
        # Reduce length of list to 10 so that I will have the best 10 
        # when I insert the new data
        while len(sorted_points) > 10:
            del sorted_points[0]

        # Build new list of sorted data
        insert_done = False
        
        new_points_list =[]
        counter = len(best_individual_games)-1
        pointer = 0
        
        for item in sorted_points:
            if item == data[2] and insert_done == False: # New item
                new_points_list.insert(0, (counter + 1, data[0], data[1], data[2]))
                insert_done = True
            else:
                if insert_done:
                    new_points_list.insert(0, best_individual_games[counter-1])
                else:
                    new_points_list.insert(0, [best_individual_games[counter-1][0] + 1, best_individual_games[counter-1][1],best_individual_games[counter-1][2], best_individual_games[counter-1][3]])
                    
                counter -= 1
                pointer += 1
    else:
        new_points_list = best_individual_games
    
    # Prepare dictionary to write as jason
    to_write = {}
    to_write['best_individual_games'] = new_points_list
    
    # Store to file
    with open('data/hof_individual.json', 'w') as outfile:
        json.dump(to_write, outfile,  sort_keys=True, indent=4)
        
    return


def insert_in_hof_all_games(data):
    # global best_all_games
    best_all_games = fill_best_all_games()

    # Get list of points from json - already sorted
    sorted_points = [] #Reverse order
    for item in best_all_games:
        sorted_points.insert(0, item[2])
    
    # Add new points - only if it is more than at least the smallest number 
    if data[1] > min(sorted_points):
        sorted_points.insert(0, data[1])
        sorted_points.sort()
        
        # Reduce length of list to 10 so that I will have the best 10 
        # when I insert the new data
        while len(sorted_points) > 10:
            del sorted_points[0]

        # Build new list of sorted data
        insert_done = False
        
        new_points_list =[]
        counter = len(best_all_games)-1
        pointer = 0
        
        for item in sorted_points:
            if item == data[1] and insert_done == False: # New item
                new_points_list.insert(0, (counter + 1, data[0], data[1], data[2]))
                insert_done = True
            else:
                if insert_done:
                    new_points_list.insert(0, best_all_games[counter-1])
                else:
                    new_points_list.insert(0, [best_all_games[counter-1][0] + 1, best_all_games[counter-1][1],best_all_games[counter-1][2],best_all_games[counter-1][3]])
                    
                counter -= 1
                pointer += 1
    else:
        new_points_list = best_all_games
    
    # Prepare dictionary to write as jason
    to_write = {}
    to_write['best_all_games'] = new_points_list

    # Store to file  
    with open('data/hof_all_games.json', 'w') as outfile:
        json.dump(to_write, outfile,  sort_keys=True, indent=4)

    return


@app.route('/<currentUser>', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def index(currentUser=defaultUser.username):
    try:
        if request.method == 'POST':
            if 'register' in request.form:
                return redirect(url_for('register')) 
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"

    allusers = json.loads(read_from_file("users.json"))
    message = ""
    thisUser=loggedUsers[currentUser]
    thisUser.current_route = "index"
    return render_template("index.html", thisUser=thisUser, message=message)

@app.route('/login', methods=['GET','POST'])
def login():
    thisUser=""

    try:
        if request.method == 'POST':
            username = request.form['username']
            allusers = json.loads(read_from_file("users.json"))
            
            if username == "":
                allusers = ""
                message = "Please enter your username to log in."
                return render_template('index.html', thisUser=defaultUser, username="", message=message)
            elif username in allusers.keys():  #User already registered
                print("User {} is registered".format(username)) #Debug
                # Is user already logged in?
                if username in loggedUsers.keys():
                    message = username + " is already logged in. Do you want to proceed? If you proceed the previous session will be destroyed."
                    return render_template("proceed_login.html", thisUser=defaultUser, username=username, message=message)
                else: # User is not logged in yet
                    x = createUser(username)
                    loggedUsers[username].total_user_points = allusers[username]['total_user_points']
                    loggedUsers[username].games_played = allusers[username]['games_played']
                    loggedUsers[username].points_best_game = allusers[username]['points_best_game']
                    loggedUsers[username].number_of_games = allusers[username]['number_of_games']
                    loggedUsers[username].date_best_game = allusers[username]['date_best_game']
                    loggedUsers[username].current_route = "user"
                    loggedUsers[username].is_logged = True
                    session['logged_in'] = True
                    return render_template("user.html", thisUser=loggedUsers[username], username="", message="")
            else:
                return redirect(url_for('register')) 
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"

    return "What has happened? login route is present."  #Should never reach here

@app.route('/proceed_login/<username>', methods=['GET', 'POST'])
def proceed_login(username):
    loggedUsers[username].session+=1
    loggedUsers[username].current_route = "user"
    return render_template("user.html", thisUser=loggedUsers[username])

@app.route('/register', methods=['GET','POST'])
def register():
    thisUser = copy.deepcopy(defaultUser)
    thisUser.current_route = "register"
    button_control = {}             # Control which buttons show up.
    button_control["username"] = ""
    button_control["register"] = ""
    button_control["check_active"] = ""
    button_control["register_active"] = "btn-deactivated btn-hide"
   
    try:
        if request.method == 'POST':
            username = request.form['username']
            allusers = json.loads(read_from_file("users.json"))
            button_control["username"] = username

            if 'check' in request.form:
                if username == "":
                    username_feedback = "Please type in a username and check its availability."
                elif username in allusers:
                    username_feedback = "Username already exist. Please try another one."
                else:
                    button_control["register"] = "register"
                    button_control["register_active"] = ""
                    button_control["check_active"] = "btn-deactivated btn-hide"
                    username_feedback = "Username available. Please click the register button."
                return render_template("register.html",button_control=button_control, username_feedback=username_feedback, thisUser=thisUser)

            if 'register' in request.form:
                username = request.form['username']
                if username == "":
                    username_feedback = "Please type in a username and check its availability."
                    return render_template("register.html",button_control=button_control, username_feedback=username_feedback, thisUser=thisUser)
                elif username in allusers:
                    username_feedback = "Username already exist. Please try another one."
                    return render_template("register.html",button_control=button_control, username_feedback=username_feedback, thisUser=thisUser)
                else:
                    allusers[username] = {"username": username, "games_played": [], "date_best_game": "", "number_of_games": 0, "points_best_game": 0, "total_user_points": 0}
                    with open("data/users.json", "w") as outfile:
                        json.dump(allusers, outfile, sort_keys=True, indent=4)

                    x = createUser(username)
                    loggedUsers[username].total_user_points = allusers[username]['total_user_points']
                    loggedUsers[username].games_played = allusers[username]['games_played']
                    loggedUsers[username].points_best_game = allusers[username]['points_best_game']
                    loggedUsers[username].number_of_games = allusers[username]['number_of_games']
                    loggedUsers[username].date_best_game = allusers[username]['date_best_game']
                    loggedUsers[username].current_route = "user"
                    loggedUsers[username].is_logged = True
                    session['logged_in'] = True
                    return render_template("user.html", thisUser=loggedUsers[username], username="", message="")
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"

    username_feedback = "Enter a valid username."
    return render_template("register.html", button_control=button_control, thisUser=thisUser)

@app.route('/logout/<currentUser>/<sessionNo>', methods=['GET', 'POST'])
@login_required
def logout(currentUser, sessionNo):
    if request.method == 'POST':    #RESET
        try:
            thisUser = loggedUsers[currentUser]
        except Exception as e:
            message =  "This session has expired. {} has been logged out from somewhere else.".format(e)
            return render_template("index.html", thisUser=defaultUser, message=message)
        
        try:
            if int(sessionNo) == thisUser.session:
                # Prepare to delete instances
                # IF GAME OBJECT EXIST DELETE, OTHERWISE DO NOTHING
                if thisUser.game == "":
                    pass
                else:
                    thisUser.game = ""      # del thisUser.game

                del thisUser
                del loggedUsers[currentUser]
                session.pop('logged_in', None)

                return redirect(url_for("index"))
            else:
                message = "This session has been disabled. You were logged out from somewhere else."
                return render_template("index.html", thisUser=defaultUser, message=message)

        except Exception as e:
            message="Something wrong happened. Please login again."
            return render_template("index.html", thisUser=defaultUser, message=message)

@app.route('/user/<currentUser>', methods=['GET', 'POST'])
@app.route('/user', methods=['GET', 'POST'])
@login_required
def user(currentUser=defaultUser.username):
    thisUser=loggedUsers[currentUser]
    thisUser.current_route = "user"
    return render_template("user.html", thisUser=thisUser)

@app.route('/halloffame/<currentUser>')
@app.route('/halloffame')
def halloffame(currentUser=defaultUser.username):
    thisUser=loggedUsers[currentUser]
    thisUser.current_route = "halloffame"
    best_individual_games = fill_best_individual_games()
    best_all_games = fill_best_all_games()
    return render_template("halloffame.html", thisUser=thisUser, best_individual_games=best_individual_games, best_all_games=best_all_games)

@app.route('/about/<currentUser>')
@app.route('/about')
def about(currentUser=defaultUser.username):
    thisUser=loggedUsers[currentUser]
    thisUser.current_route = "about"
    return render_template("about.html", thisUser=thisUser)

@app.route('/contact/<currentUser>', methods=['GET', 'POST'])
@app.route('/contact', methods=['GET', 'POST'])
def contact(currentUser=defaultUser.username):
    thisUser=loggedUsers[currentUser]
    thisUser.current_route = "contact"

    if request.method == "GET":
        return render_template("contact.html", thisUser=thisUser)
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message(subject, sender=email, recipients=[app.config['MAIL_DEFAULT_SENDER']])
        msg.body = "{} sent the following message from the Riddle-Me this game website: \n__________________________________________\n\n{}".format(name, message)
        mail.send(msg)
        return render_template("message_sent.html", name=name, email=email, subject=subject, message=message, thisUser=thisUser)
    except Exception as e:
        return render_template("message_error.html", email=email, thisUser=thisUser)

'''
ERROR EXAMPLE:
smtplib.SMTPRecipientsRefused: {'----------@a---------.--': (550, b'Verification failed for <-----@hotmail>\nThe mail server could not deliver mail to -----------@---------.  The account or domain may not exist, they may be blacklisted, or missing the proper dns entries.\nSender verify failed')}'''

@app.route('/game/<currentUser>', methods=['GET', 'POST'])
@app.route('/game', methods=['GET', 'POST'])
@login_required
def game(currentUser=defaultUser.username):  
    thisUser=loggedUsers[currentUser] 
    thisUser.current_route = "game"     # I will need this to control the menu

    if thisUser.game_on == False:
        thisUser.game_on = True     # Game On
        thisUser.game = Game()      # CREATE A GAME
    try:
        if request.method == 'POST':
            if 'play' in request.form:
                thisUser.game.points = 10
                thisUser.game.attempt = 1
            elif 'answer_btn' in request.form:
                if thisUser.game.attempt == 1:      # Check Answer
                    answer = request.form['answer_text']
                    # Clean the answer - If there are multiple spaces or other white characters in between the words
                    temp =[]                    # To hold Clean answer
                    temp = answer.split()
                    thisUser.game.most_recent_answer=""
                    for item in temp:
                        thisUser.game.most_recent_answer += item + " "
                    thisUser.game.most_recent_answer = thisUser.game.most_recent_answer.strip()  # Strip trailing spaces - there shouldn't be any left but just in case.
                    if thisUser.game.most_recent_answer.lower() == thisUser.game.current_riddle[2].lower(): # if match - answer correct
                        thisUser.points_this_game += 10
                        thisUser.game.wrong_answers = []
                        thisUser.game.attemp = 1                  # First attempt of
                        thisUser.game.riddle_counter += 1         # Next Riddle
                        if thisUser.game.riddle_counter > len(thisUser.game.riddles_sequence)-1:    # Call next riddle
                            return redirect(url_for('game_over', currentUser=thisUser.username))    # GAME OVER
                        else:                                                                       # Trigger next riddle
                            thisUser.game.current_riddle = thisUser.game.riddles_sequence[thisUser.game.riddle_counter]
                    else:                           # Otherwise answer is wrong
                        if len(answer) == 0:        #if no answer is given
                            thisUser.game.wrong_answers.append("-")
                        else:
                            thisUser.game.wrong_answers.append(answer)
                        thisUser.game.attempt = 2 # This is your next attempt
                        thisUser.game.points = 6  # Set correct number of points

                elif thisUser.game.attempt == 2:
                    # Get all words and concatenate them
                    answer = ""
                    index = ""
                    local_answer = thisUser.game.current_riddle[2].split()
                    for ndx, each_word in enumerate(local_answer):
                        index = 'answer_text' + str(ndx+1)
                        answer += (request.form[index].strip() + " ") #Strip any typed white spaces
                    temp =[]                        # Clean answer
                    temp = answer.split()
                    thisUser.game.most_recent_answer=""
                    for item in temp:
                        thisUser.game.most_recent_answer += item + " "
                    thisUser.game.most_recent_answer = thisUser.game.most_recent_answer.strip()         # Strip trailing spaces
                    
                    if thisUser.game.most_recent_answer.lower() == thisUser.game.current_riddle[2].lower(): # Answer correct
                        thisUser.points_this_game += 6          # Gain points
                        thisUser.game.attempt = 1                 # Reset attempt
                        thisUser.game.points = 10
                        thisUser.game.wrong_answers = []
                        thisUser.game.riddle_counter += 1         # Next Riddle
                        if thisUser.game.riddle_counter > len(thisUser.game.riddles_sequence)-1:     # Call next riddle
                            return redirect(url_for('game_over', currentUser=thisUser.username))
                        else:
                            thisUser.game.current_riddle = thisUser.game.riddles_sequence[thisUser.game.riddle_counter]
                    
                    else:                           # Otherwise answer is wrong
                        if len(answer) == 0:                #if no answer is given
                            thisUser.game.wrong_answers.append("-")
                        else:
                            thisUser.game.wrong_answers.append(answer)
                        thisUser.game.attempt = 3                 # This is your next attempt
                        thisUser.game.points = 2                  # Set correct number of points
                    
                elif thisUser.game.attempt == 3:
                    print("This is attempt 3 to check the answer.")
                    # Get all words and concatenate them
                    answer = ""
                    index = ""
                    local_answer = thisUser.game.current_riddle[2].split()
                    for ndx, each_word in enumerate(local_answer):
                        index = 'answer_text' + str(ndx+1)
                        answer += (request.form[index].strip() + " ") #Strip any typed white spaces
                    temp =[]                    # Clean answer
                    temp = answer.split()
                    thisUser.game.most_recent_answer=""
                    for item in temp:
                        thisUser.game.most_recent_answer += item + " "
                    thisUser.game.most_recent_answer = thisUser.game.most_recent_answer.strip()         # Strip trailing spaces
                    if thisUser.game.most_recent_answer.lower() == thisUser.game.current_riddle[2].lower(): # Answer correct
                        thisUser.points_this_game += 2           # Gain points
                        thisUser.game.attempt = 1                  # Reset attempt
                        thisUser.game.points = 10
                        thisUser.game.wrong_answers = []           # Reset wrong answers
                        thisUser.game.riddle_counter += 1
                        if thisUser.game.riddle_counter > len(thisUser.game.riddles_sequence)-1:     # Call next riddle
                            return redirect(url_for('game_over', currentUser=thisUser.username))
                        else: # Trigger next riddle
                            thisUser.game.current_riddle = thisUser.game.riddles_sequence[thisUser.game.riddle_counter]
                    else:       # Otherwise answer is wrong
                        thisUser.game.attempt = 1                 # This is your next attempt
                        thisUser.game.points = 10                 # Set correct number of points
                        thisUser.game.wrong_answers = []           # Reset wrong answers
                        thisUser.game.riddle_counter += 1
                        if thisUser.game.riddle_counter > len(thisUser.game.riddles_sequence)-1:
                            return redirect(url_for('game_over', currentUser=thisUser.username))
                        else: # Call next riddle
                            thisUser.game.current_riddle = thisUser.game.riddles_sequence[thisUser.game.riddle_counter]
            
            elif 'pass_btn' in request.form:
                if thisUser.game.attempt == 1:
                    thisUser.game.wrong_answers = []
                    thisUser.game.wrong_answers = ["-"]
                    thisUser.game.attempt = 2
                    thisUser.game.points = 6
                elif thisUser.game.attempt == 2:
                    thisUser.game.points = 2
                    thisUser.game.wrong_answers.append("-")
                    thisUser.game.attempt = 3
                elif thisUser.game.attempt == 3:
                    if thisUser.game.riddle_counter > len(thisUser.game.riddles_sequence)-1:
                        return redirect(url_for('game_over', currentUser=thisUser.username))
                    thisUser.game.points = 10
                    thisUser.game.attempt = 1
                    thisUser.game.riddle_counter += 1
                    thisUser.game.wrong_answers = []
                    if thisUser.game.riddle_counter > len(thisUser.game.riddles_sequence)-1:     # Call next riddle
                        return redirect(url_for('game_over', currentUser=thisUser.username))
                    else:
                        thisUser.game.current_riddle = thisUser.game.riddles_sequence[thisUser.game.riddle_counter]
    except Exception as e:
            message =  "This session has expired. {} has been logged out from somewhere else.".format(e)
            return render_template("index.html", thisUser=defaultUser, message=message)
    return render_template("game.html", thisUser=thisUser)

@app.route('/game_over/<currentUser>', methods=['GET', 'POST'])
@app.route('/game_over', methods=['GET', 'POST'])
@login_required
def game_over(currentUser=defaultUser.username):
    thisUser=loggedUsers[currentUser]
    thisUser.current_route = "user"  # I will need this to control the menu
    thisUser.game_on  = False
    flash(thisUser.points_this_game)
    store_game_info(currentUser)  # Updates Hall of fame too

    return render_template("user.html", thisUser=thisUser)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 8080)), debug=True)