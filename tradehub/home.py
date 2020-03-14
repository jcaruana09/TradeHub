import functools

from flask import Blueprint, render_template

bp = Blueprint('common', __name__)


@bp.route('/')
def home():
    return render_template('common/home.html')
