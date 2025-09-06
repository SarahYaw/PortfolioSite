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
            'name':'code',
            'description':'code',
            'src':'/static/assets/MabelMetalBowl.jpg',
            'alt':'code',
            'link':'code',
            'caption':'code',
        },
    ]
    context['art_projects'] = [
        {
            'name':'art',
            'description':'art',
            'src':'/static/assets/MabelMetalBowl.jpg',
            'alt':'art',
            'link':'art',
            'caption':'art',
        },
    ]
    return render_template('projects.html', context=context)


@bp.route('/contact')
def contact():
    return render_template('contact.html')

# Additional routes can be added here