from datetime import datetime
from flask import Flask, url_for, render_template, redirect
from forms import LoginForm, NewRepoForm, NewContributionForm
from flask_wtf.csrf import CSRFProtect

import flask_login

from models import User, Repository


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "THE SECRET"


login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def user_loader(login):
    user = User.nodes.get_or_none(login=login)
    return user


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.user
        if flask_login.login_user(user):
            return redirect(url_for("index"))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))


@app.route('/')
@flask_login.login_required
def index(*args):
    user = flask_login.current_user
    contributed_repositories = user.contributed_repositories.all()
    owned_repositories = user.owned_repositories.all()
    return render_template(
        "index.html",
        contributed_repositories=contributed_repositories,
        owned_repositories=owned_repositories,
        user=user
    )


@app.route("/repository/new", methods=["GET", "POST"])
@flask_login.login_required
def create_repository(*args):
    user = flask_login.current_user
    form = NewRepoForm()
    if form.validate_on_submit():
        repo = Repository(
            name=form.name.data,
        )
        repo.save()
        user.owned_repositories.connect(repo)
        return redirect(url_for("index"))
    return render_template("repo_create.html", form=form)


@app.route("/repository/contribution/new", methods=["GET", "POST"])
@flask_login.login_required
def add_contribution(*args):
    user = flask_login.current_user
    form = NewContributionForm()
    if form.validate_on_submit():
        repo = Repository.nodes.get(
            name=form.name.data,
        )
        # connect repository and user
        user.contributed_repositories.connect(
            repo, {
                "contribution_date": datetime.now()
            }
        )
        return redirect(url_for("index"))
    return render_template("contribution_add.html", form=form)
