from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .data import art_projects, code_projects, timeline_items

bp = Blueprint('main', __name__) 

@bp.route('/')
def index(): 
    return render_template('index.html')


@bp.route('/about')
def about():
    context={}
    context['timeline_items'] = timeline_items
    return render_template('about.html', context=context)

@bp.route('/projects')
def projects():
    context={}
    context['code_projects'] = code_projects
    context['art_projects'] = art_projects
    return render_template('projects.html', context=context)


@bp.route('/contact')
def contact():
    return render_template('contact.html')

# Additional routes can be added here