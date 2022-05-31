from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .authforms import LoginForm, RegistrationForm
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user
auth = Blueprint ('auth', __name__, template_folder='auth_templates', url_prefix='/auth')



@auth.route('/login', methods=['GET', 'POST'])
def login():
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():
            #username = lform.username.data
            #password = lform.password.data
            user = User.query.filter_by(username=lform.username.data).first()
            if user and check_password_hash(user.password, lform.password.data):
                login_user(user)
                print('current_user', current_user.__dict__)
                flash(f'Success - you have been signed in, {user.username}.', category='success')
                return redirect(url_for('home'))
        else:
            flash(f'Sorry, that username or email is taken. Please try again.', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('signin.html', form=lform)


@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.data)
            newuser = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)
            
            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash('Sorry, that username or email is taken. Please try again.', 'danger')
                return redirect(url_for('auth.register'))
            login_user(newuser)
            flash('Welcome! Thank you for registering!', 'info')
            return redirect(url_for('home'))
        else:
            flash('Sorry, that username or email is taken. Please try again.', 'danger')
            return redirect(url_for('auth.register'))
    return render_template('register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been signed out.' , 'info')
    return redirect(url_for(auth.login))