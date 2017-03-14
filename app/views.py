"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import ProfileForm, loginForm
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
    
@app.route("/profile/<userid>")
@login_required
def view_profile(userid):
    user=UserProfile.query.filter_by(userid==id).first()
    if user is None:
        return render_template('404.html')
    return render_template('profiles.html', user=user)
    
@app.route("/profiles")
@login_required
def view_user_profiles():
    user = UserProfile()
    db.session.query(user).all()
    return render_template('profiles.html')
    #@app.route('/filelisting', methods=['POST', 'GET'])
#def filelisting():
 #   if not session.get('logged_in'):
  #      abort(401)
        
  #  listpath = os.walk('/home/ubuntu/workspace/app/static/uploads' )
  #  for file in listpath:         
  #      print file
  #  return render_template('filelist.html', filelist=file)

@app.route("/profile", methods=('GET', 'POST'))
def create_userprofile():
    form = ProfileForm()
    if request.method == 'POST'and form.validate_on_submit():
        user = UserProfile(form.username.data, form.first_name.data, form.last_name.data, form.age.data, form.biography.data, form.email.data, form.image.data, form.gender.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('my_profile'))
    elif request.method == 'GET':
      return render_template('profile.html', form=form)
     
@app.route("/my_profile")
@login_required
def my_profile():
    return render_template('your_profile.html')
    
    #if form.validate_on_submit():
    #    user = UserProfile()
    #    form.populate_obj(user)
    #    db.session.add(user)
    #    db.session.commit()
    #    login_user(user)
    #    return redirect(url_for('tracking.index'))
    #return render_template('profile.html', form=form)
    # if user == None:
    #    flash('User %s not found.' % nickname)
    #    return redirect(url_for('login.html'))
    #return render_template('profiles.html')
    

@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()
    # Validates that a username and password was entered on your login form
    if request.method == 'POST' and form.validate_on_submit():
        if form.username.data:    
            # Gets the username and password values from the form.
           username = request.form['username']
           email = request.form['email'] 
            
             # checks that the username and password entered matches a user that is in the database.
           user = UserProfile.query.filter(username==username, email==email).first()
            
           login_user(user)

            # flashes a message to the user
           flash('Logged in successfully.', 'success')
           return redirect(url_for("my_profile"))
           
           if user is None:
                flash('Username or email is invalid' , 'error')
           
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
