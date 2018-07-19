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

def add(x,y):           #This is a testing function -- Will be removed at that end.
    """Add Function"""
    return x + y

@app.route('/', methods=['GET','POST'])
def index():
    num1 = 100
    num2 = 56
    ans = add(num1, num2)
    return "It is working. Answer is {}".format(ans)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 8080)), debug=True)