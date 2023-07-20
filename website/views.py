from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/gtaatop3')
@login_required
def gtaatop3():
    from . import gtaatop3
    values = gtaatop3.getGtaatop3()
    return render_template('gtaatop3.html', user=current_user, values=values)