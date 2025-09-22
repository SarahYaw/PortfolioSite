from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__) 

@bp.route('/')
def index(): 
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/projects')
def projects():
    context={}
    context['code_projects'] = [
        {
            'name':'Form to PDF Python Program',
            'description':"Program that lets the user import a CSV of questions and options into this program, answer the questions, export a PDF of the filled out form. Built in python using tkinter for the UI.",
            'skills':'Python (Programming Language) · Tkinter · Project Planning · Application Development · Requirements Gathering',
            'src':'/static/assets/code/formToPdf.png',
            'alt':'Plain form with example questons and answers. Black text on a gray background.',
            'link':'https://github.com/SarahYaw/simpleFormToPDF',
            'caption':"I've built this as a base for a project I'm building for a relative who has to fill out the same form every other week who's just editing PDFs all the time, hopefully this makes things easier. I'm going to make a private fork off of this so I can specify it to their situation. Any part that I looked up a lot for I put the link in the code right near it",
        },
        {
            'name':'Medication Manager React.js Project',
            'description':"Webpage that allows you to enter medications for it to track when you're due for a refill, how often you take it, who prescribed it, etc. Basic webpage with a basic back-end that gives you a CRUD interface for a table of entries. Made to brush up on React.js.",
            'skills':'React.js · Node.js · Tailwind CSS · TypeScript · User Interface Design · LoopBack.io',
            'src':'/static/assets/code/medManager.png',
            'alt':'Chart listing med name, dosage, description, morning dose, afternoon dose, evening dose, provider, last refilled, and buttons to refill, edit, and remove the medication from the list',
            'link':'https://github.com/SarahYaw/MedManager',
            'caption':'Made this as a proof-of-concept for a relative that wanted a more at-a-glance way to keep track of their medications.',
        },
        {
            'name':'AudioAI',
            'description':"Web application that allows users to use LLM's and AI voice software to create novel renditions of spec spots and other segments to fill air time. Connects to quite a few different automation softwares to air the tracks on-time.",
            'skills':'GitHub · Wireframing · Node.js · Visual Studio · Web Applications · Bootstrap (Framework) · Web Application Development · Front-End Development · Software as a Service (SaaS) · JavaScript · Application Development · Full-Stack Development · Application Programming Interfaces (API) · Cascading Style Sheets (CSS) · Git · TypeScript · Django · Project Development · REST APIs · Software Development · User Experience (UX) · Python (Programming Language) · Back-End Web Development · HTML · Vue.js · Web Development',
            'src':'/static/assets/code/audioai.png',
            'alt':'audio ai user interface showing the various adjustments one can make to a voice.',
            'link':'https://futurimedia.com/solutions/audioai/',
            'caption':'AI empowered web software that allows instantaneous production of audio commercials, spec spots, and other clips to be played over radio.',
        },
        {
            'name':'Beacon',
            'description':'This beacon mobile application is what the end-users will interact with. I did work on the administrative web application, but that is not open to the general public.',
            'skills':'GitHub · Wireframing · Node.js · Visual Studio · Web Applications · Vuetify · Web Application Development · Front-End Development · Software as a Service (SaaS) · JavaScript · Application Development · Full-Stack Development · Application Programming Interfaces (API) · Cascading Style Sheets (CSS) · Git · Project Development · REST APIs · Software Development · User Experience (UX) · Python (Programming Language) · HTML · Vue.js · Web Development',
            'src':'/static/assets/code/beacon.png',
            'alt':'beacon mobile application.',
            'link':'https://www.beaconalwayson.com/',
            'caption':'Safety alert system that sends audio and text emergency and warning alerts via radio and downloadable mobile application by location from multiple official sources.',
        },
        {
            'name':'SpotOn',
            'description':"Web application that allows users to use LLM's and AI voice software to create novel renditions of spec spots and other segments to fill air time.",
            'skills':'GitHub · Wireframing · Node.js · Visual Studio · Web Applications · Bootstrap (Framework) · Web Application Development · Front-End Development · Software as a Service (SaaS) · JavaScript · Application Development · Full-Stack Development · Application Programming Interfaces (API) · Cascading Style Sheets (CSS) · Git · TypeScript · Django · Project Development · REST APIs · Software Development · User Experience (UX) · Python (Programming Language) · Back-End Web Development · HTML · Programming · Web Development',
            'src':'/static/assets/code/spoton.png',
            'alt':'Spot On user interface showing a soundwave under the header Current Spot, and options to manage the spec spot and adjust audio levels.',
            'link':'https://futurimedia.com/solutions/spoton/',
            'caption':'One-Click spec spots and audio commercials.',
        },
        # {
        #     'name':'code2',
        #     'description':'code2',
        #     'skills':'PythonGathering',
        #     'src':'/static/assets/PennyMabelLeaves.jpg',
        #     'alt':'code2',
        #     'link':'code2',
        #     'caption':'code2',
        # },
    ]
    context['art_projects'] = [
        {
            'name':'art',
            'description':'art',
            'skills':'PythonGathering',
            'src':'/static/assets/art/PeerReviewCrossStitch.jpg',
            'alt':'art',
            'link':'art',
            'caption':'art',
        },
        {
            'name':'art2',
            'description':'art2',
            'skills':'PythonGathering',
            'src':'/static/assets/art/pumpkinHead.jpg',
            'alt':'art2',
            'link':'art2',
            'caption':'art2',
        },
        {
            'name':'art2',
            'description':'art2',
            'skills':'PythonGathering',
            'src':'/static/assets/art/TissueCoverAbleSisters.jpg',
            'alt':'art2',
            'link':'art2',
            'caption':'art2',
        },
        # {
        #     'name':'art2',
        #     'description':'art2',
        #     'skills':'PythonGathering',
        #     'src':'/static/assets/art/pumpkinHead.jpg',
        #     'alt':'art2',
        #     'link':'art2',
        #     'caption':'art2',
        # },
        # {
        #     'name':'art2',
        #     'description':'art2',
        #     'skills':'PythonGathering',
        #     'src':'/static/assets/art/pumpkinHead.jpg',
        #     'alt':'art2',
        #     'link':'art2',
        #     'caption':'art2',
        # },
        # {
        #     'name':'art2',
        #     'description':'art2',
        #     'skills':'PythonGathering',
        #     'src':'/static/assets/art/pumpkinHead.jpg',
        #     'alt':'art2',
        #     'link':'art2',
        #     'caption':'art2',
        # },
    ]
    return render_template('projects.html', context=context)


@bp.route('/contact')
def contact():
    return render_template('contact.html')

# Additional routes can be added here