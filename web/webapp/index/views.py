#-*- coding:utf-8 -*-
from flask import Blueprint, url_for, render_template, request,\
                  abort, flash, session, redirect
import json


mod = Blueprint('index', __name__, url_prefix='/index')


@mod.route('/')
def index():
    return 'Hello, world!'