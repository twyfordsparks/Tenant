from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from datetime import datetime
from time import time, sleep
from .forms import BlogFormI, CommentForm, EmailFormI
from ..models import User, BLOG, Comment, Subscribe
from flask_login import login_required, current_user
#from ..email import mail_message
import requests
import json
from .. import db

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the blog app'
    return render_template("index.html", title=title)
