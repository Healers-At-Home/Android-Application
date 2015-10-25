from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, IntegerField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, NumberRange, DataRequired, optional
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField
from ..models import User


class SearchForm(Form):
    search = StringField('Enter the phrase to search', validators=[DataRequired()])
    submit = SubmitField('Search')

class UserSearch(Form):
    search = StringField('Enter the username', validators=[DataRequired()])
    submit = SubmitField('Find User')


class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class PostForm(Form):
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')
    
    
class CommentForm(Form):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')

class Sendemail(Form):
    username = StringField('Username of the receiver')
    body = StringField('Enter the body of e-mail')
    submit = SubmitField('Send')