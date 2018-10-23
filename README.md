# Riddle-Me-This Game - Work in progress

## Security

**A note about security**  
For this project I do not need high security.
For better security the secret_key should be completely random to make it very difficult to guess.
Ideally use a random key generator.
The key should be placed in a separate configuration file which would then be imported. 
I do not consider security to be an issue for this particular project considering the purpose.

For better security I would also implement a password that would be salted and hashed. Only the hash 
would then be stored. Again I am not doing this for this project.

## Overview
### What is this website for?
This project will form part of my submission for the Fullstack Web Developer course that I am doing at Code Institute.

This will be my milestone project for Practical Python module of the new LMS.

### Version Control and Deployment
This is the [github repository](https://github.com/abonello/project-3),
and this project is deployed on Heroku [here](https://riddlegame-ab.herokuapp.com).

I am basing this project on an earlier exploratory exercise that I did. This previous exercise was meant to be a draft to practice the techniques and skills I need for this project. It can be found [here](https://github.com/abonello/riddle-game-app).
Another project that I built to learn the techniques I need is an addition game. The code can be found [here](https://github.com/abonello/addition_game).

The main change I did from my earlier riddle game project is to base the current one on OOP. In this way I can have multiple users logged in without interfering with each other. This is what I learnt from the addition game.





### What does it do?


### How does it work



## Features
~~read information about my activites~~  
~~portfolio of compositions~~  
~~menu system~~  
~~contact~~


## Technologies
~~html5, CSS3, bootstrap 3.3.7, javascript, jQuery 3.3.1~~

~~I am using CDNs for bootstrap and jQuery.~~


## Ideas - brainstorming:


 

## Testing



## Code from other sources


## Riddle Images
These are modified versions of pictures from the web.

pip installed flask_mail and updated requirements.txt

Upgrade Flask to v1.0.2, git reported that the previous version 0.12.2 had a known security vulnerability.


Getting information about heroku deployment

```bash
$ heroku apps:info riddlegame-ab
=== riddlegame-ab
Auto Cert Mgmt: false
Dynos:          web: 1
Git URL:        https://git.heroku.com/riddlegame-ab.git
Owner:          connect@anthonybonello.co.uk
Region:         eu
Repo Size:      10 MB
Slug Size:      55 MB
Stack:          heroku-18
Web URL:        https://riddlegame-ab.herokuapp.com/
Anthonys-MacBook-Pro:project_3 anthonybonello$
```
Adding handling for 404 and 500 errors.
