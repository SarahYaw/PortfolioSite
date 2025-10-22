import datetime
from flask import Blueprint, render_template
from .data import *

bp = Blueprint('main', __name__) 

@bp.route('/')
def index(): 
    return render_template('index.html')

@bp.route('/experience')
def experience():
    context={}
    currentYear = datetime.datetime.today().year
    difference = currentYear - 2016
    context['years']=[]
    for year in range(0, difference+1):
        context['years'].append(currentYear-year)
    context['timeline_items_1'] = timeline_items_1
    context['timeline_items_2'] = timeline_items_2
    context['timeline_items_3'] = timeline_items_3
    context['timeline_items_4'] = timeline_items_4
    context['mobile_timeline'] = mobile_timeline
    return render_template('experience.html', context=context)

@bp.route('/projects')
def projects():
    context={}
    context['code_projects'] = code_projects
    context['art_projects'] = art_projects
    return render_template('projects.html', context=context)

@bp.route('/bugs')
def bugs():
    context={}
    return render_template('bugs.html', context=context)
# Additional routes can be added here