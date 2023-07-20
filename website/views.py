from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user
from .models import User
from . import db

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

@views.route('/message', methods=['GET', 'POST'])
@login_required
def message():
    if request.method == 'POST':
        print('Post request')

        target_username = request.form.get('target_username')
        message = request.form.get('message')

        user = User.query.filter_by(username=target_username).first()
        if user:
            if len(message) > 1:
                if user.message:
                    user.message = user.message + f'<br>-> {datetime.now()} : {message}'
                    db.session.commit()
                    flash('Message sent!', category='success')
                else:
                    user.message = f'-> {datetime.now()} : {message}'
                    db.session.commit()
                    flash('Message sent!', category='success')
            else:
                flash('Message must be greater than 1 character!', category='error')
        else:
            flash(f'No user with the given username \'{target_username}\' found!', category='error')
            
    return render_template('message.html', user=current_user)

@views.route('/del-message', methods=['POST'])
@login_required
def del_message():
    current_user.message = None
    db.session.commit()
    flash(f'Successfully deleted all messages', category='success')

    return redirect(url_for('views.message'))