# Milestone Project 3 - Riddle-Me-This Game
## Practical Python
 - Work in progress

*Developer: Anthony Bonello*

-------
**INDEX**

* [INTRODUCTION](#introduction)
* [UXD](#uxd)  
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [WIREFRAMES](#wireframes)
* [LOGIC FLOW DIAGRAM](#game-logic-flow-diagram)
* [FEATURES](#features)
* [TECHNOLOGIES USED](#technologies-used)
* [TESTING](#testing)
* [DEPLOYMENT](#deployment)
* [CREDITS](#credits)
---------

## INTRODUCTION
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

### **A Guessing Game**  
This is the milestone project for the “Practical Python” module, part of the New LMS in the “Full Stack Web Development Course” offered by Code Institute.

The purpose of the game is to guess a word or phrase from a given picture. Three attempts are allowed. With each subsequent attempt, further clues will be shown at the expense of reduced points.


### **What I plan to achieve? - An overview**  
The first decision I felt I have to make is wether to use a text-based or a picture-based riddle. I did a google search and I found some material that I can use as a picture-based riddle game. I also thought that a picture-based would be more attractive to a wide range of users of different ages. I decided to go down this route. See [credits](#credits) for these pictures.

Then I sketched a few layouts (pencil and paper) to get a general feel of how I would get the game to flow and an idea of layout of various parts. I sketched the logic of the game using a [flow diagram](#game-logic-flow-diagram).

The game will randomly select 10 riddles from a pool of riddles. The user will be presented with the first riddle. The user has to write the answer for the riddle and submit the answer by pressing a button. An option to pass is also provided. 

A submitted answer will be checked against the stored answer and if correct a second riddle is presented. If the answer is wrong or if the user chooses to pass, a second attempt at answering will be offered. This time the user will be told how many words are expected in the answer. Similar submit and pass options are offered. If the answer is wrong or the user passes, a third attempt is offered. This time the user will be shown how many words should be in the answer and how many letters are in each word. After this final attempt the user will be directed to the next riddle, unless it is the final one, in which case the game will end and the user will be directed to the user page.

Points gained will be displayed on the user page and if they are high enough they will be added to the Hall of Fame.
____


## UXD
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

>This is the latest incarnation of my website. Its main function is to be an extension of my CV and having a place of contact if someone wants to get in touch but does not know my email address.

>The plan is to have a single page website with a parallax background. The design should be responsive.

### **Strategy** 
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

--------
```
**What do I want as the owner of the site?**
* Internet presence  
* Means to communicate with me  
* Portfoilio  
* Brief info about my activities  
```

-----------
>This is my personal website as a musician. It needs to serve as an extension of my CV for music related activities.

>People who might use the website are:
```
* someone wanting to learn music; beginners / continuing / pick up an instrument which they played when they were younger  
* performers wanting to perform one of my pieces  
* people wanting to commission a new composition or arrangement 
* artists wanting to collaborate on an art piece which include music or audio  
* someone looking for a conductor for an orchestra or a band.
```

#### What does it do?
>This website gives visitors information about my various activities related to myself as an active musician.  
It is targeted at potential clients who would like to use my services as a composer/sound desgner, conductor, performer or teacher.
Visitors have the ability to contact me by using a contact form.

#### How does it work
>The website is planned as a single page application. Each section is well separated from the others through the use of alternating background so that the material is distinct. Extra information about my activities can be accessed through the *Tell me more ...* buttons.  

>The navigation will smoothly scroll up and down so that the users will know that they are still on the same page rather than taken to a different page. This helps the users to keep track of where they are.



### **Scope** 
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

#### Features to implement
```
* Activities - some sort of list with some details and possibly extending the information,
* A short Bio,
* Examples of my compositions with the possibility for the user to listen to these examples,
* A way for the user to get in touch without revealing my email address,
* Links to Github and Linkedin.
```

#### User stories
```
* A potential student (or a parent) wanting to learn an instrument can read about my teaching and then be directed to get in touch through the online form.

* A performer wanting to play one of my pieces comes to the site to get in touch and ask for scores. The performer is given the opportunity to find out more and directed to the contact form.

* A fixer for a music group is looking for a french horn player. The fixer will be directed to the contact form.

* A person is interested in commissioning a new piece (acoustic / electroacoustic / mixed). This person will have the opportunity to read about me as a musician and offered the possibility to start communicating and ask questions through the contact form.

* A music group representative needs a conductor, perhaps to step in for their regular conductor. This person will have the opportunity to read about me as a musician and in particular, me as a conductor. There will also be the opportunity to get in touch and ask questions.

* An artist (ex visual artist) has an idea to build an installation and would like to include sound, perhaps self-generating sound depending on the movement of people within the installation space.
This artist will have the opportunity to read about my compositions and also to listen to some examples. There will be the opportunity to get in touch through the online contact form.
```
### **Structure**
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)
```
The plan is to have a Single Page Application (SPA) website. It will be divided into three main sections:
1. Activities
2. About Me (short bio)
3. Portfolio
```
>There will also be a fixed **navigation** at the top, a **header** just below the navigation, a **contact form** and a **footer** with links.

>I decided against having obvious headers for the activites and the portfolio sections. If someone reaches them from the navigation they will know before arriving. For someone arriving there through scrolling, the subheadings in the activites and the content of the portfolio is easy to distinguish.   

>I feel that adding blaring titles to these sections will be overkill and sort of corny.

>I will also add a quote section between the portfolio section and the contact form. This will form a natural break of an otherwise two sections using the greyish gradient background.

>**Navigation** will be through the nav buttons at the top, the buttons (Primary and Secondary CTA) as well as through scrolling.

>The overall feel of the page should be one of soft scrolling, avoiding instant jumps which might imply to the user that they are on a different page.

----
>The **Activities** part will be divided into 6 activities: 
```
1. Composition
2. Sound Design
3. Conducting
4. Performance
5. Music Tuition
6. Research 
```

>These activities will stack on top of each other in mobile view, but will be displayed in three rows of two for tablets and two rows of three on desktop.

The **Portfolio** part will contain a few examples based on the music I have available on soundcloud, as well as an example from my youtube channel.

>I plan to have these stack one on top of each other in mobile view. In tablet and desktop views, there will be enough space to include an image which is evocative of an idea related to the music. (Images to alternate left - right)


### Skeleton
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

>The overall plan is to have a Single Page Application with a fixed navigation at the top. This allows the user to reach all main sections of the site.

>There will also be buttons to open the *Tell me more ...* sections related to different activities.

>CTA buttons will be placed in strategic parts of the site to allow the user to directly reach the contact form.

>Priority was given to the various activities that I engage in, followed by the bio and then the portfolio. The quote is only there as a visual separation between the portfolio and the contact form.

* [wireframe](#wireframes) - follow this link for further reading


### Surface
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

>The overall design is unified by the alternating dark triangle background with the greyish gradient background sections. The color scheme is monochromatic with some contrasting collors for CTA (buttons). 
        
>The use of parallax background in alternating sections creates an interesting break to the grey gradient background as well as to give this SPA a structure (form). The grey gradient background is enhanced with an image which sits in the ::before selector.

>All navigation is animated and controlled by javascript to give a smooth scroll effect. This enables the users to feel that they are like moving on a map rather than thrown from one place to another without knowing where they landed. The navigation acts as a sort of breadcrumbs as javascript keeps track of the page position and highlight the appropriate menu item.

>Overall, the content will be dispalyed in one column spanning the whole width of the screen in mobile view.
On tablets, this will change to a two column view (half each) for the activities. At this point I will also add images next to each portfolio item in alternate positions (left - right). In desktop view, the activites will display in two rows of three equal columns.

>The images used are related to the feel, emotions, and/or philosophy of the adjacent composition.

>In all views, the About Me and the Contact form will be full width.

>The footer will be stacked in one column in mobile view and will get a two column layout for the tablet and desktop views. (Note that the *back to top* link will remain centered for all views.)

>The quote was added to facilitate the flow of the overall structure of the page by breaking two adjacent sections which have the greyish gradient background and also helps in the form, akin to a **Rondo** musical structure.

#### Colors 

```
* **Heading color**:  
rgb(255, 233, 184) is taken from music background image.  

* **Logo Color / Brand**:  
rgb(255, 255, 240) with a transition to red with a hue-rotate of -50deg to reach rgb(217, 40, 188) #d928bc, the same colour used by for the hover of the secondary CTA. The reason why this color is initially set to red is to get the color transition to work over the range of colors I wanted.

* **Background color** (For non-parallax sections): ```

```
```
* **Text color**:  
rgb(0, 0, 0) (*changed from #D5D5D5*) for grey gradient backgrounds and color: rgb(255, 233, 184) (same as header) for text on triangular background, including about me, quote and footer. 
NB: *text color for grey gradient background changed again from rgb(25, 39, 51); to aid readability*.

```
```
* **footer &lt;a&gt; color**:  
rgb(255, 233, 184) and rgb(255, 195, 66) when hovered. Text of links will slightly increase in size on hover too.    
Same colors are used for links in **About Me**.

* **Form error color**:  
#e2631f  

* **Button colors** (complementary colors):  
    * **Primary CTA** : rgb(253, 134, 29) #fd861d
    * **Secondary CTA** :rgb(99, 40, 217) #6328d9 with a hover color of rgb(217, 40, 188)
#d928bc
* Set all buttons in soundcloud to value %23ff5500 (orange). This color code is one of the standard soundcloud colors.
```

#### Typography

>Fonts used are from [google fonts](https://fonts.google.com/). The main font is **Roboto** with a fall-back to sans-serif. The other font used is **Lobster** with a fall-back to Cursive. The latter was chosen as it contrasts well with roboto and sans-serif. This is used in two places, the logo and the main header of the page.


## WIREFRAMES
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)  
* [Back to Skeleton](#skeleton)

A mockup wireframes for this game has been prepared using  
![Pencil](static/img/Pencil-logo-shadow.png) [**Pencil Project**](https://pencil.evolus.vn/). If you click on the buttons it will mimic the general flow of the game.

You can reach these [here](https://abonello.github.io/project-3_wireframe/)  
Please note that a copy of the files for this wireframe are in this repository too at [WireFrame/index.html](https://github.com/abonello/project-3/tree/master/WireFrame)  

## GAME LOGIC FLOW DIAGRAM
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)  
* [Back to Overview](#What-I-plan-to-achieve?---An-overview)  

This is the flow diagram of the logic controlling the game.
![Logic Flow Diagram](WireFrame/pages/game_logic_flow_chart.png)



## FEATURES
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)


### Existing Features

>Navigation is through a menu which appears as a button for mobiles and tablets, and as a fixed menu at the top of the page in desktop view. 
Clicking on a menu item will start a smooth scrolling to the top of that section within the page. This is done in order not to confuse the user in thinking that this is a new page.

>Also the menu keeps track of which section a user is currently in. The menu item for the current section is highlighted with a darker background. This acts as a sort of breadcrumb.

>Parallax background gives the page a feel of progressing since the foreground scrolls against something which is fixed. To a lesser extent the gradient background helps create a sense of movement as well while scrolling.

>Each section in the activities allow the user to read about that particular activity. The *Tell me more ...* button displays further information.

>The About me section is a short bio. The link to my linkedin allows a reader to find more about me. There is also a CTA button.

>The portfolio allows the user to listen to some examples of my music from soundcloud and youtube.

>The contact form - through email.js,  allows the user to get in touch with me, enabling all the tasks which depend on this, asking for scores, performance / conducting opportunities, composition / sound design / arrangement / collaboration propositions, questions about tuition.  
A modal will appear to confirm to the user that the message has been sent.  
Please note: Since I am actually using this project on my site, I did make the contact form functional.


### Features Left to Implement
```
1. FIXED: ~~Improve the functionality of the CTA button on mobiles. It should direct the user to the top of the contact form. Instead it is directing the user to the submit button. The user has to scroll back up.~~
2. In the future I might add a complete list of my compositions with details of instrumentation and details about performances.
3. Add current and future activities.
4. Fix parallax for mobiles
```



## TECHNOLOGIES USED
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

# REVISE THIS SECTION

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used to build the sctructure and the content of this project.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - used for styling this project.
- [jQuery v3.3.1](https://jquery.com) - simplifies accessing the DOM.
- [Bootstrap v3.3.7](https://getbootstrap.com/docs/3.3/) - used for some of the styles (modified), as well as layout of the content.
- [Font Awesome v4.7.0](https://fontawesome.com/v4.7.0/) - used to display the GitHub and Linkedin Icons.
- [Google Fonts](https://fonts.google.com/) - Lobster and Roboto.
- [email.js](http://www.emailjs.com/) - used to enable the contact form to send emails to me.
- [jasmine v2.4.1](https://github.com/jasmine/jasmine) - behavior-driven development framework, used to unit test the functions related to form validation.
- [Compress JPEG ](compressjpeg.com) - I use GIMP to manipulate images. Once I export them as jpg, I use Compress Jpeg to minify them. Usually, I can gain between 25% and 50% reduction in file size.

## TESTING
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

### Final check on desktop

I tested the various scrollings on desktop using Safari v8.0.8, Chrome v68.0.3440.106 and Firefox v62.0.

### Manual testing using Chrome.
Example of testing steps:  
1. css link - set body background color to red. Pass (before it was white)
2. script.js link - append hello world div using jQuery. Checked in Chrome. Pass  
Noticed that links for bootstrap (both css and js are not loading.)
3. Changed links for bootstrap - now loading. Checked with Chrome.
4. Gave (main sections) divs a temp class with a border and some height. Pass Checked with Chrome.
5. When I click the Tell me more button for the composition section, a new div is displayed below the activities section. Pass  
6. Test that all other buttons work. Pass. All 
7. The code for scrolling to the newly displayed info is working well. Pass. Checked with Chrome
8. Extra info is hidden when a new activity is selected Pass
9. Page scrolls back to the top of the calling activity when extra info is closed. Pass
10. When extra info is closed its height is reduced while scrolling. Pass - This makes the action smoother. Especially for the lower cards where the scrolling is slower and might not hide the place previously taken by the extra info just closed.
11. Fixed problem created from unequal sizes of activities cards. Pass
12. Hide images in portfolio in extra small. Pass
13. Tested media query for margin in composition portfolio. Pass
14. Changed jQuery code that shows current year in copyright note with javaScript as it was waiting to load everything including the 
code from SoundCloud. This was resulting in the page sitting note showing the correct copyright note. Pass
15. The contact form itself has no back end and will not submit anything. 
    To indicate some activity I added jQuery code to display an alert when the contact form is submitted. This was tested. Pass
16. Added validation code. Tested - Pass
17. Added code that will hide the collapsed menu when an item is selected. Pass

### Manual Testing - User Stories

* A student / parent is looking for a music teacher:  
    1. The user comes to the page
    2. Clicks on activites in the menu (or scrolls down manually to the activities section)
    3. Reaches the Music Tuition part
    4. Clicks on the *Tell me more ...* button (secondary CTA)
    5. Reads the content
    6. Press the *get in touch* button (primary CTA)
    7. Fills in the form and press the submit button

**Test pass on desktop.**

-----

* A performer wants to play one of my pieces: *could have heard it somewhere else or looking for anything I can provide*  
    1. The user comes to the page
    2. Clicks on activites in the menu (or scrolls down manually to the activities section)
    3. Reaches the Composition part
    4. Clicks on the *Tell me more ...* button (secondary CTA)
    5. Reads the content
    6. Press the *get in touch* button (primary CTA)
    7. Fills in the form and press the submit button

**Test pass on desktop.**

-----

* Someone is looking for a french horn performer:
    1. The user comes to the page
    2. Clicks on activites in the menu (or scrolls down manually to the activities section)
    3. Reaches the Performance part
    4. Press the *get in touch* button (primary CTA)
    5. Fills in the form and press the submit button

**Test pass on desktop.**

-----

* A person would like to commission a new composition.  

    There are multiple routes such a user can take.
    If someone looked for me to commission a piece, that person would know something about my music. Otherwise this person will:

    1. Come to my page
    2. Click on the Portfolio in the menu
    3. The user will click on the various buttons to listen to some of my music.
    4. When the user has listened enough, they might choose to contact me.  
        They will reach the contact form either through the contact menu item or by scrolling to the bottom of the page.  
        Listeneing to music takes time and if the user is ready to stay and listen they will have all the time to explore the whole page.

    In any case commissioning a piece of music is not a decision taken there and then but will involve a lengthy communication.

**Test Pass. Contact form tested separately.**

-----

* Someone is looking for a conductor.  
    1. Come to the page
    2. Click on Activities from the menu
    3. Read various sections such as conducting / composition /sound design  
        Each extended section has a close button that will take the user back to the calling activity.
        There is also a primary CTA button in case the user is ready to get in touch.
    4. The user might also choose to read more about me and possibly extend to the Linkein profile.
    5. When the user is ready, they can use the contact form to contact me (or if they are in linked in, they might choose to contact me from there).

**All tested and works well**

-----

* A visual artist wants to collaborate on a multimedia project:

    1. The artist comes to my site
    2. Reads various sections from my activities including the extended sections. Possibilities include composition / sound design / research.
    3. If the user feels ready to contact me, a CTA button is available.
    4. Alternatively the artist might want to read more about me in which case s/he will go to the About Me either by scrolling or by using the navigation buttons. There is the possibility to reach my Linkein.
    5. The artist might decide to listen to some of my music from the portfolio.
    6. When the artist wants to get in touch there are various routes available. In the section where the CTA button is available this will take the user straight to the contact form. Otherwise, the user can scroll to the contact form or use the Contact link in the navigation bar.

**All tested and works well**

-----

* Testing the contact form  
Test reaching the contact form from various places. PASS with the exception that ~~the CTA buttons will take the user to the submit button on mobile devices~~. This has now been fixed.
    1. Submitting empty form: **Error message shown to user prompting to fill in the name**
    2. User fills in only name and trying to submit: **Error message shown prompting user to fill in email**
    3. User fills in first part of email only (Ex. asdf): **Error message showing that the email lacks an @ symbol**
    4. User adds @ symbol and tries to submit: **Error message telling the user that the part following the @ symbol is missing**
    5. User completes the name and email and leaves the rest of the form empty: **Error message prompting the user to fill in a subject**
    6. User fills in the name, email with correct format and subject and tries to submit: **Error message prompting user to write a text message**  
        Following this typing less than 3 letters, an error message prompts the user that the message should be at least three letters long. (This is an arbitrary number.)
    7. Trying to send a filled in form with a fictitious email that passes the format test (EX: asdf@asdfg.saf): **Error modal saying that Send email failed**.  
    This is due to "Sender verify failed error" raised by the email server.
    This offers me some protection from receiving spam from people who try to mimic an email address.


### Mobile / Tablet testing

Apart from using Chrome developer tools to test the layout and functionality of the page in mobile and tablet layouts, I also tested the site on my mobile phone and that of my friend. Both are android phones.  

The site is responsive and everything seems to work well in chrome developer tools. However, when viewed on a real phone, I noticed that the parallax background is not working as intended. In these cases it gracefully degrades to a normal background that scrolls with the page.

I found that this is browser dependent. Google Chrome (Mobile v68.03440.91) does not display the parallax background as intended, but Firefox (Mobile v61.0.2) does. I googled for any possible solutions but none of the suggestions work.

FIXED: ~~I also noticed that the CTA button on mobiles will direct the user to the submit button of the form. The user will have to scroll back up.~~ (This functionality works well on desktop.)


### Unit testing Code for Form Validation

I refactored the code related to the form validation and used **Jasmine** (v2.4.1) to unit test the functions. I noticed that I could not unit test the code straight in the javascript file I was using due to the code being in a $(document).ready function. For this reason I copied the code to a separate file for testing, copying back any changes I make.

The code beign tested, the spec code and the html which runs the unit tests are in [this folder](/Users/anthonybonello/Documents/FullStackWebDeveloper/CI_MilestoneProjects/project_1/jasmine). I am also including a zip of the version of jasmine I used. If you would like to run the unit tests, you will need to unzip this in addition to the files I made.

Note: I had to add jQuery (v3.3.1) to the html file.


While doing the unit tests I did uncover two bugs. The first one allowed a user to send the form by just filling spaces for the name, subject and message, together with an email.
The second one allowed a user to ignore the error messages and still try to send the form. More on these two bugs below, in the BUGS section.




### BUGS

1. 

~~As mentioned in the testing section above, when the CTA button is clicked in mobile devices the user is taken to the submit button instead of the top of the contact form. I tried to look into this but I cannot find a way to improve on this at the moment. I consider this bug as high priority to fix.~~

**FIXED**

This bug is now fixed. It took me about 8hrs of work and testing but it was worth going through the process. All I had to do is to get the height of the extended info section that will be set to 0px on closing, and take that amount in consideration when scrolling to the top of the contact form. The complexity arises from the fact that I used the CTA buttons in two other places, outside of the extended info. These are not meant to collapse. I solved this by separating the actions in different functions, something that I should have done from the start. NOTE: The reason why I want to reduce the height of the extended section to 0px is a visual one. I want to animate this in order to avoid a sudden jump that would otherwise happen. This is in keeping with the overall feel of the site that all movements are done smoothly.  

Tested manually on google chrome and my mobile (Android) and it works well.

----
2.
~~While unit testing, I noticed that I can just filling spaces for the name, subject and message, together with an email and still be able to send the form. I did not like this and consider it a bug.~~

**FIXED**

This is now fixed. I added code that would reject a white space. Adjacent white spaces would be collapsed to a single space and thus reject too.

----

3.
~~A Bug allowed a user to ignore the error messages and still try to send the form. Example, If I fill in the name and email and then add a subject containing a special character that I am not accepting, I can fill in the message, ignore the error and try to submit the form. On doing this, the page would refresh. Apart from this the user would not get any feedback on what has happened and why.~~

**FIXED**

This bug is now fixed and an alert will be displayed whenever a error is displayed including this particular case. When the user dismisses the alert, s/he will be taken back to the form to do the necessary edits.

----


4. 
The other bug is the background parallax effect. It does not work on all mobile browsers. I researched this on google but none of the fixes I came across seems to work. This is not a high priority bug as the site still looks and functions well without the parallax effect.


### Cleaning and validating code

* **HTML** - https://validator.w3.org/  
>There are a number of warnings for the iframes realted to the code from soundcloud. The validator complains about width beign set to 100%. I tried removing this and the iframe will only occupy half the width I want. With width="100%" it works and fills all the space available.  
There is an Error saying that | is an illegal character. This is found in code copied from google fonts. I am leaving this as is.
There are errors saying: "The element button must not appear as a descendant of the a element". These are properly nested and work well as they are and they ensure that no matter where the user clicks on the button it will elicit a response.

* **CSS** - https://jigsaw.w3.org/css-validator/  
>It complains about vendor prefixes in code that comes from colorzilla (re background gradient) or was added by form validator. I am goind to leave these as they are.  
There is also another warning about two classes having the same background and border colors. I will keep these as they are.
```
* **Form Validator** -  https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation

* **JavaScript** - http://esprima.org/demo/validate.html
>Code is syntactically valid.
```
* **jshint Linter** - http://jshint.com/
>Note: *Linter complains that there are 2 undefined variables, namely* **$** *and* **emailjs**. *These are defined in imported files,* **jquery-3.3.1.min.js** *and* **email.min.js** *respectively.* 


## DEPLOYMENT
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

The repository of this project is at [**github repository**](https://github.com/abonello/project-3),  
and it is deployed on Heroku [**here**](http://riddlegame-ab.herokuapp.com/).

# NEED TO ADD NOTE ABOUT HOW TO DEPLOY



## CREDITS
* [Back to TOP](#Milestone-Project-3---Riddle-Me-This-Game)

### Code from other sources
>Apart from some code based on examples in Bootstrap, I am using code provided by soundcloud and youtube to access the material on these sites.  
The code for scrolling is adapted from various tutorials. I have modified it and used it before in various projects.
It is heavily documented on youtube and elsewhere.  
[colorzilla](http://colorzilla.com/gradient-editor) to create background gradients.


### IMAGES
>**Dark Triangles** for background:  
Downloaded from [Subtle Patterns](https://www.toptal.com/designers/subtlepatterns/tag/dark/)  
Image notes: JUNE 7, 2017  
Playful triangle pattern, this time in black.  
Use: All patterns on this site can be used free of charge, but please [read this](https://creativecommons.org/licenses/by-sa/3.0/) before using them: CC BY-SA 3.0 - Subtle Patterns © Toptal Designers.

**Wood Image** for background of grey areas:  
>Downloaded from [Pexels](https://www.pexels.com/photo/background-board-construction-dirty-269035/)  
Use: CC0 License  
Image is cropped to create a seamlessly horizontally tiling image;  
copied, inverted and pasted below to created a seamlessly vertically tiling image.

>**fast-min.jpg**
[Pexels](https://www.pexels.com/photo/light-trails-on-city-street-327345/)
Use: CC0 License  
Image is cropped, rotated, sheared, resized.

>**Ringtone.jpg**  
found at https://blog.ambient-mixer.com/sound/what-your-ringtone-says-about-your-personality/  
Image Credit by = http://bit.ly/1HLbWKi  

>**battle.jpg**
found at [Wikipedia](https://en.wikipedia.org/wiki/Mahdist_War#/media/File:Bataille_d%27Ondurman_2.jpg)  
Use: Public Domain  
Image cropped and resized.

>**Slideshow.png**
found at [Pexels](https://www.pexels.com/photo/curve-industry-photography-vintage-65128/)  
Use: Pexels License  
Free for personal and commercial use, No attribution required  
Image is cropped and resized.

### FONTS
>**Lobster** and **Roboto** fonts from [google fonts](https://fonts.google.com/).

















----------------

==========================


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