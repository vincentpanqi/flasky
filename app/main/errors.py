#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/10

from flask import render_template
from . import main

@main.app_errorhandler(403)
def server_Forbidden(e):
    return render_template('403.html'), 403

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
