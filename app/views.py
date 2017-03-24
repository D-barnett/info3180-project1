"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import ProfileForm, LoginForm
from models import UserProfile

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profile", methods=('GET', 'POST'))
def create_userprofile():
    form = ProfileForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            firstname = form.first_name.data
            lastname = form.last_name.data
            age = form.age.data
            biography = form.biography.data
            email = form.email.data
            image =form.image.data 
            gender = form.gender.data 
      
            # save user to database
            user = UserProfile(id, username,firstname,lastname,age,biography,email,image,gender)
            db.session.add(user)
            db.session.commit()

            flash('User successfully added')
            return redirect(url_for('login'))
    flash_errors(form)
    return render_template('profile.html', form=form)
      
      
@app.route("/profile/<userid>", methods=('GET', 'POST'))
@login_required
def view_profile(userid):
    user=UserProfile.query.filter_by(userid=userid).first_or_404()
    if user is None:
        return render_template('404.html')
    return render_template('your_profile.html', user=user)
    
@app.route("/profiles", methods=['GET', 'POST'])
@login_required
def view_user_profiles():
    users = UserProfile.query.all()
    return render_template('all_users.html', users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # Validates that a username and password was entered on your login form
    if request.method == 'POST':
       if form.validate_on_submit():
            # Gets the username and password values from the form.
           username = request.form['username']
           email = request.form['email'] 
            
             # checks that the username and password entered matches a user that is in the database.
           user = UserProfile.query.filter(username==username, email==email).first()
           
           if user is not None:
             login_user(user)
             # flashes a message to the user
             flash('Logged in successfully.', 'success')
             return redirect(url_for("home"))
           else:
             flash('Username or Password is incorrect.', 'danger')

    flash_errors(form)
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    # Logouts the user and ends the session
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))
    
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
))
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
