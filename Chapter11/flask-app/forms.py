import flask_login
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import PasswordInput

from models import User, Repository


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = StringField(
        'Password', validators=[DataRequired()],
        widget=PasswordInput(hide_value=False)
    )
    submit = SubmitField('Submit')

    def validate(self):
        user = User.nodes.get_or_none(
            login=self.login.data,
            password=self.password.data,
        )
        if user is None:
            raise ValidationError("User/Password incorrect")
        self.user = user
        return self


class NewRepoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        user = flask_login.current_user
        r = user.contributed_repositories.get_or_none(name=field.data)
        if r is not None:
            raise ValidationError(
                'You already own a repository with that name'
            )


class NewContributionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        r = Repository.nodes.get_or_none(name=field.data)
        if r is None:
            raise ValidationError(
                'Can ony add contributions to existing repositories'
            )
